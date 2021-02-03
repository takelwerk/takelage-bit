# frozen_string_literal: true

require 'rake'

@gce_firewall = {
  delete: 'gcloud compute firewall-rules delete %<rule_name>s  ' \
          "--project=#{@project['google_id']}",
  describe: 'gcloud compute firewall-rules describe  %<rule_name>s ' \
            "--project=#{@project['google_id']}",
  disable: 'gcloud compute firewall-rules update %<rule_name>s --disabled ' \
           "--project=#{@project['google_id']}",
  enable: 'gcloud compute firewall-rules update %<rule_name>s --no-disabled ' \
          "--project=#{@project['google_id']}",
  list: 'gcloud compute firewall-rules list ' \
        "--project=#{@project['google_id']}",
  create: 'gcloud compute firewall-rules create  %<rule_name>s ' \
          '--action=allow ' \
          '--rules %<proto>s:%<port>d ' \
          "--target-tags=#{@project['google_repo']}-%<rule_name>s " \
          "--project=#{@project['google_id']}"
}
