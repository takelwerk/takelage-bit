# frozen_string_literal: true

require 'rake'

@gce_login = {
  host: 'gcloud beta compute ' \
        "ssh #{@project['google_repo']}-%<project_environment>s " \
        "--zone=#{@project['zone']} " \
        "--project=#{@project['project_id']} ",
  container: 'ssh ' \
             "-p #{@project['ssh_port']} " \
             "#{@project['url_prod']}"
}
