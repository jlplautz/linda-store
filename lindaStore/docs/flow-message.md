 ```python
 
 celery -A lindaStore worker --loglevel=inf
[2024-03-20 20:51:23,719: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'
 
 -------------- celery@ProBook-6470b v5.3.6 (emerald-rush)
--- ***** ----- 
-- ******* ---- Linux-5.4.0-173-generic-x86_64-with-glibc2.31 2024-03-20 20:51:23
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         lindaStore:0x7f20a16e1690
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . lindaStore.orders.tasks.order_created

[2024-03-20 20:51:23,958: WARNING/MainProcess] /home/plautz/Proj_2024/linda-store/.venv/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2024-03-20 20:51:23,964: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2024-03-20 20:51:23,966: WARNING/MainProcess] /home/plautz/Proj_2024/linda-store/.venv/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2024-03-20 20:51:23,972: INFO/MainProcess] mingle: searching for neighbors
[2024-03-20 20:51:23,985: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'
[2024-03-20 20:51:25,015: INFO/MainProcess] mingle: all alone
[2024-03-20 20:51:25,061: INFO/MainProcess] celery@ProBook-6470b ready.
[2024-03-20 20:51:28,129: INFO/MainProcess] Events of group {task} enabled by remote.
```

## browser -> http://localhost:8000/orders/create/
```python
Thank you
Your order has been successfully completed. Your order number is 24.
```

## Console terminal 
```python
[2024-03-20 21:04:14,130: INFO/MainProcess] Task lindaStore.orders.tasks.order_created[10b94959-0e3d-46ac-ad62-ed2fe427ea96] received
[2024-03-20 21:04:14,142: WARNING/ForkPoolWorker-2] Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Order nr. 24
From: admin@lindaStore.com
To: jorge.plautz@gmail.com
Date: Wed, 20 Mar 2024 21:04:14 -0000
Message-ID: <171096865414.19077.7818468100987584885@ProBook-6470b>

Dear Jorge Luiz,

You have successfully placed an order.Your order ID is 24.
[2024-03-20 21:04:14,142: WARNING/ForkPoolWorker-2] -------------------------------------------------------------------------------
[2024-03-20 21:04:14,142: INFO/ForkPoolWorker-2] Task lindaStore.orders.tasks.order_created[10b94959-0e3d-46ac-ad62-ed2fe427ea96] succeeded in 0.009326692999820807s: 1
```

