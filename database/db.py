import sqlite3

DB_NAME = "jobs.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            url TEXT
        )
    """)

    conn.commit()
    conn.close()
# insert into the database
def save_job(title, company, location, url):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO jobs(title, company, location, url)
        VALUES (?, ?, ?, ?)
        """,
        (title, company, location, url)
    )

    conn.commit()
    conn.close()

    return "Job saved successfully."

# retrieve jobs from the database
def get_jobs():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs")

    jobs = cursor.fetchall()

    conn.close()

    return jobs




# Create table automatically
init_db()