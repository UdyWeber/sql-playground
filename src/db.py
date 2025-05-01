import sqlite3

from logging import info

from constants import ORDERED_DB_TABLE_NAMES
from data import (
    generate_departments,
    generate_employees,
    generate_employees_with_dependents,
    load_random_data,
    Department,
    Employee,
    Dependent,
)


def aquire_connection() -> sqlite3.Connection:
    return sqlite3.connect("test.db")


def clean_db(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()

    info("Cleaning last database footprint...")
    for t in ORDERED_DB_TABLE_NAMES:
        cur.execute(f"DROP TABLE IF EXISTS {t}")

    conn.commit()
    cur.close()


def create_default_tables(conn: sqlite3.Connection) -> None:
    info("Creating the database default tables...")

    cur = conn.cursor()

    # NOTE: Has to execute the pragma to enable foreign key syntax in SQLite3
    cur.execute("PRAGMA foreign_keys = ON;")

    info("Creating the department table...")
    cur.execute(Department.sql_create_table_str())

    info("Creating the employee table...")
    cur.execute(Employee.sql_create_table_str())

    info("Creating the dependents table...")
    cur.execute(Dependent.sql_create_table_str())

    # NOTE: Query all database object
    res = cur.execute("SELECT name FROM sqlite_master;")
    info(f"Default dabase object where created for database {res.fetchall()}")

    conn.commit()
    cur.close()


def generate_seed_data(conn: sqlite3.Connection):
    info("Generating seed data into the database...")
    cur = conn.cursor()

    load_random_data()

    generate_departments(cur)
    conn.commit()

    generate_employees(cur)
    conn.commit()

    generate_employees_with_dependents(cur)
    conn.commit()

    cur.close()
