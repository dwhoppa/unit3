# quiz 40

## ER diagram
![image](https://github.com/user-attachments/assets/4ff0ccde-c159-47b5-b5f7-e8552df9e8d1)

## code
          SELECT t.account_id,
                 c.first_name,
                 c.last_name,
                 a.account_type,
                 SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) -
                 SUM(CASE WHEN transaction_type = 'withdraw' THEN amount ELSE 0 END) AS net_deposit,
              a.balance
          FROM main.transactions t
          join main.accounts a on t.account_id = a.account_id
          join main.customers c on a.customer_id = c.customer_id
          GROUP BY t.account_id
          having net_deposit != a.balance;

## proof of work
![image](https://github.com/user-attachments/assets/44465d6c-fe4f-4db3-abfb-5f5de0c8a285)
