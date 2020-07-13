# frozen_string_literal: true

require 'rake'

@gce_registry = {
  push: 'docker push ' \
        "#{@project['google_user']}/" \
        "#{@project['project_id']}/" \
        "#{@project['google_repo']}-%<project_environment>s:" \
        "#{@project['version']}",
  tag: 'docker tag ' \
        "#{@project['local_user']}/" \
        "#{@project['project']}:%<project_environment>s " \
        "#{@project['google_user']}/#{@project['project_id']}/" \
        "#{@project['google_repo']}-%<project_environment>s:" \
        "#{@project['version']}"
}
