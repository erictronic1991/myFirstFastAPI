# Standard library module for accessing environment variables
import os  # Used to read DATABASE_URL from the environment

# PostgreSQL driver for Python; provides low-level DB-API 2.0 interface
import psycopg2  # Enables connecting to and interacting with PostgreSQL

# Read the database connection string from environment; fall back to a sensible default for Docker Compose
DB_URL = os.getenv(
    "DATABASE_URL",  # Environment variable name expected to contain the connection string
    "postgresql://postgres:postgres@db:5432/postgres",  # Default URL used if env var is not set
)

# Create the table if it doesn't already exist; called during app startup

def init_db():  # Initialize the database schema
    conn = psycopg2.connect(DB_URL)  # Open a new database connection using the URL
    cur = conn.cursor()  # Create a cursor to execute SQL commands
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS queries (
            id SERIAL PRIMARY KEY,               -- Auto-incrementing integer ID
            question TEXT NOT NULL,             -- The question text submitted by the user
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Insert timestamp
        );
        """
    )  # Execute DDL to ensure the table exists
    conn.commit()  # Persist the schema change
    cur.close()  # Close the cursor to free resources
    conn.close()  # Close the connection to avoid leaks

# Insert a single question string into the queries table

def save_question(question):  # Persist a question row
    conn = psycopg2.connect(DB_URL)  # Open a new connection for this transaction
    cur = conn.cursor()  # Acquire a cursor for executing SQL
    cur.execute(
        "INSERT INTO queries (question) VALUES (%s);",  # Parameterized query prevents SQL injection
        (question,),  # Parameters are passed as a singleton tuple
    )  # Execute the INSERT statement
    conn.commit()  # Commit the transaction to save the row
    cur.close()  # Close the cursor
    conn.close()  # Close the connection
