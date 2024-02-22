package infraLifecycle

import (
	"fmt"
	"log"
	"os"
	"os/signal"
	"sync"
	"sync/atomic"
	"syscall"

	"github.com/gofiber/fiber/v2"
	"gorm.io/gorm"

	"shishifubing.com/tianyi/api/controller"
	"shishifubing.com/tianyi/docs"
	"shishifubing.com/tianyi/pkg"
	web2 "shishifubing.com/tianyi/web"

	infraBranch "shishifubing.com/tianyi/infrastructure/branch"
	infraConfig "shishifubing.com/tianyi/infrastructure/config"
	infraJob "shishifubing.com/tianyi/infrastructure/job"
	infraJWT "shishifubing.com/tianyi/infrastructure/jwt"
	infraPipeline "shishifubing.com/tianyi/infrastructure/pipeline"
	infraPool "shishifubing.com/tianyi/infrastructure/pool"
	infraProject "shishifubing.com/tianyi/infrastructure/project"
	infraSession "shishifubing.com/tianyi/infrastructure/session"
	infraUser "shishifubing.com/tianyi/infrastructure/user"

	usecase "shishifubing.com/tianyi/usecase"
	useBranch "shishifubing.com/tianyi/usecase/branch"
	useJob "shishifubing.com/tianyi/usecase/job"
	useLifecycle "shishifubing.com/tianyi/usecase/lifecycle"
	usePipeline "shishifubing.com/tianyi/usecase/pipeline"
	usePool "shishifubing.com/tianyi/usecase/pool"
	useProject "shishifubing.com/tianyi/usecase/project"

	useSession "shishifubing.com/tianyi/usecase/session"
	useUser "shishifubing.com/tianyi/usecase/user"
)

var (
	Version     = 1.00
	Title       = "天意 Tianyi"
	Description = "description"
)

type infrastructure struct {
	user     useUser.Repository     `validate:"required"`
	project  useProject.Repository  `validate:"required"`
	branch   useBranch.Repository   `validate:"required"`
	session  useSession.Interactor  `validate:"required"`
	pool     usePool.Pool           `validate:"required"`
	job      useJob.Repository      `validate:"required"`
	pipeline usePipeline.Repository `validate:"required"`
}

type app struct {
	conf   *infraConfig.App
	db     *gorm.DB
	router *fiber.App
	ctrl   *controller.App
	inter  usecase.Interactor
	infra  *infrastructure
}

func New(configs ...*infraConfig.App) useLifecycle.App {
	app := &app{}
	if len(configs) != 0 {
		app.conf = configs[0]
	} else {
		confCopy := infraConfig.Default
		app.conf = &confCopy
	}
	return app
}

func (a *app) Migrate() error {
	repositories := []interface{ Migrate() error }{
		a.infra.branch, a.infra.project, a.infra.user,
	}
	for _, repo := range repositories {
		if err := repo.Migrate(); err != nil {
			return err
		}
	}
	return nil
}

func (a *app) Run() {
	go a.Listen()
	a.ShutdownOnInterruptionSignal()
}

func (a *app) Listen() {
	defer a.ShutdownOnPanic()
	err := a.router.Listen(":" + a.conf.Server.Port)
	if err == nil {
		return
	}
	log.Println("Runtime error:\n", err)
	a.Shutdown(1)
}

func (a *app) ShutdownOnPanic() {
	err := recover()
	if err == nil {
		return
	}
	log.Println("Runtime panic:\n", err)
	a.Shutdown(1)
}

func (a *app) Shutdown(code int) {
	log.Println("Shutting down...")
	shutdowns := []func() error{
		a.router.Shutdown, a.infra.session.Close, a.infra.pool.Close,
	}
	waitGroup, failToggle := sync.WaitGroup{}, int32(0)
	for _, shutdown := range shutdowns {
		waitGroup.Add(1)
		go func(shutdown func() error) {
			defer waitGroup.Done()
			if err := shutdown(); err != nil {
				atomic.AddInt32(&failToggle, 1)
				log.Println(err)
			}
		}(shutdown)
	}
	waitGroup.Wait()
	if failToggle != 0 {
		os.Exit(1)
	}
	os.Exit(code)
}

