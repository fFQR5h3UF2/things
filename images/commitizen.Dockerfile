FROM python:alpine3.19@sha256:ae1f508f01ac1806e84c68b43ee0983b586426dfa39f5d21eced0dd7f5e230f4
LABEL org.opencontainers.image.source="https://github.com/shishifubing/dotfiles"
LABEL org.opencontainers.image.description="Commitizen image"
RUN apk add --no-cache gnupg git
RUN pip install --no-cache-dir commitizen
