#!/usr/bin/env python
from resource_management import *
from resource_management.libraries.script.script import Script
import sys, os, glob
from resource_management.libraries.functions.version import format_hdp_stack_version
from resource_management.libraries.functions.default import default



# server configurations
config = Script.get_config()



# # params from flink-ambari-config
# flink_install_dir = config['configurations']['flink-ambari-config']['flink_install_dir']
# flink_numcontainers = config['configurations']['flink-ambari-config']['flink_numcontainers']
# flink_jobmanager_memory = config['configurations']['flink-ambari-config']['flink_jobmanager_memory']
# flink_container_memory = config['configurations']['flink-ambari-config']['flink_container_memory']
# setup_prebuilt = config['configurations']['flink-ambari-config']['setup_prebuilt']
# flink_appname = config['configurations']['flink-ambari-config']['flink_appname']
# flink_queue = config['configurations']['flink-ambari-config']['flink_queue']
# flink_streaming = config['configurations']['flink-ambari-config']['flink_streaming']
#
# hadoop_conf_dir = config['configurations']['flink-ambari-config']['hadoop_conf_dir']
# flink_download_url = config['configurations']['flink-ambari-config']['flink_download_url']
#
#
# conf_dir=''
# bin_dir=''

# params from flink-conf.yaml
impala_user = config['configurations']['impala-env']['impala_user']
impala_group = config['configurations']['impala-env']['impala_group']
impala_log_dir = config['configurations']['impala-env']['impala_log_dir']
impala_log_file = os.path.join(impala_log_dir,'impala-setup.log')