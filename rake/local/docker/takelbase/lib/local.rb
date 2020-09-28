# frozen_string_literal: true

require 'rake'

@cmd_local_docker_takelbase_molecule_command = "cd ansible && bash -c '" \
  'TAKELAGE_DOCKER_CMD_OVERRIDE=%<docker_command_override>s ' \
  'TAKELAGE_DOCKER_CMD=%<docker_command>s ' \
  'TAKELAGE_DOCKER_MOUNT_PATH=%<docker_mount_path>s ' \
  'TAKELAGE_DOCKER_TTY=%<docker_tty>s ' \
  'TAKELAGE_PROJECT_ENV=%<project_environment>s ' \
  "TAKELAGE_PROJECT_NAME=#{@project['name']} " \
  "molecule %<molecule_command>s --scenario-name local'"

@cmd_local_docker_takelbase_molecule_features = \
  'cd ansible && ' \
  'TAKELAGE_PROJECT_ENV=%<project_environment>s ' \
  'molecule dependency --scenario-name local'

@cmd_local_docker_takelbase_molecule_log = 'docker logs -f ' \
  "molecule-takel-#{@project['name']}-local-%<project_environment>s"

@cmd_local_docker_takelbase_molecule_list_command = "cd ansible && bash -c '" \
  'TAKELAGE_DOCKER_CMD_OVERRIDE=%<docker_command_override>s ' \
  'TAKELAGE_DOCKER_CMD=%<docker_command>s ' \
  'TAKELAGE_DOCKER_MOUNT_PATH=%<docker_mount_path>s ' \
  'TAKELAGE_DOCKER_TTY=%<docker_tty>s ' \
  'TAKELAGE_PROJECT_ENV=%<project_environment>s ' \
  "molecule %<molecule_command>s'"

@cmd_local_docker_takelbase_list = {
  converge: @cmd_local_docker_takelbase_molecule_command,
  destroy: @cmd_local_docker_takelbase_molecule_command,
  list: @cmd_local_docker_takelbase_molecule_list_command,
  login: @cmd_local_docker_takelbase_molecule_command,
  verify: @cmd_local_docker_takelbase_molecule_command,
  features: @cmd_local_docker_takelbase_molecule_features,
  log: @cmd_local_docker_takelbase_molecule_log
}
