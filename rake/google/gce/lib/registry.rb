# frozen_string_literal: true

require 'rake'

@gce_registry = {
  push: 'docker push ' \
        "#{@project['google_user']}/" \
        "#{@project['google_id']}/" \
        "#{@project['google_repo']}-%<project_environment>s:" \
        "#{@project['version']}",
  tag: 'docker tag ' \
        "#{@project['local_user']}/" \
        "#{@project['name']}:%<project_environment>s " \
        "#{@project['google_user']}/#{@project['google_id']}/" \
        "#{@project['google_repo']}-%<project_environment>s:" \
        "#{@project['version']}"
}
