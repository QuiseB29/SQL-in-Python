from connect_mysql import connect_database
#connection to database
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        member_to_remove = (1, )
        
        query = "DELETE FROM workoutsessions WHERE id = %s"
        
        cursor.execute(query,member_to_remove)
        conn.commit()
        print("Customer removed successfully.")
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        cursor.close()
        cursor.close()