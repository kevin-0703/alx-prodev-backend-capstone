#!/usr/bin/python3

seed = __import__('seed')

# Step 1: Connect to MySQL server
connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print("connection successful")

    # Step 2: Connect to ALX_prodev database
    connection = seed.connect_to_prodev()

    if connection:
        # Step 3: Create user_data table
        seed.create_table(connection)

        # Step 4: Insert CSV data from remote S3 link
        csv_url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2024/12/3888260f107e3701e3cd81af49ef997cf70b6395.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20250907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250907T135230Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0ee6ef8e9c1c38d66c1cee25fad8e02cc3a3d80a6ba6ac4fdf520b5df759a723"
        seed.insert_data(connection, csv_url)

        # Step 5: Verify database exists
        cursor = connection.cursor()
        cursor.execute("""
            SELECT SCHEMA_NAME 
            FROM INFORMATION_SCHEMA.SCHEMATA 
            WHERE SCHEMA_NAME = 'ALX_prodev';
        """)
        result = cursor.fetchone()
        if result:
            print("Database ALX_prodev is present ")

        # Step 6: Preview first 5 rows
        cursor.execute("SELECT * FROM user_data LIMIT 5;")
        rows = cursor.fetchall()
        print(rows)

        cursor.close()
        connection.close()
