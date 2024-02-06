FROM python:alpine3.19@sha256:14cfc61fc2404da8adc7b1cb1fcb299aefafab22ae571f652527184fbb21ce69
LABEL org.opencontainers.image.source="https://github.com/shishifubing/dotfiles"
LABEL org.opencontainers.image.description="Commitizen image"
RUN apk add --no-cache gnupg git
RUN pip install --no-cache-dir commitizen
