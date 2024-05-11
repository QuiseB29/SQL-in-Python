from connect_mysql import connect_database

def list_distinct_trainers():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT DISTINCT name, trainer_id FROM members"

            cursor.execute(query)
            print("Displaying Trainers successfully.")

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

list_distinct_trainers()


        
    
    
    