from connect_mysql import connect_database
# Establish a connection to the MySQL database
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()  # Create a cursor

        query = "SELECT COUNT(*) FROM Members"  # Define the SQL query to count members

        cursor.execute(query)  # Execute the query
        count = cursor.fetchone()[0]  # Fetch the count of members

        print(f"Total number of members: {count}")  # Print the count

    except Exception as e:  # Catch any exceptions
        print(f"Error: {e}")

    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection

