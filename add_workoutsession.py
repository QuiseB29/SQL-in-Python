from connect_mysql import connect_database  # Assuming you have a module named connect_mysql with the connect_database function
conn = connect_database()  # Establish a connection to the MySQL database

if conn is not None:
    try:
        cursor = conn.cursor()  # Create a cursor object to execute SQL queries
        
        new_workoutsession = ("11", "2024-3-4", 9, 17)  # Define the parameters for the new workout session
        
        query = "INSERT INTO workoutsessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"  # Define the SQL query
        
        cursor.execute(query, new_workoutsession)  # Execute the query with the provided parameters
        conn.commit()  # Commit the transaction to apply changes to the database
        print("New Workout added successfully.")  # Print a success message
        
    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection
