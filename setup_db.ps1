$DB_NAME="myproject"
$PSQL="C:\Program Files\PostgreSQL\17\bin\psql.exe"

# Create database
& "$PSQL" -U postgres -c "CREATE DATABASE $DB_NAME;"

# Apply schema
& "$PSQL" -U postgres -d $DB_NAME -f schema.sql

# Seed data
& "$PSQL" -U postgres -d $DB_NAME -f seed.sql

Write-Output "Database setup complete."