package infra

import (
	infraConfig "shishifubing.com/tianyi/infrastructure/config"
	infraLifecycle "shishifubing.com/tianyi/infrastructure/lifecycle"
	useLifecycle "shishifubing.com/tianyi/usecase/lifecycle"
)

func NewApp(configs ...*infraConfig.App) useLifecycle.Interactor {
	return useLifecycle.New(infraLifecycle.New(configs...).Setup())
}
