package infra

import (
	infraConfig "shishifubing.com/pkg/tianyi/infrastructure/config"
	infraLifecycle "shishifubing.com/pkg/tianyi/infrastructure/lifecycle"
	useLifecycle "shishifubing.com/pkg/tianyi/usecase/lifecycle"
)

func NewApp(configs ...*infraConfig.App) useLifecycle.Interactor {
	return useLifecycle.New(infraLifecycle.New(configs...).Setup())
}
