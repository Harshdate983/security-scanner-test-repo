# Intentional scanner test finding: fake database password.
db_password = "fake-db-password-456"

# Normal database configuration; no actual database connection is made.
db_host = "localhost"
db_name = "test_database"
db_port = 5432
# Intentional scanner test finding: SQL Injection.

user_id = request.args.get("id")
query = "SELECT * FROM users WHERE id = " + user_id

# Intentional scanner test finding: SQL Injection using f-string.

query_fstring = f"SELECT * FROM users WHERE id = {user_id}"