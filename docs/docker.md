```python
❯ docker run --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

Unable to find image 'rabbitmq:3-management' locally
3-management: Pulling from library/rabbitmq
bccd10f490ab: Pull complete 
f1000ca5c91d: Pull complete 
15fd8d52bc6c: Pull complete 
d9b381d4c87a: Pull complete 
497a9eb5f435: Pull complete 
dd2bd0cede52: Pull complete 
bed3197826ba: Pull complete 
0c1d09ec487d: Pull complete 
a89de7acba35: Pull complete 
74d11b8768c5: Pull complete 
b8a34a89caa8: Pull complete 
853ab4a97c91: Pull complete 
Digest: sha256:18d7104751b66c882c109349f537108c7cd979d87fe9020ef4dc4d773d37691e
Status: Downloaded newer image for rabbitmq:3-management
2024-03-19 09:45:38.598157+00:00 [notice] <0.44.0> Application syslog exited with reason: stopped
2024-03-19 09:45:38.604948+00:00 [notice] <0.248.0> Logging: switching to configured handler(s); following messages may not be visible in this log output
2024-03-19 09:45:38.605771+00:00 [notice] <0.248.0> Logging: configured log handlers are now ACTIVE
2024-03-19 09:45:38.615279+00:00 [info] <0.248.0> ra: starting system quorum_queues
2024-03-19 09:45:38.615390+00:00 [info] <0.248.0> starting Ra system: quorum_queues in directory: /var/lib/rabbitmq/mnesia/rabbit@747398c0cd45/quorum/rabbit@747398c0cd45
2024-03-19 09:45:38.727128+00:00 [info] <0.262.0> ra system 'quorum_queues' running pre init for 0 registered servers
2024-03-19 09:45:38.747487+00:00 [info] <0.263.0> ra: meta data store initialised for system quorum_queues. 0 record(s) recovered
2024-03-19 09:45:38.773648+00:00 [notice] <0.268.0> WAL: ra_log_wal init, open tbls: ra_log_open_mem_tables, closed tbls: ra_log_closed_mem_tables
2024-03-19 09:45:38.878267+00:00 [info] <0.248.0> ra: starting system coordination
2024-03-19 09:45:38.878380+00:00 [info] <0.248.0> starting Ra system: coordination in directory: /var/lib/rabbitmq/mnesia/rabbit@747398c0cd45/coordination/rabbit@747398c0cd45
2024-03-19 09:45:38.880612+00:00 [info] <0.275.0> ra system 'coordination' running pre init for 0 registered servers
2024-03-19 09:45:38.881688+00:00 [info] <0.276.0> ra: meta data store initialised for system coordination. 0 record(s) recovered
2024-03-19 09:45:38.881967+00:00 [notice] <0.281.0> WAL: ra_coordination_log_wal init, open tbls: ra_coordination_log_open_mem_tables, closed tbls: ra_coordination_log_closed_mem_tables
2024-03-19 09:45:38.887188+00:00 [info] <0.248.0> ra: starting system coordination
2024-03-19 09:45:38.887317+00:00 [info] <0.248.0> starting Ra system: coordination in directory: /var/lib/rabbitmq/mnesia/rabbit@747398c0cd45/coordination/rabbit@747398c0cd45
2024-03-19 09:45:39.196255+00:00 [info] <0.248.0> Waiting for Khepri leader for 30000 ms, 9 retries left
2024-03-19 09:45:39.209004+00:00 [notice] <0.284.0> RabbitMQ metadata store: candidate -> leader in term: 1 machine version: 0
2024-03-19 09:45:39.226996+00:00 [info] <0.248.0> Khepri leader elected
2024-03-19 09:45:39.943637+00:00 [info] <0.248.0> 
2024-03-19 09:45:39.943637+00:00 [info] <0.248.0>  Starting RabbitMQ 3.13.0 on Erlang 26.2.2 [jit]
2024-03-19 09:45:39.943637+00:00 [info] <0.248.0>  Copyright (c) 2007-2024 Broadcom Inc and/or its subsidiaries
2024-03-19 09:45:39.943637+00:00 [info] <0.248.0>  Licensed under the MPL 2.0. Website: https://rabbitmq.com

  ##  ##      RabbitMQ 3.13.0
  ##  ##
  ##########  Copyright (c) 2007-2024 Broadcom Inc and/or its subsidiaries
  ######  ##
  ##########  Licensed under the MPL 2.0. Website: https://rabbitmq.com

  Erlang:      26.2.2 [jit]
  TLS Library: OpenSSL - OpenSSL 3.1.5 30 Jan 2024
  Release series support status: supported

  Doc guides:  https://www.rabbitmq.com/docs/documentation
  Support:     https://www.rabbitmq.com/docs/contact
  Tutorials:   https://www.rabbitmq.com/tutorials
  Monitoring:  https://www.rabbitmq.com/docs/monitoring

  Logs: <stdout>

  Config file(s): /etc/rabbitmq/conf.d/10-defaults.conf

  Starting broker...2024-03-19 09:45:39.944994+00:00 [info] <0.248.0> 
2024-03-19 09:45:39.944994+00:00 [info] <0.248.0>  node           : rabbit@747398c0cd45
2024-03-19 09:45:39.944994+00:00 [info] <0.248.0>  home dir       : /var/lib/rabbitmq
2024-03-19 09:45:39.944994+00:00 [info] <0.248.0>  config file(s) : /etc/rabbitmq/conf.d/10-defaults.conf
2024-03-19 09:45:39.944994+00:00 [info] <0.248.0>  cookie hash    : GVBmQ8wB1yzQVROOsZh7/g==
2024-03-19 09:45:39.944994+00:00 [info] <0.248.0>  log(s)         : <stdout>
2024-03-19 09:45:39.944994+00:00 [info] <0.248.0>  data dir       : /var/lib/rabbitmq/mnesia/rabbit@747398c0cd45
2024-03-19 09:45:40.492700+00:00 [info] <0.248.0> Running boot step pre_boot defined by app rabbit
2024-03-19 09:45:40.492815+00:00 [info] <0.248.0> Running boot step rabbit_global_counters defined by app rabbit
2024-03-19 09:45:40.493401+00:00 [info] <0.248.0> Running boot step rabbit_osiris_metrics defined by app rabbit
2024-03-19 09:45:40.493577+00:00 [info] <0.248.0> Running boot step rabbit_core_metrics defined by app rabbit
2024-03-19 09:45:40.494252+00:00 [info] <0.248.0> Running boot step rabbit_alarm defined by app rabbit
2024-03-19 09:45:40.512992+00:00 [info] <0.321.0> Memory high watermark set to 4738 MiB (4968364441 bytes) of 11845 MiB (12420911104 bytes) total
2024-03-19 09:45:40.521731+00:00 [info] <0.323.0> Enabling free disk space monitoring (disk free space: 4573888512, total memory: 12420911104)
2024-03-19 09:45:40.521958+00:00 [info] <0.323.0> Disk free limit set to 50MB
2024-03-19 09:45:40.526798+00:00 [info] <0.248.0> Running boot step code_server_cache defined by app rabbit
2024-03-19 09:45:40.527049+00:00 [info] <0.248.0> Running boot step file_handle_cache defined by app rabbit
2024-03-19 09:45:40.552044+00:00 [info] <0.326.0> Limiting to approx 1048479 file handles (943629 sockets)
2024-03-19 09:45:40.552388+00:00 [info] <0.327.0> FHC read buffering: OFF
2024-03-19 09:45:40.552466+00:00 [info] <0.327.0> FHC write buffering: ON
2024-03-19 09:45:40.553474+00:00 [info] <0.248.0> Running boot step worker_pool defined by app rabbit
2024-03-19 09:45:40.553957+00:00 [info] <0.307.0> Will use 4 processes for default worker pool
2024-03-19 09:45:40.554169+00:00 [info] <0.307.0> Starting worker pool 'worker_pool' with 4 processes in it
2024-03-19 09:45:40.555976+00:00 [info] <0.248.0> Running boot step database defined by app rabbit
2024-03-19 09:45:40.556598+00:00 [info] <0.248.0> Peer discovery: configured backend: rabbit_peer_discovery_classic_config
2024-03-19 09:45:40.557991+00:00 [notice] <0.308.0> Feature flags: attempt to enable `detailed_queues_endpoint`...
2024-03-19 09:45:40.697906+00:00 [notice] <0.308.0> Feature flags: `detailed_queues_endpoint` enabled
2024-03-19 09:45:40.698094+00:00 [notice] <0.308.0> Feature flags: attempt to enable `stream_update_config_command`...
2024-03-19 09:45:40.842704+00:00 [notice] <0.308.0> Feature flags: `stream_update_config_command` enabled
2024-03-19 09:45:40.842960+00:00 [notice] <0.308.0> Feature flags: attempt to enable `stream_filtering`...
2024-03-19 09:45:41.019106+00:00 [notice] <0.308.0> Feature flags: `stream_filtering` enabled
2024-03-19 09:45:41.019365+00:00 [notice] <0.308.0> Feature flags: attempt to enable `stream_sac_coordinator_unblock_group`...
2024-03-19 09:45:41.166764+00:00 [notice] <0.308.0> Feature flags: `stream_sac_coordinator_unblock_group` enabled
2024-03-19 09:45:41.167010+00:00 [notice] <0.308.0> Feature flags: attempt to enable `restart_streams`...
2024-03-19 09:45:41.330993+00:00 [notice] <0.308.0> Feature flags: `restart_streams` enabled
2024-03-19 09:45:41.331253+00:00 [notice] <0.308.0> Feature flags: attempt to enable `message_containers`...
2024-03-19 09:45:41.475973+00:00 [notice] <0.308.0> Feature flags: `message_containers` enabled
2024-03-19 09:45:41.476416+00:00 [info] <0.248.0> DB: virgin node -> run peer discovery
2024-03-19 09:45:41.489667+00:00 [notice] <0.44.0> Application mnesia exited with reason: stopped
2024-03-19 09:45:41.755479+00:00 [info] <0.248.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:45:41.755690+00:00 [info] <0.248.0> Successfully synced tables from a peer
2024-03-19 09:45:41.755883+00:00 [info] <0.248.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:45:41.756044+00:00 [info] <0.248.0> Successfully synced tables from a peer
2024-03-19 09:45:41.769758+00:00 [info] <0.248.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:45:41.770006+00:00 [info] <0.248.0> Successfully synced tables from a peer
2024-03-19 09:45:41.770360+00:00 [info] <0.248.0> Running boot step tracking_metadata_store defined by app rabbit
2024-03-19 09:45:41.770570+00:00 [info] <0.536.0> Setting up a table for connection tracking on this node: tracked_connection
2024-03-19 09:45:41.770678+00:00 [info] <0.536.0> Setting up a table for per-vhost connection counting on this node: tracked_connection_per_vhost
2024-03-19 09:45:41.770786+00:00 [info] <0.536.0> Setting up a table for per-user connection counting on this node: tracked_connection_per_user
2024-03-19 09:45:41.770924+00:00 [info] <0.536.0> Setting up a table for channel tracking on this node: tracked_channel
2024-03-19 09:45:41.771021+00:00 [info] <0.536.0> Setting up a table for channel tracking on this node: tracked_channel_per_user
2024-03-19 09:45:41.771164+00:00 [info] <0.248.0> Running boot step networking_metadata_store defined by app rabbit
2024-03-19 09:45:41.771320+00:00 [info] <0.248.0> Running boot step feature_flags defined by app rabbit
2024-03-19 09:45:41.771554+00:00 [info] <0.248.0> Running boot step codec_correctness_check defined by app rabbit
2024-03-19 09:45:41.771620+00:00 [info] <0.248.0> Running boot step external_infrastructure defined by app rabbit
2024-03-19 09:45:41.771682+00:00 [info] <0.248.0> Running boot step rabbit_event defined by app rabbit
2024-03-19 09:45:41.771851+00:00 [info] <0.248.0> Running boot step rabbit_registry defined by app rabbit
2024-03-19 09:45:41.771998+00:00 [info] <0.248.0> Running boot step rabbit_auth_mechanism_amqplain defined by app rabbit
2024-03-19 09:45:41.772107+00:00 [info] <0.248.0> Running boot step rabbit_auth_mechanism_cr_demo defined by app rabbit
2024-03-19 09:45:41.772296+00:00 [info] <0.248.0> Running boot step rabbit_auth_mechanism_plain defined by app rabbit
2024-03-19 09:45:41.772372+00:00 [info] <0.248.0> Running boot step rabbit_exchange_type_direct defined by app rabbit
2024-03-19 09:45:41.772445+00:00 [info] <0.248.0> Running boot step rabbit_exchange_type_fanout defined by app rabbit
2024-03-19 09:45:41.772512+00:00 [info] <0.248.0> Running boot step rabbit_exchange_type_headers defined by app rabbit
2024-03-19 09:45:41.772577+00:00 [info] <0.248.0> Running boot step rabbit_exchange_type_topic defined by app rabbit
2024-03-19 09:45:41.772643+00:00 [info] <0.248.0> Running boot step rabbit_mirror_queue_mode_all defined by app rabbit
2024-03-19 09:45:41.772710+00:00 [info] <0.248.0> Running boot step rabbit_mirror_queue_mode_exactly defined by app rabbit
2024-03-19 09:45:41.772781+00:00 [info] <0.248.0> Running boot step rabbit_mirror_queue_mode_nodes defined by app rabbit
2024-03-19 09:45:41.772858+00:00 [info] <0.248.0> Running boot step rabbit_priority_queue defined by app rabbit
2024-03-19 09:45:41.772931+00:00 [info] <0.248.0> Priority queues enabled, real BQ is rabbit_variable_queue
2024-03-19 09:45:41.773047+00:00 [info] <0.248.0> Running boot step rabbit_queue_location_client_local defined by app rabbit
2024-03-19 09:45:41.773155+00:00 [info] <0.248.0> Running boot step rabbit_queue_location_min_masters defined by app rabbit
2024-03-19 09:45:41.773297+00:00 [info] <0.248.0> Running boot step rabbit_queue_location_random defined by app rabbit
2024-03-19 09:45:41.773407+00:00 [info] <0.248.0> Running boot step kernel_ready defined by app rabbit
2024-03-19 09:45:41.773477+00:00 [info] <0.248.0> Running boot step rabbit_sysmon_minder defined by app rabbit
2024-03-19 09:45:41.773752+00:00 [info] <0.248.0> Running boot step rabbit_epmd_monitor defined by app rabbit
2024-03-19 09:45:41.774531+00:00 [info] <0.544.0> epmd monitor knows us, inter-node communication (distribution) port: 25672
2024-03-19 09:45:41.774807+00:00 [info] <0.248.0> Running boot step guid_generator defined by app rabbit
2024-03-19 09:45:41.778726+00:00 [info] <0.248.0> Running boot step rabbit_node_monitor defined by app rabbit
2024-03-19 09:45:41.779197+00:00 [info] <0.548.0> Starting rabbit_node_monitor (in ignore mode)
2024-03-19 09:45:41.779444+00:00 [info] <0.248.0> Running boot step delegate_sup defined by app rabbit
2024-03-19 09:45:41.780552+00:00 [info] <0.248.0> Running boot step rabbit_memory_monitor defined by app rabbit
2024-03-19 09:45:41.781751+00:00 [info] <0.248.0> Running boot step rabbit_fifo_dlx_sup defined by app rabbit
2024-03-19 09:45:41.781991+00:00 [info] <0.248.0> Running boot step core_initialized defined by app rabbit
2024-03-19 09:45:41.782060+00:00 [info] <0.248.0> Running boot step rabbit_channel_tracking_handler defined by app rabbit
2024-03-19 09:45:41.782198+00:00 [info] <0.248.0> Running boot step rabbit_connection_tracking_handler defined by app rabbit
2024-03-19 09:45:41.782300+00:00 [info] <0.248.0> Running boot step rabbit_definitions_hashing defined by app rabbit
2024-03-19 09:45:41.782420+00:00 [info] <0.248.0> Running boot step rabbit_exchange_parameters defined by app rabbit
2024-03-19 09:45:41.829531+00:00 [info] <0.248.0> Running boot step rabbit_mirror_queue_misc defined by app rabbit
2024-03-19 09:45:41.830528+00:00 [info] <0.248.0> Running boot step rabbit_policies defined by app rabbit
2024-03-19 09:45:41.831430+00:00 [info] <0.248.0> Running boot step rabbit_policy defined by app rabbit
2024-03-19 09:45:41.831800+00:00 [info] <0.248.0> Running boot step rabbit_queue_location_validator defined by app rabbit
2024-03-19 09:45:41.831979+00:00 [info] <0.248.0> Running boot step rabbit_quorum_memory_manager defined by app rabbit
2024-03-19 09:45:41.832137+00:00 [info] <0.248.0> Running boot step rabbit_quorum_queue defined by app rabbit
2024-03-19 09:45:41.833505+00:00 [info] <0.248.0> Running boot step rabbit_stream_coordinator defined by app rabbit
2024-03-19 09:45:41.833703+00:00 [info] <0.248.0> Running boot step rabbit_vhost_limit defined by app rabbit
2024-03-19 09:45:41.833816+00:00 [info] <0.248.0> Running boot step rabbit_mgmt_reset_handler defined by app rabbitmq_management
2024-03-19 09:45:41.833904+00:00 [info] <0.248.0> Running boot step rabbit_mgmt_db_handler defined by app rabbitmq_management_agent
2024-03-19 09:45:41.833979+00:00 [info] <0.248.0> Management plugin: using rates mode 'basic'
2024-03-19 09:45:41.834365+00:00 [info] <0.248.0> Running boot step recovery defined by app rabbit
2024-03-19 09:45:41.859843+00:00 [info] <0.248.0> Running boot step empty_db_check defined by app rabbit
2024-03-19 09:45:41.860012+00:00 [info] <0.248.0> Will seed default virtual host and user...
2024-03-19 09:45:41.860262+00:00 [info] <0.248.0> Adding vhost '/' (description: 'Default virtual host', tags: [])
2024-03-19 09:45:41.863838+00:00 [info] <0.248.0> Inserted a virtual host record {vhost,<<"/">>,[],
2024-03-19 09:45:41.863838+00:00 [info] <0.248.0>                                       #{description =>
2024-03-19 09:45:41.863838+00:00 [info] <0.248.0>                                             <<"Default virtual host">>,
2024-03-19 09:45:41.863838+00:00 [info] <0.248.0>                                         tags => []}}
2024-03-19 09:45:41.889255+00:00 [info] <0.595.0> Making sure data directory '/var/lib/rabbitmq/mnesia/rabbit@747398c0cd45/msg_stores/vhosts/628WB79CIFDYO9LJI6DKMI09L' for vhost '/' exists
2024-03-19 09:45:41.890622+00:00 [info] <0.595.0> Setting segment_entry_count for vhost '/' with 0 queues to '2048'
2024-03-19 09:45:41.907735+00:00 [info] <0.595.0> Starting message stores for vhost '/'
2024-03-19 09:45:41.921379+00:00 [info] <0.605.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_transient": using rabbit_msg_store_ets_index to provide index
2024-03-19 09:45:41.923603+00:00 [info] <0.595.0> Started message store of type transient for vhost '/'
2024-03-19 09:45:41.923934+00:00 [info] <0.609.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_persistent": using rabbit_msg_store_ets_index to provide index
2024-03-19 09:45:41.924690+00:00 [warning] <0.609.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_persistent": rebuilding indices from scratch
2024-03-19 09:45:41.926051+00:00 [info] <0.595.0> Started message store of type persistent for vhost '/'
2024-03-19 09:45:41.926332+00:00 [info] <0.595.0> Recovering 0 queues of type rabbit_classic_queue took 34ms
2024-03-19 09:45:41.926408+00:00 [info] <0.595.0> Recovering 0 queues of type rabbit_quorum_queue took 0ms
2024-03-19 09:45:41.926541+00:00 [info] <0.595.0> Recovering 0 queues of type rabbit_stream_queue took 0ms
2024-03-19 09:45:41.933365+00:00 [info] <0.248.0> Created user 'guest'
2024-03-19 09:45:41.935553+00:00 [info] <0.248.0> Successfully set user tags for user 'guest' to [administrator]
2024-03-19 09:45:41.939004+00:00 [info] <0.248.0> Successfully set permissions for user 'guest' in virtual host '/' to '.*', '.*', '.*'
2024-03-19 09:45:41.939183+00:00 [info] <0.248.0> Running boot step rabbit_observer_cli defined by app rabbit
2024-03-19 09:45:41.939421+00:00 [info] <0.248.0> Running boot step rabbit_looking_glass defined by app rabbit
2024-03-19 09:45:41.939532+00:00 [info] <0.248.0> Running boot step rabbit_core_metrics_gc defined by app rabbit
2024-03-19 09:45:41.939846+00:00 [info] <0.248.0> Running boot step background_gc defined by app rabbit
2024-03-19 09:45:41.940158+00:00 [info] <0.248.0> Running boot step routing_ready defined by app rabbit
2024-03-19 09:45:41.940237+00:00 [info] <0.248.0> Running boot step pre_flight defined by app rabbit
2024-03-19 09:45:41.940321+00:00 [info] <0.248.0> Running boot step notify_cluster defined by app rabbit
2024-03-19 09:45:41.940407+00:00 [info] <0.248.0> Running boot step networking defined by app rabbit
2024-03-19 09:45:41.940482+00:00 [info] <0.248.0> Running boot step rabbit_quorum_queue_periodic_membership_reconciliation defined by app rabbit
2024-03-19 09:45:41.940777+00:00 [info] <0.248.0> Running boot step definition_import_worker_pool defined by app rabbit
2024-03-19 09:45:41.940911+00:00 [info] <0.307.0> Starting worker pool 'definition_import_pool' with 4 processes in it
2024-03-19 09:45:41.941511+00:00 [info] <0.248.0> Running boot step cluster_name defined by app rabbit
2024-03-19 09:45:41.941663+00:00 [info] <0.248.0> Initialising internal cluster ID to 'rabbitmq-cluster-id-HIG9hxKvaqzBiW7IINWmmQ'
2024-03-19 09:45:41.943839+00:00 [info] <0.248.0> Running boot step direct_client defined by app rabbit
2024-03-19 09:45:41.944191+00:00 [info] <0.248.0> Running boot step rabbit_management_load_definitions defined by app rabbitmq_management
2024-03-19 09:45:41.944418+00:00 [info] <0.646.0> Resetting node maintenance status
2024-03-19 09:45:41.982635+00:00 [warning] <0.669.0> Deprecated features: `management_metrics_collection`: Feature `management_metrics_collection` is deprecated.
2024-03-19 09:45:41.982635+00:00 [warning] <0.669.0> By default, this feature can still be used for now.
2024-03-19 09:45:41.982635+00:00 [warning] <0.669.0> Its use will not be permitted by default in a future minor RabbitMQ version and the feature will be removed from a future major RabbitMQ version; actual versions to be determined.
2024-03-19 09:45:41.982635+00:00 [warning] <0.669.0> To continue using this feature when it is not permitted by default, set the following parameter in your configuration:
2024-03-19 09:45:41.982635+00:00 [warning] <0.669.0>     "deprecated_features.permit.management_metrics_collection = true"
2024-03-19 09:45:41.982635+00:00 [warning] <0.669.0> To test RabbitMQ as if the feature was removed, set this in your configuration:
2024-03-19 09:45:41.982635+00:00 [warning] <0.669.0>     "deprecated_features.permit.management_metrics_collection = false"
2024-03-19 09:45:45.568712+00:00 [info] <0.706.0> Management plugin: HTTP (non-TLS) listener started on port 15672
2024-03-19 09:45:45.568915+00:00 [info] <0.737.0> Statistics database started.
2024-03-19 09:45:45.569045+00:00 [info] <0.736.0> Starting worker pool 'management_worker_pool' with 3 processes in it
2024-03-19 09:45:45.583717+00:00 [info] <0.751.0> Prometheus metrics: HTTP (non-TLS) listener started on port 15692
2024-03-19 09:45:45.584078+00:00 [info] <0.646.0> Ready to start client connection listeners
2024-03-19 09:45:45.586862+00:00 [info] <0.795.0> started TCP listener on [::]:5672
 completed with 4 plugins.
2024-03-19 09:45:45.705574+00:00 [info] <0.646.0> Server startup complete; 4 plugins started.
2024-03-19 09:45:45.705574+00:00 [info] <0.646.0>  * rabbitmq_prometheus
2024-03-19 09:45:45.705574+00:00 [info] <0.646.0>  * rabbitmq_management
2024-03-19 09:45:45.705574+00:00 [info] <0.646.0>  * rabbitmq_management_agent
2024-03-19 09:45:45.705574+00:00 [info] <0.646.0>  * rabbitmq_web_dispatch
2024-03-19 09:45:45.781422+00:00 [info] <0.9.0> Time to start RabbitMQ: 10927389 us
2024-03-19 09:48:38.308595+00:00 [info] <0.823.0> accepting AMQP connection <0.823.0> (172.17.0.1:59162 -> 172.17.0.2:5672)
2024-03-19 09:48:38.308854+00:00 [error] <0.823.0> closing AMQP connection <0.823.0> (172.17.0.1:59162 -> 172.17.0.2:5672):
2024-03-19 09:48:38.308854+00:00 [error] <0.823.0> {bad_header,<<"GET / HT">>}
2024-03-19 09:48:39.419861+00:00 [info] <0.829.0> accepting AMQP connection <0.829.0> (172.17.0.1:59168 -> 172.17.0.2:5672)
2024-03-19 09:48:39.420155+00:00 [error] <0.829.0> closing AMQP connection <0.829.0> (172.17.0.1:59168 -> 172.17.0.2:5672):
2024-03-19 09:48:39.420155+00:00 [error] <0.829.0> {bad_header,<<"GET / HT">>}
2024-03-19 09:48:41.684235+00:00 [info] <0.835.0> accepting AMQP connection <0.835.0> (172.17.0.1:59178 -> 172.17.0.2:5672)
2024-03-19 09:48:41.684550+00:00 [error] <0.835.0> closing AMQP connection <0.835.0> (172.17.0.1:59178 -> 172.17.0.2:5672):
2024-03-19 09:48:41.684550+00:00 [error] <0.835.0> {bad_header,<<"GET / HT">>}
2024-03-19 09:48:46.722975+00:00 [info] <0.840.0> accepting AMQP connection <0.840.0> (172.17.0.1:50892 -> 172.17.0.2:5672)
2024-03-19 09:48:46.723297+00:00 [error] <0.840.0> closing AMQP connection <0.840.0> (172.17.0.1:50892 -> 172.17.0.2:5672):
2024-03-19 09:48:46.723297+00:00 [error] <0.840.0> {bad_header,<<"GET / HT">>}
2024-03-19 09:48:56.557978+00:00 [info] <0.893.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:48:56.558199+00:00 [info] <0.893.0> Successfully synced tables from a peer
2024-03-19 09:49:06.372296+00:00 [info] <0.915.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:49:06.372477+00:00 [info] <0.915.0> Successfully synced tables from a peer
2024-03-19 09:49:11.657353+00:00 [info] <0.927.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:49:11.657551+00:00 [info] <0.927.0> Successfully synced tables from a peer
2024-03-19 09:49:14.116430+00:00 [info] <0.939.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:49:14.116673+00:00 [info] <0.939.0> Successfully synced tables from a peer
2024-03-19 09:52:14.841383+00:00 [info] <0.1049.0> accepting AMQP connection <0.1049.0> (172.17.0.1:47170 -> 172.17.0.2:5672)
2024-03-19 09:52:14.844539+00:00 [info] <0.1049.0> connection <0.1049.0> (172.17.0.1:47170 -> 172.17.0.2:5672): user 'guest' authenticated and granted access to vhost '/'
2024-03-19 09:53:02.883333+00:00 [info] <0.1125.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:53:02.883522+00:00 [info] <0.1125.0> Successfully synced tables from a peer
2024-03-19 09:53:09.207122+00:00 [info] <0.1134.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:53:09.207384+00:00 [info] <0.1134.0> Successfully synced tables from a peer
2024-03-19 09:53:11.772807+00:00 [info] <0.1155.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:53:11.773082+00:00 [info] <0.1155.0> Successfully synced tables from a peer
2024-03-19 09:53:15.590319+00:00 [info] <0.1167.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:53:15.590508+00:00 [info] <0.1167.0> Successfully synced tables from a peer
2024-03-19 09:54:53.631608+00:00 [info] <0.1262.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:54:53.632210+00:00 [info] <0.1262.0> Successfully synced tables from a peer
2024-03-19 09:55:05.129112+00:00 [info] <0.1285.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:55:05.129526+00:00 [info] <0.1285.0> Successfully synced tables from a peer
2024-03-19 09:56:24.922686+00:00 [info] <0.1359.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:56:24.923188+00:00 [info] <0.1359.0> Successfully synced tables from a peer
2024-03-19 09:56:40.794009+00:00 [info] <0.1373.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 09:56:40.794221+00:00 [info] <0.1373.0> Successfully synced tables from a peer
2024-03-19 10:01:48.038374+00:00 [info] <0.1640.0> accepting AMQP connection <0.1640.0> (172.17.0.1:33492 -> 172.17.0.2:5672)
2024-03-19 10:01:48.043893+00:00 [info] <0.1640.0> connection <0.1640.0> (172.17.0.1:33492 -> 172.17.0.2:5672): user 'guest' authenticated and granted access to vhost '/'
2024-03-19 10:01:48.049113+00:00 [info] <0.1648.0> accepting AMQP connection <0.1648.0> (172.17.0.1:33504 -> 172.17.0.2:5672)
2024-03-19 10:01:48.051977+00:00 [info] <0.1648.0> connection <0.1648.0> (172.17.0.1:33504 -> 172.17.0.2:5672): user 'guest' authenticated and granted access to vhost '/'
2024-03-19 10:01:48.059100+00:00 [warning] <0.1655.0> Deprecated features: `transient_nonexcl_queues`: Feature `transient_nonexcl_queues` is deprecated.
2024-03-19 10:01:48.059100+00:00 [warning] <0.1655.0> By default, this feature can still be used for now.
2024-03-19 10:01:48.059100+00:00 [warning] <0.1655.0> Its use will not be permitted by default in a future minor RabbitMQ version and the feature will be removed from a future major RabbitMQ version; actual versions to be determined.
2024-03-19 10:01:48.059100+00:00 [warning] <0.1655.0> To continue using this feature when it is not permitted by default, set the following parameter in your configuration:
2024-03-19 10:01:48.059100+00:00 [warning] <0.1655.0>     "deprecated_features.permit.transient_nonexcl_queues = true"
2024-03-19 10:01:48.059100+00:00 [warning] <0.1655.0> To test RabbitMQ as if the feature was removed, set this in your configuration:
2024-03-19 10:01:48.059100+00:00 [warning] <0.1655.0>     "deprecated_features.permit.transient_nonexcl_queues = false"
2024-03-19 10:01:48.072201+00:00 [info] <0.1666.0> accepting AMQP connection <0.1666.0> (172.17.0.1:33506 -> 172.17.0.2:5672)
2024-03-19 10:01:48.077826+00:00 [info] <0.1666.0> connection <0.1666.0> (172.17.0.1:33506 -> 172.17.0.2:5672): user 'guest' authenticated and granted access to vhost '/'
2024-03-19 10:01:49.108006+00:00 [warning] <0.1655.0> Deprecated features: `global_qos`: Feature `global_qos` is deprecated.
2024-03-19 10:01:49.108006+00:00 [warning] <0.1655.0> By default, this feature can still be used for now.
2024-03-19 10:01:49.108006+00:00 [warning] <0.1655.0> Its use will not be permitted by default in a future minor RabbitMQ version and the feature will be removed from a future major RabbitMQ version; actual versions to be determined.
2024-03-19 10:01:49.108006+00:00 [warning] <0.1655.0> To continue using this feature when it is not permitted by default, set the following parameter in your configuration:
2024-03-19 10:01:49.108006+00:00 [warning] <0.1655.0>     "deprecated_features.permit.global_qos = true"
2024-03-19 10:01:49.108006+00:00 [warning] <0.1655.0> To test RabbitMQ as if the feature was removed, set this in your configuration:
2024-03-19 10:01:49.108006+00:00 [warning] <0.1655.0>     "deprecated_features.permit.global_qos = false"
2024-03-19 10:03:13.734070+00:00 [info] <0.1790.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:03:13.734325+00:00 [info] <0.1790.0> Successfully synced tables from a peer
2024-03-19 10:03:16.414937+00:00 [info] <0.1800.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:03:16.415144+00:00 [info] <0.1800.0> Successfully synced tables from a peer
2024-03-19 10:03:26.733892+00:00 [info] <0.1821.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:03:26.734088+00:00 [info] <0.1821.0> Successfully synced tables from a peer
2024-03-19 10:03:41.655879+00:00 [info] <0.1845.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:03:41.656069+00:00 [info] <0.1845.0> Successfully synced tables from a peer
2024-03-19 10:03:49.855912+00:00 [info] <0.1858.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:03:49.856357+00:00 [info] <0.1858.0> Successfully synced tables from a peer
2024-03-19 10:03:53.822583+00:00 [info] <0.1867.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:03:53.822769+00:00 [info] <0.1867.0> Successfully synced tables from a peer
2024-03-19 10:03:55.450962+00:00 [info] <0.1877.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:03:55.451161+00:00 [info] <0.1877.0> Successfully synced tables from a peer
2024-03-19 10:08:20.418025+00:00 [info] <0.2109.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:08:20.418209+00:00 [info] <0.2109.0> Successfully synced tables from a peer
2024-03-19 10:08:30.028931+00:00 [info] <0.2125.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:08:30.029144+00:00 [info] <0.2125.0> Successfully synced tables from a peer
2024-03-19 10:08:39.353094+00:00 [info] <0.2139.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:08:39.353279+00:00 [info] <0.2139.0> Successfully synced tables from a peer
2024-03-19 10:25:14.636554+00:00 [info] <0.2418.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:25:14.636801+00:00 [info] <0.2418.0> Successfully synced tables from a peer
2024-03-19 10:25:16.377381+00:00 [info] <0.2429.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:25:16.377608+00:00 [info] <0.2429.0> Successfully synced tables from a peer
2024-03-19 10:25:21.430716+00:00 [info] <0.2441.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:25:21.430915+00:00 [info] <0.2441.0> Successfully synced tables from a peer
2024-03-19 10:25:51.692931+00:00 [info] <0.2481.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:25:51.693128+00:00 [info] <0.2481.0> Successfully synced tables from a peer
2024-03-19 10:25:55.682438+00:00 [info] <0.2495.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:25:55.682669+00:00 [info] <0.2495.0> Successfully synced tables from a peer
2024-03-19 10:26:02.926564+00:00 [info] <0.2511.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:26:02.926767+00:00 [info] <0.2511.0> Successfully synced tables from a peer
2024-03-19 10:26:26.130182+00:00 [info] <0.2526.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:26:26.130391+00:00 [info] <0.2526.0> Successfully synced tables from a peer
2024-03-19 10:26:33.315043+00:00 [info] <0.2540.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:26:33.315231+00:00 [info] <0.2540.0> Successfully synced tables from a peer
2024-03-19 10:26:35.124633+00:00 [info] <0.2549.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:26:35.124813+00:00 [info] <0.2549.0> Successfully synced tables from a peer
2024-03-19 10:26:37.105077+00:00 [info] <0.2558.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:26:37.105267+00:00 [info] <0.2558.0> Successfully synced tables from a peer
2024-03-19 10:26:43.096472+00:00 [info] <0.2567.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:26:43.096667+00:00 [info] <0.2567.0> Successfully synced tables from a peer
2024-03-19 10:28:25.917126+00:00 [info] <0.2604.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:28:25.917704+00:00 [info] <0.2604.0> Successfully synced tables from a peer
2024-03-19 10:28:36.628635+00:00 [info] <0.2626.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:28:36.628852+00:00 [info] <0.2626.0> Successfully synced tables from a peer
2024-03-19 10:28:45.109597+00:00 [info] <0.2639.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:28:45.109829+00:00 [info] <0.2639.0> Successfully synced tables from a peer
2024-03-19 10:28:55.921069+00:00 [info] <0.2653.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:28:55.921300+00:00 [info] <0.2653.0> Successfully synced tables from a peer
2024-03-19 10:29:05.929510+00:00 [info] <0.2666.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:29:05.929734+00:00 [info] <0.2666.0> Successfully synced tables from a peer
2024-03-19 10:29:07.650264+00:00 [info] <0.2674.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:29:07.650497+00:00 [info] <0.2674.0> Successfully synced tables from a peer
2024-03-19 10:29:13.308937+00:00 [info] <0.2688.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:29:13.309167+00:00 [info] <0.2688.0> Successfully synced tables from a peer
2024-03-19 10:29:45.040399+00:00 [info] <0.2726.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:29:45.040585+00:00 [info] <0.2726.0> Successfully synced tables from a peer
2024-03-19 10:31:23.240528+00:00 [info] <0.2776.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:31:23.240800+00:00 [info] <0.2776.0> Successfully synced tables from a peer
2024-03-19 10:31:32.548052+00:00 [info] <0.2788.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:31:32.548305+00:00 [info] <0.2788.0> Successfully synced tables from a peer
2024-03-19 10:31:35.811705+00:00 [info] <0.2797.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-19 10:31:35.811907+00:00 [info] <0.2797.0> Successfully synced tables from a peer
```