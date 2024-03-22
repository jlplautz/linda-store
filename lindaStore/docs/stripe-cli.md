## Comando para login
❯ ./stripe login --api-key sk_test_51Owb3gDVEbfTGILqJNzTEJGzJIxgraTRoUoYmQZFQrqOA2jcj6NzDnQ1wzBvnNsZUdk7O8AAtsmFq11JLMgjpXnO00OUpN8bFL
Your pairing code is: envy-wows-freed-polite
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit https://dashboard.stripe.com/stripecli/confirm_auth?t=ImG6O4rJnZn6U7gqZrlmQZ8OYGrEL1my (^C to quit)
> Done! The Stripe CLI is configured for LindaStore with account id acct_1Owb3gDVEbfTGILq

Please note: this key will expire after 90 days, at which point you'll need to re-authenticate.

## Comando para ver configuração
~ via 🐍 v3.11.0 
❯ ./stripe config  --list      
color = ''
project-name = 'default'
[default]
account_id = 'acct_1Owb3gDVEbfTGILq'
device_name = 'ProBook-6470b'
display_name = 'LindaStore'
live_mode_api_key = 'rk_live_***********************************************************************************************iho4'
live_mode_key_expires_at = '2024-06-19'
live_mode_pub_key = 'pk_live_51Owb3gDVEbfTGILq0KeCtu8ou9bIwLv8HZq8xu6boX8mUkDrclYJmb7b730tC7db09hvLbB6Zo1CDnHm1Q1Xjas800uKRdoZJm'
test_mode_api_key = 'rk_test_51Owb3gDVEbfTGILqDwYHZftjEroDi4AUTJ4X19iMPxHQSFszIgJQJ9mLzZfaC5uKbn5uxoRupvBxB2ZT3RVj6GAH00ZuzRJqq6'
test_mode_key_expires_at = '2024-06-19'
test_mode_pub_key = 'pk_test_51Owb3gDVEbfTGILq5eUm289abIzLZcDUOiBkqauyFLwspa3fdUf4DQ3tqyVqpVWkqnY4xOG1lfxG7BxGMGkkOwgt002Lbodc5U'

password = Lingara.1

## Comando para ver escutar os webhooks
~ via 🐍 v3.11.0 
❯ ./stripe listen --forward-to localhost:8000/payment/webhook/
> Ready! You are using Stripe API Version [2023-10-16]. Your webhook signing secret is whsec_b652f632241a73754eaa31ee4c73bc0128ad58ccae770c52354c701ef201026c (^C to quit)

2024-03-21 17:15:40   --> charge.succeeded [evt_3Ows1WDVEbfTGILq0kWqSzYa]
2024-03-21 17:15:40  <--  [200] POST http://localhost:8000/payment/webhook/ [evt_3Ows1WDVEbfTGILq0kWqSzYa]
2024-03-21 17:15:40   --> payment_intent.succeeded [evt_3Ows1WDVEbfTGILq08KIuW03]
2024-03-21 17:15:40  <--  [200] POST http://localhost:8000/payment/webhook/ [evt_3Ows1WDVEbfTGILq08KIuW03]
2024-03-21 17:15:40   --> payment_intent.created [evt_3Ows1WDVEbfTGILq0mJcqPOj]
2024-03-21 17:15:40  <--  [200] POST http://localhost:8000/payment/webhook/ [evt_3Ows1WDVEbfTGILq0mJcqPOj]
2024-03-21 17:15:49   --> checkout.session.completed [evt_1Ows1hDVEbfTGILqOb0JUcs3]
2024-03-21 17:15:49  <--  [500] POST http://localhost:8000/payment/webhook/ [evt_1Ows1hDVEbfTGILqOb0JUcs3]

