# 24.04
FROM ubuntu@sha256:1395dff3ecc43bbc9c1fb2af3b9d8c0df89ef9ef5f11f7ac69c6e0875862ef08
RUN apt-get update && \
    apt-get install -y gpg git python3 python3-pip python3-venv
COPY . /action
ENTRYPOINT [ "/action/bump_version.sh" ]