## ***rabbitmq *******************************************************************************
```python
❯ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
2024-03-21 17:45:30.011549+00:00 [notice] <0.44.0> Application syslog exited with reason: stopped
2024-03-21 17:45:30.016417+00:00 [notice] <0.248.0> Logging: switching to configured handler(s); following messages may not be visible in this log output
2024-03-21 17:45:30.017266+00:00 [notice] <0.248.0> Logging: configured log handlers are now ACTIVE
2024-03-21 17:45:30.024595+00:00 [info] <0.248.0> ra: starting system quorum_queues
2024-03-21 17:45:30.024715+00:00 [info] <0.248.0> starting Ra system: quorum_queues in directory: /var/lib/rabbitmq/mnesia/rabbit@b8b1e8919a33/quorum/rabbit@b8b1e8919a33
2024-03-21 17:45:30.081017+00:00 [info] <0.262.0> ra system 'quorum_queues' running pre init for 0 registered servers
2024-03-21 17:45:30.089707+00:00 [info] <0.263.0> ra: meta data store initialised for system quorum_queues. 0 record(s) recovered
2024-03-21 17:45:30.104106+00:00 [notice] <0.268.0> WAL: ra_log_wal init, open tbls: ra_log_open_mem_tables, closed tbls: ra_log_closed_mem_tables
2024-03-21 17:45:30.119350+00:00 [info] <0.248.0> ra: starting system coordination
2024-03-21 17:45:30.119474+00:00 [info] <0.248.0> starting Ra system: coordination in directory: /var/lib/rabbitmq/mnesia/rabbit@b8b1e8919a33/coordination/rabbit@b8b1e8919a33
2024-03-21 17:45:30.121260+00:00 [info] <0.275.0> ra system 'coordination' running pre init for 0 registered servers
2024-03-21 17:45:30.122527+00:00 [info] <0.276.0> ra: meta data store initialised for system coordination. 0 record(s) recovered
2024-03-21 17:45:30.122861+00:00 [notice] <0.281.0> WAL: ra_coordination_log_wal init, open tbls: ra_coordination_log_open_mem_tables, closed tbls: ra_coordination_log_closed_mem_tables
2024-03-21 17:45:30.127664+00:00 [info] <0.248.0> ra: starting system coordination
2024-03-21 17:45:30.127750+00:00 [info] <0.248.0> starting Ra system: coordination in directory: /var/lib/rabbitmq/mnesia/rabbit@b8b1e8919a33/coordination/rabbit@b8b1e8919a33
2024-03-21 17:45:30.294478+00:00 [info] <0.248.0> Waiting for Khepri leader for 30000 ms, 9 retries left
2024-03-21 17:45:30.303830+00:00 [notice] <0.284.0> RabbitMQ metadata store: candidate -> leader in term: 1 machine version: 0
2024-03-21 17:45:30.310558+00:00 [info] <0.248.0> Khepri leader elected
2024-03-21 17:45:30.676236+00:00 [info] <0.248.0> 
2024-03-21 17:45:30.676236+00:00 [info] <0.248.0>  Starting RabbitMQ 3.13.0 on Erlang 26.2.2 [jit]
2024-03-21 17:45:30.676236+00:00 [info] <0.248.0>  Copyright (c) 2007-2024 Broadcom Inc and/or its subsidiaries
2024-03-21 17:45:30.676236+00:00 [info] <0.248.0>  Licensed under the MPL 2.0. Website: https://rabbitmq.com

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

  Starting broker...2024-03-21 17:45:30.677409+00:00 [info] <0.248.0> 
2024-03-21 17:45:30.677409+00:00 [info] <0.248.0>  node           : rabbit@b8b1e8919a33
2024-03-21 17:45:30.677409+00:00 [info] <0.248.0>  home dir       : /var/lib/rabbitmq
2024-03-21 17:45:30.677409+00:00 [info] <0.248.0>  config file(s) : /etc/rabbitmq/conf.d/10-defaults.conf
2024-03-21 17:45:30.677409+00:00 [info] <0.248.0>  cookie hash    : 9pHvHHQLyQ+HTK2ddNm9Vw==
2024-03-21 17:45:30.677409+00:00 [info] <0.248.0>  log(s)         : <stdout>
2024-03-21 17:45:30.677409+00:00 [info] <0.248.0>  data dir       : /var/lib/rabbitmq/mnesia/rabbit@b8b1e8919a33
2024-03-21 17:45:31.165487+00:00 [info] <0.248.0> Running boot step pre_boot defined by app rabbit
2024-03-21 17:45:31.165579+00:00 [info] <0.248.0> Running boot step rabbit_global_counters defined by app rabbit
2024-03-21 17:45:31.165960+00:00 [info] <0.248.0> Running boot step rabbit_osiris_metrics defined by app rabbit
2024-03-21 17:45:31.166122+00:00 [info] <0.248.0> Running boot step rabbit_core_metrics defined by app rabbit
2024-03-21 17:45:31.166721+00:00 [info] <0.248.0> Running boot step rabbit_alarm defined by app rabbit
2024-03-21 17:45:31.178592+00:00 [info] <0.321.0> Memory high watermark set to 4738 MiB (4968367718 bytes) of 11845 MiB (12420919296 bytes) total
2024-03-21 17:45:31.183248+00:00 [info] <0.323.0> Enabling free disk space monitoring (disk free space: 3244650496, total memory: 12420919296)
2024-03-21 17:45:31.183360+00:00 [info] <0.323.0> Disk free limit set to 50MB
2024-03-21 17:45:31.185826+00:00 [info] <0.248.0> Running boot step code_server_cache defined by app rabbit
2024-03-21 17:45:31.185996+00:00 [info] <0.248.0> Running boot step file_handle_cache defined by app rabbit
2024-03-21 17:45:31.194172+00:00 [info] <0.326.0> Limiting to approx 1048479 file handles (943629 sockets)
2024-03-21 17:45:31.194420+00:00 [info] <0.327.0> FHC read buffering: OFF
2024-03-21 17:45:31.194539+00:00 [info] <0.327.0> FHC write buffering: ON
2024-03-21 17:45:31.195347+00:00 [info] <0.248.0> Running boot step worker_pool defined by app rabbit
2024-03-21 17:45:31.195460+00:00 [info] <0.307.0> Will use 4 processes for default worker pool
2024-03-21 17:45:31.195539+00:00 [info] <0.307.0> Starting worker pool 'worker_pool' with 4 processes in it
2024-03-21 17:45:31.196266+00:00 [info] <0.248.0> Running boot step database defined by app rabbit
2024-03-21 17:45:31.196804+00:00 [info] <0.248.0> Peer discovery: configured backend: rabbit_peer_discovery_classic_config
2024-03-21 17:45:31.205627+00:00 [notice] <0.308.0> Feature flags: attempt to enable `detailed_queues_endpoint`...
2024-03-21 17:45:31.336166+00:00 [notice] <0.308.0> Feature flags: `detailed_queues_endpoint` enabled
2024-03-21 17:45:31.336506+00:00 [notice] <0.308.0> Feature flags: attempt to enable `stream_update_config_command`...
2024-03-21 17:45:31.465395+00:00 [notice] <0.308.0> Feature flags: `stream_update_config_command` enabled
2024-03-21 17:45:31.465569+00:00 [notice] <0.308.0> Feature flags: attempt to enable `stream_filtering`...
2024-03-21 17:45:31.581862+00:00 [notice] <0.308.0> Feature flags: `stream_filtering` enabled
2024-03-21 17:45:31.582124+00:00 [notice] <0.308.0> Feature flags: attempt to enable `stream_sac_coordinator_unblock_group`...
2024-03-21 17:45:31.715282+00:00 [notice] <0.308.0> Feature flags: `stream_sac_coordinator_unblock_group` enabled
2024-03-21 17:45:31.715607+00:00 [notice] <0.308.0> Feature flags: attempt to enable `restart_streams`...
2024-03-21 17:45:31.834809+00:00 [notice] <0.308.0> Feature flags: `restart_streams` enabled
2024-03-21 17:45:31.835078+00:00 [notice] <0.308.0> Feature flags: attempt to enable `message_containers`...
2024-03-21 17:45:31.953977+00:00 [notice] <0.308.0> Feature flags: `message_containers` enabled
2024-03-21 17:45:31.954285+00:00 [info] <0.248.0> DB: virgin node -> run peer discovery
2024-03-21 17:45:31.964179+00:00 [notice] <0.44.0> Application mnesia exited with reason: stopped
2024-03-21 17:45:32.213875+00:00 [info] <0.248.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-21 17:45:32.214074+00:00 [info] <0.248.0> Successfully synced tables from a peer
2024-03-21 17:45:32.214340+00:00 [info] <0.248.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-21 17:45:32.214670+00:00 [info] <0.248.0> Successfully synced tables from a peer
2024-03-21 17:45:32.234726+00:00 [info] <0.248.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-21 17:45:32.234964+00:00 [info] <0.248.0> Successfully synced tables from a peer
2024-03-21 17:45:32.235330+00:00 [info] <0.248.0> Running boot step tracking_metadata_store defined by app rabbit
2024-03-21 17:45:32.235586+00:00 [info] <0.536.0> Setting up a table for connection tracking on this node: tracked_connection
2024-03-21 17:45:32.235757+00:00 [info] <0.536.0> Setting up a table for per-vhost connection counting on this node: tracked_connection_per_vhost
2024-03-21 17:45:32.235986+00:00 [info] <0.536.0> Setting up a table for per-user connection counting on this node: tracked_connection_per_user
2024-03-21 17:45:32.236143+00:00 [info] <0.536.0> Setting up a table for channel tracking on this node: tracked_channel
2024-03-21 17:45:32.236243+00:00 [info] <0.536.0> Setting up a table for channel tracking on this node: tracked_channel_per_user
2024-03-21 17:45:32.236390+00:00 [info] <0.248.0> Running boot step networking_metadata_store defined by app rabbit
2024-03-21 17:45:32.236554+00:00 [info] <0.248.0> Running boot step feature_flags defined by app rabbit
2024-03-21 17:45:32.236798+00:00 [info] <0.248.0> Running boot step codec_correctness_check defined by app rabbit
2024-03-21 17:45:32.236875+00:00 [info] <0.248.0> Running boot step external_infrastructure defined by app rabbit
2024-03-21 17:45:32.236973+00:00 [info] <0.248.0> Running boot step rabbit_event defined by app rabbit
2024-03-21 17:45:32.237199+00:00 [info] <0.248.0> Running boot step rabbit_registry defined by app rabbit
2024-03-21 17:45:32.237379+00:00 [info] <0.248.0> Running boot step rabbit_auth_mechanism_amqplain defined by app rabbit
2024-03-21 17:45:32.237501+00:00 [info] <0.248.0> Running boot step rabbit_auth_mechanism_cr_demo defined by app rabbit
2024-03-21 17:45:32.237718+00:00 [info] <0.248.0> Running boot step rabbit_auth_mechanism_plain defined by app rabbit
2024-03-21 17:45:32.237828+00:00 [info] <0.248.0> Running boot step rabbit_exchange_type_direct defined by app rabbit
2024-03-21 17:45:32.237919+00:00 [info] <0.248.0> Running boot step rabbit_exchange_type_fanout defined by app rabbit
2024-03-21 17:45:32.238049+00:00 [info] <0.248.0> Running boot step rabbit_exchange_type_headers defined by app rabbit
2024-03-21 17:45:32.238168+00:00 [info] <0.248.0> Running boot step rabbit_exchange_type_topic defined by app rabbit
2024-03-21 17:45:32.238268+00:00 [info] <0.248.0> Running boot step rabbit_mirror_queue_mode_all defined by app rabbit
2024-03-21 17:45:32.238374+00:00 [info] <0.248.0> Running boot step rabbit_mirror_queue_mode_exactly defined by app rabbit
2024-03-21 17:45:32.238486+00:00 [info] <0.248.0> Running boot step rabbit_mirror_queue_mode_nodes defined by app rabbit
2024-03-21 17:45:32.238581+00:00 [info] <0.248.0> Running boot step rabbit_priority_queue defined by app rabbit
2024-03-21 17:45:32.238647+00:00 [info] <0.248.0> Priority queues enabled, real BQ is rabbit_variable_queue
2024-03-21 17:45:32.238767+00:00 [info] <0.248.0> Running boot step rabbit_queue_location_client_local defined by app rabbit
2024-03-21 17:45:32.238866+00:00 [info] <0.248.0> Running boot step rabbit_queue_location_min_masters defined by app rabbit
2024-03-21 17:45:32.238974+00:00 [info] <0.248.0> Running boot step rabbit_queue_location_random defined by app rabbit
2024-03-21 17:45:32.239080+00:00 [info] <0.248.0> Running boot step kernel_ready defined by app rabbit
2024-03-21 17:45:32.239142+00:00 [info] <0.248.0> Running boot step rabbit_sysmon_minder defined by app rabbit
2024-03-21 17:45:32.239383+00:00 [info] <0.248.0> Running boot step rabbit_epmd_monitor defined by app rabbit
2024-03-21 17:45:32.240283+00:00 [info] <0.544.0> epmd monitor knows us, inter-node communication (distribution) port: 25672
2024-03-21 17:45:32.240485+00:00 [info] <0.248.0> Running boot step guid_generator defined by app rabbit
2024-03-21 17:45:32.244328+00:00 [info] <0.248.0> Running boot step rabbit_node_monitor defined by app rabbit
2024-03-21 17:45:32.244774+00:00 [info] <0.548.0> Starting rabbit_node_monitor (in ignore mode)
2024-03-21 17:45:32.244998+00:00 [info] <0.248.0> Running boot step delegate_sup defined by app rabbit
2024-03-21 17:45:32.245973+00:00 [info] <0.248.0> Running boot step rabbit_memory_monitor defined by app rabbit
2024-03-21 17:45:32.246367+00:00 [info] <0.248.0> Running boot step rabbit_fifo_dlx_sup defined by app rabbit
2024-03-21 17:45:32.246522+00:00 [info] <0.248.0> Running boot step core_initialized defined by app rabbit
2024-03-21 17:45:32.246589+00:00 [info] <0.248.0> Running boot step rabbit_channel_tracking_handler defined by app rabbit
2024-03-21 17:45:32.246720+00:00 [info] <0.248.0> Running boot step rabbit_connection_tracking_handler defined by app rabbit
2024-03-21 17:45:32.246799+00:00 [info] <0.248.0> Running boot step rabbit_definitions_hashing defined by app rabbit
2024-03-21 17:45:32.246921+00:00 [info] <0.248.0> Running boot step rabbit_exchange_parameters defined by app rabbit
2024-03-21 17:45:32.278268+00:00 [info] <0.248.0> Running boot step rabbit_mirror_queue_misc defined by app rabbit
2024-03-21 17:45:32.278991+00:00 [info] <0.248.0> Running boot step rabbit_policies defined by app rabbit
2024-03-21 17:45:32.279543+00:00 [info] <0.248.0> Running boot step rabbit_policy defined by app rabbit
2024-03-21 17:45:32.279650+00:00 [info] <0.248.0> Running boot step rabbit_queue_location_validator defined by app rabbit
2024-03-21 17:45:32.279736+00:00 [info] <0.248.0> Running boot step rabbit_quorum_memory_manager defined by app rabbit
2024-03-21 17:45:32.279861+00:00 [info] <0.248.0> Running boot step rabbit_quorum_queue defined by app rabbit
2024-03-21 17:45:32.280746+00:00 [info] <0.248.0> Running boot step rabbit_stream_coordinator defined by app rabbit
2024-03-21 17:45:32.280965+00:00 [info] <0.248.0> Running boot step rabbit_vhost_limit defined by app rabbit
2024-03-21 17:45:32.281111+00:00 [info] <0.248.0> Running boot step rabbit_mgmt_reset_handler defined by app rabbitmq_management
2024-03-21 17:45:32.281214+00:00 [info] <0.248.0> Running boot step rabbit_mgmt_db_handler defined by app rabbitmq_management_agent
2024-03-21 17:45:32.281291+00:00 [info] <0.248.0> Management plugin: using rates mode 'basic'
2024-03-21 17:45:32.281766+00:00 [info] <0.248.0> Running boot step recovery defined by app rabbit
2024-03-21 17:45:32.298329+00:00 [info] <0.248.0> Running boot step empty_db_check defined by app rabbit
2024-03-21 17:45:32.298435+00:00 [info] <0.248.0> Will seed default virtual host and user...
2024-03-21 17:45:32.298625+00:00 [info] <0.248.0> Adding vhost '/' (description: 'Default virtual host', tags: [])
2024-03-21 17:45:32.302635+00:00 [info] <0.248.0> Inserted a virtual host record {vhost,<<"/">>,[],
2024-03-21 17:45:32.302635+00:00 [info] <0.248.0>                                       #{description =>
2024-03-21 17:45:32.302635+00:00 [info] <0.248.0>                                             <<"Default virtual host">>,
2024-03-21 17:45:32.302635+00:00 [info] <0.248.0>                                         tags => []}}
2024-03-21 17:45:32.320516+00:00 [info] <0.595.0> Making sure data directory '/var/lib/rabbitmq/mnesia/rabbit@b8b1e8919a33/msg_stores/vhosts/628WB79CIFDYO9LJI6DKMI09L' for vhost '/' exists
2024-03-21 17:45:32.322163+00:00 [info] <0.595.0> Setting segment_entry_count for vhost '/' with 0 queues to '2048'
2024-03-21 17:45:32.336437+00:00 [info] <0.595.0> Starting message stores for vhost '/'
2024-03-21 17:45:32.344564+00:00 [info] <0.605.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_transient": using rabbit_msg_store_ets_index to provide index
2024-03-21 17:45:32.346535+00:00 [info] <0.595.0> Started message store of type transient for vhost '/'
2024-03-21 17:45:32.346881+00:00 [info] <0.609.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_persistent": using rabbit_msg_store_ets_index to provide index
2024-03-21 17:45:32.347717+00:00 [warning] <0.609.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_persistent": rebuilding indices from scratch
2024-03-21 17:45:32.349018+00:00 [info] <0.595.0> Started message store of type persistent for vhost '/'
2024-03-21 17:45:32.349280+00:00 [info] <0.595.0> Recovering 0 queues of type rabbit_classic_queue took 26ms
2024-03-21 17:45:32.349376+00:00 [info] <0.595.0> Recovering 0 queues of type rabbit_quorum_queue took 0ms
2024-03-21 17:45:32.349471+00:00 [info] <0.595.0> Recovering 0 queues of type rabbit_stream_queue took 0ms
2024-03-21 17:45:32.355240+00:00 [info] <0.248.0> Created user 'guest'
2024-03-21 17:45:32.361156+00:00 [info] <0.248.0> Successfully set user tags for user 'guest' to [administrator]
2024-03-21 17:45:32.364127+00:00 [info] <0.248.0> Successfully set permissions for user 'guest' in virtual host '/' to '.*', '.*', '.*'
2024-03-21 17:45:32.364253+00:00 [info] <0.248.0> Running boot step rabbit_observer_cli defined by app rabbit
2024-03-21 17:45:32.364535+00:00 [info] <0.248.0> Running boot step rabbit_looking_glass defined by app rabbit
2024-03-21 17:45:32.364646+00:00 [info] <0.248.0> Running boot step rabbit_core_metrics_gc defined by app rabbit
2024-03-21 17:45:32.364938+00:00 [info] <0.248.0> Running boot step background_gc defined by app rabbit
2024-03-21 17:45:32.365288+00:00 [info] <0.248.0> Running boot step routing_ready defined by app rabbit
2024-03-21 17:45:32.365387+00:00 [info] <0.248.0> Running boot step pre_flight defined by app rabbit
2024-03-21 17:45:32.365476+00:00 [info] <0.248.0> Running boot step notify_cluster defined by app rabbit
2024-03-21 17:45:32.365566+00:00 [info] <0.248.0> Running boot step networking defined by app rabbit
2024-03-21 17:45:32.365659+00:00 [info] <0.248.0> Running boot step rabbit_quorum_queue_periodic_membership_reconciliation defined by app rabbit
2024-03-21 17:45:32.366090+00:00 [info] <0.248.0> Running boot step definition_import_worker_pool defined by app rabbit
2024-03-21 17:45:32.366176+00:00 [info] <0.307.0> Starting worker pool 'definition_import_pool' with 4 processes in it
2024-03-21 17:45:32.367078+00:00 [info] <0.248.0> Running boot step cluster_name defined by app rabbit
2024-03-21 17:45:32.367373+00:00 [info] <0.248.0> Initialising internal cluster ID to 'rabbitmq-cluster-id-SM56kHlMj91o-vCr9vlzgg'
2024-03-21 17:45:32.369275+00:00 [info] <0.248.0> Running boot step direct_client defined by app rabbit
2024-03-21 17:45:32.369486+00:00 [info] <0.248.0> Running boot step rabbit_management_load_definitions defined by app rabbitmq_management
2024-03-21 17:45:32.369637+00:00 [info] <0.646.0> Resetting node maintenance status
2024-03-21 17:45:32.391494+00:00 [warning] <0.669.0> Deprecated features: `management_metrics_collection`: Feature `management_metrics_collection` is deprecated.
2024-03-21 17:45:32.391494+00:00 [warning] <0.669.0> By default, this feature can still be used for now.
2024-03-21 17:45:32.391494+00:00 [warning] <0.669.0> Its use will not be permitted by default in a future minor RabbitMQ version and the feature will be removed from a future major RabbitMQ version; actual versions to be determined.
2024-03-21 17:45:32.391494+00:00 [warning] <0.669.0> To continue using this feature when it is not permitted by default, set the following parameter in your configuration:
2024-03-21 17:45:32.391494+00:00 [warning] <0.669.0>     "deprecated_features.permit.management_metrics_collection = true"
2024-03-21 17:45:32.391494+00:00 [warning] <0.669.0> To test RabbitMQ as if the feature was removed, set this in your configuration:
2024-03-21 17:45:32.391494+00:00 [warning] <0.669.0>     "deprecated_features.permit.management_metrics_collection = false"
2024-03-21 17:45:35.115587+00:00 [info] <0.706.0> Management plugin: HTTP (non-TLS) listener started on port 15672
2024-03-21 17:45:35.115807+00:00 [info] <0.737.0> Statistics database started.
2024-03-21 17:45:35.115971+00:00 [info] <0.736.0> Starting worker pool 'management_worker_pool' with 3 processes in it
2024-03-21 17:45:35.128576+00:00 [info] <0.751.0> Prometheus metrics: HTTP (non-TLS) listener started on port 15692
2024-03-21 17:45:35.128902+00:00 [info] <0.646.0> Ready to start client connection listeners
2024-03-21 17:45:35.130848+00:00 [info] <0.795.0> started TCP listener on [::]:5672
2024-03-21 17:45:35.230821+00:00 [info] <0.646.0> Server startup complete; 4 plugins started.
2024-03-21 17:45:35.230821+00:00 [info] <0.646.0>  * rabbitmq_prometheus
2024-03-21 17:45:35.230821+00:00 [info] <0.646.0>  * rabbitmq_management
2024-03-21 17:45:35.230821+00:00 [info] <0.646.0>  * rabbitmq_management_agent
2024-03-21 17:45:35.230821+00:00 [info] <0.646.0>  * rabbitmq_web_dispatch
 completed with 4 plugins.
2024-03-21 17:45:35.401288+00:00 [info] <0.9.0> Time to start RabbitMQ: 8850520 us
2024-03-21 17:45:37.931440+00:00 [info] <0.800.0> accepting AMQP connection <0.800.0> (172.17.0.1:46858 -> 172.17.0.2:5672)
2024-03-21 17:45:37.935482+00:00 [info] <0.800.0> connection <0.800.0> (172.17.0.1:46858 -> 172.17.0.2:5672): user 'guest' authenticated and granted access to vhost '/'
2024-03-21 17:45:37.939404+00:00 [info] <0.809.0> accepting AMQP connection <0.809.0> (172.17.0.1:46874 -> 172.17.0.2:5672)
2024-03-21 17:45:37.942223+00:00 [info] <0.809.0> connection <0.809.0> (172.17.0.1:46874 -> 172.17.0.2:5672): user 'guest' authenticated and granted access to vhost '/'
2024-03-21 17:45:37.947542+00:00 [warning] <0.816.0> Deprecated features: `transient_nonexcl_queues`: Feature `transient_nonexcl_queues` is deprecated.
2024-03-21 17:45:37.947542+00:00 [warning] <0.816.0> By default, this feature can still be used for now.
2024-03-21 17:45:37.947542+00:00 [warning] <0.816.0> Its use will not be permitted by default in a future minor RabbitMQ version and the feature will be removed from a future major RabbitMQ version; actual versions to be determined.
2024-03-21 17:45:37.947542+00:00 [warning] <0.816.0> To continue using this feature when it is not permitted by default, set the following parameter in your configuration:
2024-03-21 17:45:37.947542+00:00 [warning] <0.816.0>     "deprecated_features.permit.transient_nonexcl_queues = true"
2024-03-21 17:45:37.947542+00:00 [warning] <0.816.0> To test RabbitMQ as if the feature was removed, set this in your configuration:
2024-03-21 17:45:37.947542+00:00 [warning] <0.816.0>     "deprecated_features.permit.transient_nonexcl_queues = false"
2024-03-21 17:45:37.956740+00:00 [info] <0.827.0> accepting AMQP connection <0.827.0> (172.17.0.1:46888 -> 172.17.0.2:5672)
2024-03-21 17:45:37.959152+00:00 [info] <0.827.0> connection <0.827.0> (172.17.0.1:46888 -> 172.17.0.2:5672): user 'guest' authenticated and granted access to vhost '/'
2024-03-21 17:45:39.033717+00:00 [warning] <0.816.0> Deprecated features: `global_qos`: Feature `global_qos` is deprecated.
2024-03-21 17:45:39.033717+00:00 [warning] <0.816.0> By default, this feature can still be used for now.
2024-03-21 17:45:39.033717+00:00 [warning] <0.816.0> Its use will not be permitted by default in a future minor RabbitMQ version and the feature will be removed from a future major RabbitMQ version; actual versions to be determined.
2024-03-21 17:45:39.033717+00:00 [warning] <0.816.0> To continue using this feature when it is not permitted by default, set the following parameter in your configuration:
2024-03-21 17:45:39.033717+00:00 [warning] <0.816.0>     "deprecated_features.permit.global_qos = true"
2024-03-21 17:45:39.033717+00:00 [warning] <0.816.0> To test RabbitMQ as if the feature was removed, set this in your configuration:
2024-03-21 17:45:39.033717+00:00 [warning] <0.816.0>     "deprecated_features.permit.global_qos = false"
2024-03-21 17:47:03.727650+00:00 [info] <0.899.0> accepting AMQP connection <0.899.0> (172.17.0.1:46304 -> 172.17.0.2:5672)
2024-03-21 17:47:03.731344+00:00 [info] <0.899.0> connection <0.899.0> (172.17.0.1:46304 -> 172.17.0.2:5672): user 'guest' authenticated and granted access to vhost '/'
2024-03-21 17:49:34.593986+00:00 [info] <0.930.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-21 17:49:34.594132+00:00 [info] <0.930.0> Successfully synced tables from a peer
2024-03-21 17:49:36.944194+00:00 [info] <0.938.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
2024-03-21 17:49:36.944348+00:00 [info] <0.938.0> Successfully synced tables from a peer
```

