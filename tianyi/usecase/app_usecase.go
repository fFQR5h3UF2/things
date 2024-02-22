package usecase

import (
	useBranch "shishifubing.com/tianyi/usecase/branch"
	useJob "shishifubing.com/tianyi/usecase/job"
	useJWT "shishifubing.com/tianyi/usecase/jwt"
	useLifecycle "shishifubing.com/tianyi/usecase/lifecycle"
	usePipeline "shishifubing.com/tianyi/usecase/pipeline"
	usePool "shishifubing.com/tianyi/usecase/pool"
	useProject "shishifubing.com/tianyi/usecase/project"
	useSession "shishifubing.com/tianyi/usecase/session"
	useUser "shishifubing.com/tianyi/usecase/user"
)

type Interactor interface {
	Lifecycle() useLifecycle.Interactor
	User() useUser.Interactor
	// Access    usecaseAccess.Interactor
	JWT() useJWT.Interactor
	Project() useProject.Interactor
	Branch() useBranch.Interactor
	Session() useSession.Interactor
	Pool() usePool.Interactor
	Job() useJob.Interactor
	Pipeline() usePipeline.Interactor
}

func New(
	lifecycle useLifecycle.Interactor, user useUser.Interactor,
	jwt useJWT.Interactor, project useProject.Interactor,
	branch useBranch.Interactor, session useSession.Interactor,
	pool usePool.Interactor, job useJob.Interactor,
	pipeline usePipeline.Interactor,
) Interactor {
	return &interactor{
		lifecycle, user, jwt, project, branch, session, pool, job, pipeline,
	}
}

type interactor struct {
	lifecycle useLifecycle.Interactor
	user      useUser.Interactor
	// Access    usecaseAccess.Interactor
	jwt      useJWT.Interactor
	project  useProject.Interactor
	branch   useBranch.Interactor
	session  useSession.Interactor
	pool     usePool.Interactor
	job      useJob.Interactor
	pipeline usePipeline.Interactor
}

func (i *interactor) Lifecycle() useLifecycle.Interactor { return i.lifecycle }
func (i *interactor) User() useUser.Interactor           { return i.user }
func (i *interactor) JWT() useJWT.Interactor             { return i.jwt }
func (i *interactor) Project() useProject.Interactor     { return i.project }
func (i *interactor) Branch() useBranch.Interactor       { return i.branch }
func (i *interactor) Session() useSession.Interactor     { return i.session }
func (i *interactor) Pool() usePool.Interactor           { return i.pool }
func (i *interactor) Job() useJob.Interactor             { return i.job }
func (i *interactor) Pipeline() usePipeline.Interactor   { return i.pipeline }
