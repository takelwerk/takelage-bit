[![takelage image](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_project_nightly.yml/badge.svg)](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_project_nightly.yml)
[![ansible roles](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_roles_nightly.yml/badge.svg)](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_roles_nightly.yml)
[![hub.docker.com](https://img.shields.io/docker/v/takelage/bitboard/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelage/bitboard)
[![License](https://img.shields.io/github/license/geospin-takelage/takelage-bit?label=License&color=blueviolet)](https://github.com/geospin-takelage/takelage-bit/blob/main/LICENSE)

# takelage-bit

*takelage-bit* is bit server to facilitate collaboration
using the takelage devops workflow.
The takelage devops workflow helps devops engineers
build, test and deploy os images.

A *takelage-bit* docker container called *bitboard* is published on 
[Docker Hub](https://hub.docker.com/r/takelage/bitboard).
It contains a 
[public ssh key pair](ansible/roles/takel-bit-server/files)
so it is usable for testing purposes only!

## Framework Versions

| App | Artifact |
| --- | -------- |
| *[takelage-doc](https://github.com/geospin-takelage/takelage-doc)* | [![License](https://img.shields.io/github/license/geospin-takelage/takelage-doc?label=License&color=blueviolet)](https://github.com/geospin-takelage/takelage-doc/blob/main/LICENSE) |
| *[takelage-dev](https://github.com/geospin-takelage/takelage-dev)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/takelage/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelage/takelage) |
| *[takelage-cli](https://github.com/geospin-takelage/takelage-cli)* | [![rubygems.org](https://img.shields.io/gem/v/takelage?label=rubygems.org&color=blue)](https://rubygems.org/gems/takelage) |
| *[takelage-var](https://github.com/geospin-takelage/takelage-var)* | [![pypi,org](https://img.shields.io/pypi/v/takeltest?label=pypi.org&color=blue)](https://pypi.org/project/takeltest/) |
| *[takelage-bit](https://github.com/geospin-takelage/takelage-bit)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/bitboard/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelage/bitboard) | 
| *[takelage-img-takelslim](https://github.com/geospin-takelage/takelage-img-takelslim)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/takelslim/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelage/takelslim) | 
| *[takelage-img-takelbase](https://github.com/geospin-takelage/takelage-img-takelbase)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/takelbase/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelage/takelbase) | 
| *[takelage-img-multipostgres](https://github.com/geospin-takelage/takelage-img-multipostgres)* | [![hub.docker.com](https://img.shields.io/docker/v/takelage/multipostgres/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelage/multipostgres) | 

## Framework Status

| App | Deploy project | Test project | Test roles |
| --- | -------------- | ------------ | ---------- |
| *[takelage-dev](https://github.com/geospin-takelage/takelage-dev)* | [![deploy project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-dev/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/geospin-takelage/takelage-dev/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-dev/Build%20and%20test%20project?label=test%20project)](https://github.com/geospin-takelage/takelage-dev/actions/workflows/build_test_project_nightly.yml) | [![test roles](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-dev/Test%20roles?label=test%20roles)](https://github.com/geospin-takelage/takelage-dev/actions/workflows/build_test_roles_nightly.yml) |
| *[takelage-cli](https://github.com/geospin-takelage/takelage-cli)* | [![deploy project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-cli/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/geospin-takelage/takelage-cli/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-cli/Test%20project?label=test%20project)](https://github.com/geospin-takelage/takelage-cli/actions/workflows/test_project_nightly.yml) |
| *[takelage-var](https://github.com/geospin-takelage/takelage-var)* |[![deploy project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-var/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/geospin-takelage/takelage-var/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-var/Build%20and%20test%20project?label=test%20project)](https://github.com/geospin-takelage/takelage-var/actions/workflows/build_test_project_nightly.yml) |
| *[takelage-bit](https://github.com/geospin-takelage/takelage-bit)* | [![deploy project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-bit/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-bit/Build%20and%20test%20project?label=test%20project)](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_project_nightly.yml) | [![test roles](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-bit/Test%20roles?label=test%20roles)](https://github.com/geospin-takelage/takelage-bit/actions/workflows/build_test_roles_nightly.yml) |
| *[takelage-img-takelslim](https://github.com/geospin-takelage/takelage-img-takelslim)* | [![deploy project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-img-takelslim/Build%20and%20deploy%20takelslim?label=deploy%20project)](https://github.com/geospin-takelage/takelage-img-takelslim/actions/workflows/build_deploy_takelslim_nightly.yml) |
| *[takelage-img-takelbase](https://github.com/geospin-takelage/takelage-img-takelbase)* | [![deploy project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-img-takelbase/Build%20and%20deploy%20takelbase?label=deploy%20project)](https://github.com/geospin-takelage/takelage-img-takelbase/actions/workflows/build_deploy_takelbase_nightly.yml) |
| *[takelage-img-multipostgres](https://github.com/geospin-takelage/takelage-img-multipostgres)* | [![deploy project](https://img.shields.io/github/workflow/status/geospin-takelage/takelage-img-multipostgres/Build%20and%20deploy%20multipostgres?label=deploy%20project)](https://github.com/geospin-takelage/takelage-img-multipostgres/actions/workflows/build_deploy_multipostgres_nightly.yml) |

## bit

[bit](https://github.com/teambit/bit) is a 
[git](https://git-scm.com) extension.
bit is not meant to replace git.
You may think of bit as a git powered clipboard manager
with versioning and central storage.
For open source projects you may use [bit.dev](https://bit.dev)
as your central bit storage.
For software testing or private use you may use a *bitboard* server
created with this project.

Both bit and git are in their core free and open source tools.
Around these tools both free and non-free infrastructure has emerged.
git sparked projects like [GitHub](https://github.com) and 
[GitLab](https://gitlab.com) while bit has been
developed by Cocycles, the company behind 
[bit.dev](https://bit.dev).

bit.dev's intended audience is the javascript community and
they also host the best resources for bit: 
the [bit docs](https://docs.bit.dev/docs/faq).

The takelage devops workflow uses the open source parts of bit.
The bit part of takelage is targeting devops engineers.
It enables them to share parts of their git repositories.
And they may inject private data into open source projects.
