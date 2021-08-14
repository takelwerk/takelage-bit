[![license](https://img.shields.io/github/license/takelwerk/takelage-bit?color=blueviolet)](https://github.com/takelwerk/takelage-bit/blob/main/LICENSE)
[![hub.docker.com](https://img.shields.io/docker/v/takelwerk/bitboard/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelwerk/bitboard)
[![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_deploy_project_on_push.yml)
[![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_project_nightly.yml)
[![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_roles_nightly.yml)

# takelage-bit

*takelage-bit* is bit server to facilitate collaboration
using the takelage devops workflow.
The takelage devops workflow helps devops engineers
build, test and deploy os images.

A *takelage-bit* docker container called *bitboard* is published on 
[Docker Hub](https://hub.docker.com/r/takelwerk/bitboard).
It contains a 
[public ssh key pair](ansible/roles/takel-bit-server/files)
so it is usable for testing purposes only!

## Framework Versions

| App | Artifact |
| --- | -------- |
| *[takelage-doc](https://github.com/takelwerk/takelage-doc)* | [![License](https://img.shields.io/github/license/takelwerk/takelage-doc?color=blueviolet)](https://github.com/takelwerk/takelage-doc/blob/main/LICENSE) |
| *[takelage-dev](https://github.com/takelwerk/takelage-dev)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelage/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelwerk/takelage) |
| *[takelage-cli](https://github.com/takelwerk/takelage-cli)* | [![rubygems.org](https://img.shields.io/gem/v/takeltau?label=rubygems.org&color=blue)](https://rubygems.org/gems/takeltau) |
| *[takelage-var](https://github.com/takelwerk/takelage-var)* | [![pypi,org](https://img.shields.io/pypi/v/pytest-takeltest?label=pypi.org&color=blue)](https://pypi.org/project/pytest-takeltest/) |
| *[takelage-bit](https://github.com/takelwerk/takelage-bit)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/bitboard/latest?label=hub.docker.com&sort=semver&color=blue)](https://hub.docker.com/r/takelwerk/bitboard) | 
| *[takelage-img-takelslim](https://github.com/takelwerk/takelage-img-takelslim)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelslim/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelwerk/takelslim) | 
| *[takelage-img-takelbase](https://github.com/takelwerk/takelage-img-takelbase)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelbase/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelwerk/takelbase) | 
| *[takelage-img-takelruby](https://github.com/takelwerk/takelage-img-takelruby)* | [![hub.docker.com](https://img.shields.io/docker/v/takelwerk/takelruby/latest?label=hub.docker.com&color=blue)](https://hub.docker.com/r/takelwerk/takelruby) | 

## Framework Status

| App | Deploy project | Test project | Test roles |
| --- | -------------- | ------------ | ---------- |
| *[takelage-dev](https://github.com/takelwerk/takelage-dev)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_project_nightly.yml) | [![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-dev/Test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-dev/actions/workflows/build_test_roles_nightly.yml) |
| *[takelage-cli](https://github.com/takelwerk/takelage-cli)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-cli/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-cli/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-cli/Test%20project?label=test%20project)](https://github.com/takelwerk/takelage-cli/actions/workflows/test_project_nightly.yml) |
| *[takelage-var](https://github.com/takelwerk/takelage-var)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-var/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-var/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-var/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-var/actions/workflows/build_test_project_nightly.yml) |
| *[takelage-bit](https://github.com/takelwerk/takelage-bit)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Build,%20test%20and%20deploy%20project?label=deploy%20project)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_deploy_project_on_push.yml) | [![test project](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Build%20and%20test%20project?label=test%20project)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_project_nightly.yml) | [![test roles](https://img.shields.io/github/workflow/status/takelwerk/takelage-bit/Test%20roles?label=test%20roles)](https://github.com/takelwerk/takelage-bit/actions/workflows/build_test_roles_nightly.yml) |
| *[takelage-img-takelslim](https://github.com/takelwerk/takelage-img-takelslim)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-img-takelslim/Build%20and%20deploy%20takelslim?label=deploy%20project)](https://github.com/takelwerk/takelage-img-takelslim/actions/workflows/build_deploy_takelslim_nightly.yml) |
| *[takelage-img-takelbase](https://github.com/takelwerk/takelage-img-takelbase)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-img-takelbase/Build%20and%20deploy%20takelbase?label=deploy%20project)](https://github.com/takelwerk/takelage-img-takelbase/actions/workflows/build_deploy_takelbase_nightly.yml) |
| *[takelage-img-takelruby](https://github.com/takelwerk/takelage-img-takelruby)* | [![deploy project](https://img.shields.io/github/workflow/status/takelwerk/takelage-img-takelruby/Build%20and%20deploy%20takelruby%20latest?label=deploy%20project)](https://github.com/takelwerk/takelage-img-takelruby/actions/workflows/build_deploy_takelruby_nightly.yml) |

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
