package usePool

import (
	"shishifubing.com/pkg/tianyi/entity"
)

type (
	Handler      func(job *entity.Job) error
	ErrorHandler func(job *entity.Job, err error) error
)

type Interactor interface {
	Pool() Pool
}

type Pool interface {
	// define a job
	Job(name string, handler Handler, errorHandler ErrorHandler)
	// start the pool
	Start()
	// close the pool
	Close() error
}
