from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        new_member = ("Mary Jane", 45, "9887")
        
        query = "INSERT INTO Members (name,age,trainer_id) VALUES (%s, %s, %s)"
        
        cursor.execute(query,new_member)
        conn.commit()
        print("New customer added successfully.")
        
    finally:
        cursor.close()
        conn.close()