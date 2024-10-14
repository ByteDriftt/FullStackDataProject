"""Script to manage users in a PostgreSQL database."""

import psycopg2
import random


def generate_unique_username(base_name):
    """Generate a unique username by appending a random number."""
    return f"{base_name}_{random.randint(1000, 9999)}"


def display_users(cursor):
    """Fetch and display all users from the database."""
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)


def insert_user(cursor, username, email):
    """Insert a new user into the database."""
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (%s, %s)",
        (username, email)
    )


# Establish connection to the database
conn = psycopg2.connect("dbname=myproject user=postgres password=eskisehir")
cur = conn.cursor()

# Display existing users
print("Existing users:")
display_users(cur)

# Try to insert a new user with a unique username
new_base_name = "new_user"
new_username = generate_unique_username(new_base_name)
new_email = f"{new_username}@example.com"

try:
    insert_user(cur, new_username, new_email)
    conn.commit()
    print(f"\nNew user {new_username} inserted successfully")
except psycopg2.errors.UniqueViolation:
    print("\nFailed to insert {new_username}. Trying again.")
    conn.rollback()  # Reset the failed transaction
    new_username = generate_unique_username(new_base_name)
    new_email = f"{new_username}@example.com"
    insert_user(cur, new_username, new_email)
    conn.commit()
    print(f"\nNew user {new_username} inserted successfully")

# Display updated user list
print("\nUpdated user list:")
display_users(cur)

# Close database connection
cur.close()
conn.close()
