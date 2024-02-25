package useJWT

import "shishifubing.com/pkg/tianyi/entity"

type Interactor interface {
	// generate user jwt
	New(user *entity.User) (string, error)
	// get claims from jwt
	Claims(token interface{}) (*entity.JWTClaims, error)
}
