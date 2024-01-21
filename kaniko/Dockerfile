FROM gcr.io/kaniko-project/executor:v1.19.2-debug@sha256:899886a2db1c127ff1565d5c7b1e574af1810bbdad048e9850e4f40b5848d79c
COPY . /action
ENTRYPOINT [ "/busybox/sh", "/action/run_kaniko.sh" ]
