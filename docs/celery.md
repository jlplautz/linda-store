❯ celery -A lindaStore worker -l info
[2024-03-19 10:01:47,746: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'
 
 -------------- celery@ProBook-6470b v5.3.6 (emerald-rush)
--- ***** ----- 
-- ******* ---- Linux-5.4.0-173-generic-x86_64-with-glibc2.31 2024-03-19 10:01:47
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         lindaStore:0x7f09c3f7a7e0
- ** ---------- .> transport:   amqp://guest:**@localhost:5672//
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . lindaStore.orders.tasks.order_created

[2024-03-19 10:01:48,033: WARNING/MainProcess] /home/plautz/Proj_2024/linda-store/.venv/lib/python3.12/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2024-03-19 10:01:48,045: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2024-03-19 10:01:48,047: WARNING/MainProcess] /home/plautz/Proj_2024/linda-store/.venv/lib/python3.12/site-packages/celery/worker/consumer/consumer.py:507: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
whether broker connection retries are made during startup in Celery 6.0 and above.
If you wish to retain the existing behavior for retrying connections on startup,
you should set broker_connection_retry_on_startup to True.
  warnings.warn(

[2024-03-19 10:01:48,052: INFO/MainProcess] mingle: searching for neighbors
[2024-03-19 10:01:48,069: WARNING/MainProcess] No hostname was supplied. Reverting to default 'localhost'
[2024-03-19 10:01:49,098: INFO/MainProcess] mingle: all alone
[2024-03-19 10:01:49,144: INFO/MainProcess] celery@ProBook-6470b ready.
[2024-03-19 10:01:49,148: INFO/MainProcess] Task lindaStore.orders.tasks.order_created[7ee0cd3c-201f-44b9-ac21-c87aaface6e6] received
[2024-03-19 10:01:49,307: WARNING/ForkPoolWorker-2] Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Order nr. 7
From: jorge.plautz@gmail.com
To: jorge.plautz@gmail.com
Date: Tue, 19 Mar 2024 10:01:49 -0000
Message-ID: <171084250929.137507.7407062004180923554@ProBook-6470b>

Dear Jorge Luiz,

You have successfully placed an order.Your order id is 7.

[2024-03-19 10:01:49,307: WARNING/ForkPoolWorker-2] -------------------------------------------------------------------------------
[2024-03-19 10:01:49,307: INFO/ForkPoolWorker-2] Task lindaStore.orders.tasks.order_created[7ee0cd3c-201f-44b9-ac21-c87aaface6e6] succeeded in 0.056247990010888316s: 1
[2024-03-19 10:01:49,307: INFO/ForkPoolWorker-2] Task lindaStore.orders.tasks.order_created[7ee0cd3c-201f-44b9-ac21-c87aaface6e6] succeeded in 0.056247990010888316s: 1


[2024-03-19 11:53:03,593: INFO/MainProcess] Task lindaStore.orders.tasks.order_created[c7f2d2e6-b263-49f3-b4b4-f8a78ba89386] received
[2024-03-19 11:53:03,604: WARNING/ForkPoolWorker-2] Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Order nr. 8
From: jorge.plautz@gmail.com
To: jorge.plautz@gmail.com
Date: Tue, 19 Mar 2024 11:53:03 -0000
Message-ID: <171084918360.137507.13797405977097879142@ProBook-6470b>

Dear Jorge Luiz,

You have successfully placed an order.Your order id is 8.
[2024-03-19 11:53:03,613: WARNING/ForkPoolWorker-2] -------------------------------------------------------------------------------
[2024-03-19 11:53:03,615: INFO/ForkPoolWorker-2] Task lindaStore.orders.tasks.order_created[c7f2d2e6-b263-49f3-b4b4-f8a78ba89386] succeeded in 0.020212746007018723s: 1
