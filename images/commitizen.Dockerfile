FROM python:alpine3.19@sha256:c793b92fd9e0e2a0b611756788a033d569ca864b733461c8fb30cfd14847dbcf
LABEL org.opencontainers.image.source="https://github.com/shishifubing/dotfiles"
LABEL org.opencontainers.image.description="Commitizen image"
RUN apk add --no-cache gnupg git
RUN pip install --no-cache-dir commitizen
