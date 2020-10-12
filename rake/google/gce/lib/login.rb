# frozen_string_literal: true

require 'rake'

env_url = "url_%<project_environment>s"

@gce_login = {
  host: 'gcloud beta compute ' \
        "ssh #{@project['google_repo']}-%<project_environment>s " \
        "--zone=#{@project['google_zone']} " \
        "--project=#{@project['google_id']} ",
  container: 'ssh ' \
             "-p #{@project['ssh_port']} " \
             '%<url_env>s'
}
