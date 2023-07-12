import mysql.connector

try:
    # open the database connection
    mydb = mysql.connector.connect(
        user='root',
        password='?!?!?!?!?',
        host='localhost',
        database='SKToolInventory2'
    )
    print("Database connection successful")

    # perform a count statement on the tools table
    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) FROM tools")
    count = cursor.fetchone()[0]
    print("Number of rows in the tools table:", count)

    # create a new temporary table for the violating tools
    temp_table_query = """
        CREATE TEMPORARY TABLE violating_tools
        SELECT *
        FROM tools
        WHERE power_type != 'Battery' AND tool_name LIKE '%Cordless%'
    """
    cursor.execute(temp_table_query)

    select_query = """
        SELECT *
        FROM violating_tools
        LIMIT 10
    """

    cursor.execute(select_query)
    results = cursor.fetchall()
    print("First 10 rows of violating_tools:")
    for row in results:
        print(row)

    # delete the violating tools from the tools table
    delete_query = """
        DELETE FROM tools
        WHERE power_type != 'Battery' AND tool_name LIKE '%Cordless%'
    """

    # execute the delete query
    cursor.execute(delete_query)
    mydb.commit()
    print("Deletion completed successfully")

    # perform the select statement on the tools table to show the updated state
    cursor.execute("""
        SELECT *
        FROM tools
        WHERE power_type != 'Battery' AND tool_name LIKE '%Cordless%'
    """)
    results_after = cursor.fetchall()
    print("Tools after deletions:")
    for row in results_after:
        print(row)

    # perform a Count statement on the tools table again
    cursor.execute("SELECT COUNT(*) FROM tools")
    count = cursor.fetchone()[0]
    print("Number of rows in the tools table after deletions:", count)

    cursor.close()

except mysql.connector.Error as err:
    print("Error connecting to the database:", err)

finally:
    # close the database connection
    if mydb.is_connected():
        mydb.close()
        print("Database connection closed")

