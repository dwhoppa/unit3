# quiz 42

## ER diagram
![image](https://github.com/user-attachments/assets/ad52c6df-2074-4790-9db9-ea6d65541e94)


## code
                from secure_password import check_hash
                from my_lib import DatabaseManager
                
                x = DatabaseManager('bitcoin_exchange.db')
                result=x.search("SELECT * from ledger")
                x.close()
                
                for row in result:
                    id, send_id, rece_id, amount, signature = row
                    string_hash = f"id {id},sender_id {send_id},receiver_id {rece_id},amount {amount}"
                    print(signature)
                    if check_hash(input_str=string_hash, hash=signature):
                        print("TX IS CORRECT")
                    else:
                        print("TX IS BAD")

## proof of work
![image](https://github.com/user-attachments/assets/eb8d7d41-38aa-4ad2-9beb-66c05be2fcd7)
