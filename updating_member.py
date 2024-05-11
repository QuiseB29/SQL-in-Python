from connect_mysql import connect_database

def update_member_age(member_id, new_age):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Define the SQL query to update the age of a member
            query = 'UPDATE members SET age = %s WHERE id = %s'

            # Execute the query with the provided parameters
            cursor.execute(query, (new_age, member_id))
            conn.commit()
            print("Member age updated successfully.")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# Example usage:
# Update the age of member with ID 1 to 15
update_member_age(1, 34)
