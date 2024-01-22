FROM python:alpine3.19@sha256:801b54e1ec51c23dd6f174f3f26a0ff5bf2a002c4bc0bf05b0e2b9237e10f5b8
LABEL org.opencontainers.image.source="https://github.com/shishifubing/dotfiles"
LABEL org.opencontainers.image.description="Commitizen image"
RUN apk add --no-cache gnupg git
RUN pip install --no-cache-dir commitizen
