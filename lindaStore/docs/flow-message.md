 celery -A lindaStore worker --loglevel=info
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


## browser -> http://localhost:8000/orders/create/

Thank you
Your order has been successfully completed. Your order number is 24.


## Console terminal 

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
