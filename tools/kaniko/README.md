# kaniko

Kaniko wrapper

## Usage

```yaml
name: On tag
on:
  push:
    tags:
      - "v*"
jobs:
  publish_image:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
      - uses: ./kaniko
        with:
          dockerfile: images/commitizen.Dockerfile
          destination: shishifubing/commitizen:${{ github.ref_name }}
          token: ${{ secrets.CI_DOCKERHUB_TOKEN }}
```
