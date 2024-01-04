# alpine:3.19
FROM python@sha256:ae1f508f01ac1806e84c68b43ee0983b586426dfa39f5d21eced0dd7f5e230f4
RUN apk add --no-cache gnupg git
RUN pip install --no-cache-dir commitizen
