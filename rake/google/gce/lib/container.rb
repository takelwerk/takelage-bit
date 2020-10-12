# frozen_string_literal: true

require 'rake'

@gce_container = {
  create: 'gcloud compute instances ' \
          'create-with-container ' \
          "#{@project['google_repo']}-%<project_environment>s " \
          "--address=#{@project['ip_prod']} " \
          '--container-image= ' \
          "#{@project['google_user']}/#{@project['project_id']}/" \
          "#{@project['google_repo']}-%<project_environment>s:" \
          "#{@project['version']} " \
          '--container-privileged ' \
          "--machine-type=#{@project['machine_type_prod']} " \
          "--boot-disk-size=#{@project['boot_disk_size_prod']} " \
          "--project=#{@project['project_id']} " \
          '--scopes=storage-full ' \
          "--tags=#{@project['google_repo']}-%<project_environment>s " \
          "--zone=#{@project['google_zone']} ",
  list: 'gcloud compute instances list ' \
        "--project=#{@project['project_id']} ",
  update: 'gcloud compute instances ' \
          'update-container ' \
          "#{@project['google_repo']}-%<project_environment>s " \
          "--container-image=#{@project['google_user']}/" \
          "#{@project['project_id']}/" \
          "#{@project['google_repo']}-%<project_environment>s:" \
          "#{@project['version']} " \
          '--container-privileged ' \
          "--zone=#{@project['google_zone']} " \
          "--project=#{@project['project_id']} "
}
