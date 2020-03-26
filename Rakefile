require 'rake'
require 'yaml'

$project = YAML.load(File.read('project.yml'))

# Add run=dry to see shell $commands
# Example: rake stage run=dry

#####################################################################
# Variables

$base_dir = ENV['TAKELAGE_PROJECT_BASE_DIR'] ? ENV['TAKELAGE_PROJECT_BASE_DIR'] : "/tmp/#{$project['project']}"
# The tasks will add shell commands to this empty global array
$commands = []

#####################################################################
# Default task

task :default do
  sh 'rake --tasks', verbose: false
end

#####################################################################
# Import Rakefiles from all subfolders in ./rake

Dir.glob("rake/**/Rakefile").each do |rakefile|
  import rakefile
end

#####################################################################
# Final task

# Detect run=dry command line parameter
dry_run = false
if ENV['run'] == 'dry'
  dry_run = true
end

# if Rakefile is invoked with run=dry
# then print commands
# else run commands
task :finally do
  $commands.each do |command|
    if dry_run
      puts command
    else
      sh command
    end
  end
end

# Run final task at exit
at_exit { Rake::Task[:finally].invoke if $!.nil? }
#####################################################################
