# quiz 39


## SQL diagram
![image](https://github.com/user-attachments/assets/7a2f6fff-7bce-4ed7-bb5d-8ca73cbe6c0d)



## code

            import sqlite3
            
            haiku = """Code flows like a stream
            Algorithms guide its way
            In silence, it solves"""
            
            database_name = "test_python39.db"
            
            con = sqlite3.connect(database_name)
            cursor = con.cursor()
            
            query_create_table = """
            CREATE TABLE IF NOT EXISTS words (
                id INTEGER PRIMARY KEY,
                length INTEGER,
                word TEXT UNIQUE NOT NULL
            )
            """
            cursor.execute(query_create_table)
            
            for word in haiku.split():
                cursor.execute("INSERT OR IGNORE INTO words (length, word) VALUES (?, ?)", (len(word), word))
            
            cursor.execute("SELECT AVG(length) FROM words")
            out = cursor.fetchone()
            
            con.commit()
            con.close()
            
            print("Average word length is", out)


## proof of work
![image](https://github.com/user-attachments/assets/50fbc9d2-b41a-404c-9bb8-a6d7f2fb3054)