## ***celery *******************************************************************************
```python
❯ celery -A lindaStore worker --loglevel=info
[2024-03-21 17:45:37,504: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'
 
 -------------- celery@ProBook-6470b v5.3.6 (emerald-rush)
--- ***** ----- 
-- ******* ---- Linux-5.4.0-173-generic-x86_64-with-glibc2.31 2024-03-21 17:45:37
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         lindaStore:0x7f35847b1650
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . lindaStore.orders.tasks.order_created

[2024-03-21 17:45:37,929: WARNING/MainProcess] /home/plautz/Proj_2024/linda-store/.venv/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2024-03-21 17:45:37,935: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2024-03-21 17:45:37,937: WARNING/MainProcess] /home/plautz/Proj_2024/linda-store/.venv/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2024-03-21 17:45:37,943: INFO/MainProcess] mingle: searching for neighbors
[2024-03-21 17:45:37,954: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'
[2024-03-21 17:45:39,026: INFO/MainProcess] mingle: all alone
[2024-03-21 17:45:39,075: INFO/MainProcess] celery@ProBook-6470b ready.
[2024-03-21 17:47:03,738: INFO/MainProcess] Task lindaStore.orders.tasks.order_created[b803c91f-2aff-4983-83d0-2d33d0c0d4a5] received
[2024-03-21 17:47:03,872: WARNING/ForkPoolWorker-2] Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Order nr. 28
From: admin@lindaStore.com
To: jorge.plautz@gmail.com
Date: Thu, 21 Mar 2024 17:47:03 -0000
Message-ID: <171104322386.34580.8516053885976465720@ProBook-6470b>

Dear Jorge Luiz,

You have successfully placed an order.Your order ID is 28.
[2024-03-21 17:47:03,873: WARNING/ForkPoolWorker-2] -------------------------------------------------------------------------------
[2024-03-21 17:47:03,875: INFO/ForkPoolWorker-2] Task lindaStore.orders.tasks.order_created[b803c91f-2aff-4983-83d0-2d33d0c0d4a5] succeeded in 0.13527400199745898s: 1
```