func (a *app) ShutdownOnInterruptionSignal() {
	// ch for the interruption signal
	ch := make(chan os.Signal, 1)
	// when an interruption or termination signal is sent, shutdown
	signal.Notify(ch, os.Interrupt, syscall.SIGTERM)
	// wait for it and shutdown
	<-ch
	a.Shutdown(0)
}

func (a *app) Setup() useLifecycle.App {
	return a.
		SetupConfig().
		SetupDatabase().
		SetupInfrastructure().
		SetupInteractor().
		SetupController().
		SetupSwagger().
		SetupRouter()
}

func (a *app) SetupConfig() useLifecycle.App {
	a.conf.Populate()
	return a
}

func (a *app) SetupDatabase() useLifecycle.App {
	a.db = connectDatabase(a.conf.DB)
	return a
}

func (a *app) SetupInfrastructure() useLifecycle.App {
	if a.db == nil {
		log.Panicln("database is nil")
	}
	job := infraJob.New(a.db)
	a.infra = &infrastructure{
		user:     infraUser.New(a.db),
		project:  infraProject.New(a.db),
		branch:   infraBranch.New(a.db),
		session:  infraSession.New(a.conf.Redis),
		pool:     infraPool.New(a.conf, job),
		job:      job,
		pipeline: infraPipeline.New(a.db),
	}
	if err := pkg.ValidateStruct(a.infra); err != nil {
		panic(err)
	}
	return a
}

func (a *app) SetupInteractor() useLifecycle.App {
	if a.infra == nil {
		log.Panicln("repository is nil")
	}
	branch := useBranch.New(a.infra.branch)
	job := useJob.New(a.infra.job)
	a.inter = usecase.New(
		useLifecycle.New(a),
		useUser.New(a.infra.user),
		infraJWT.New(a.conf.Server.JWT),
		useProject.New(a.infra.project, branch),
		branch,
		useSession.New(a.infra.session),
		usePool.New(a.infra.pool),
		job,
		usePipeline.New(a.infra.pipeline, job),
	)
	return a
}

func (a *app) SetupController() useLifecycle.App {
	if a.infra == nil {
		log.Panicln("repository is nil")
	}
	jwt := controller.NewJWT(a.conf.Server.JWT.GetSecret())
	inter, infra := a.inter, a.infra
	a.ctrl = &controller.App{
		User: controller.NewUser(inter.User(), inter.Session()),
		Frontend: controller.NewFrontend(
			web2.FrontendFilesystem, docs.SwaggerFilesystem,
		),
		Session:   controller.NewSession(infra.session, jwt, inter.JWT()),
		Lifecycle: controller.NewLifecycle(inter.Lifecycle()),
		Project:   controller.NewProject(inter.Project()),
		Branch:    controller.NewBranch(inter.Branch(), inter.Project()),
		Pipeline: controller.NewPipeline(
			inter.Branch(), inter.Project(), inter.Pipeline(),
		),
		JWT: jwt,
	}
	if err := pkg.ValidateStruct(a.ctrl); err != nil {
		log.Panicln(err)
	}
	infra.pool.Job(
		usePipeline.InteractorKey,
		inter.Pipeline().RunJob, inter.Pipeline().JobErrorHandler,
	)
	return a
}

func (a *app) SetupSwagger() useLifecycle.App {
	docs.SwaggerInfo.Title = Title
	docs.SwaggerInfo.Description = Description
	docs.SwaggerInfo.Version = fmt.Sprintf("%.2f", Version)
	docs.SwaggerInfo.Host = fmt.Sprintf(
		"%s:%s", a.conf.Server.Host, a.conf.Server.Port,
	)
	docs.SwaggerInfo.BasePath = "/"
	docs.SwaggerInfo.Schemes = []string{"http", "https"}
	return a
}

func (a *app) SetupRouter() useLifecycle.App {
	if a.ctrl == nil {
		log.Panicln("controller is nil")
	}
	a.router = newRouter(a.conf.Fiber)
	setupRouter(a.router, a.ctrl, a.conf)
	return a
}
