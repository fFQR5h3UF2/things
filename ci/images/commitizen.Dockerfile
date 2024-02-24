FROM python:alpine3.19@sha256:1a0501213b470de000d8432b3caab9d8de5489e9443c2cc7ccaa6b0aa5c3148e
LABEL org.opencontainers.image.source="https://github.com/shishifubing/dotfiles"
LABEL org.opencontainers.image.description="Commitizen image"
RUN apk add --no-cache gnupg git
RUN pip install --no-cache-dir commitizen
