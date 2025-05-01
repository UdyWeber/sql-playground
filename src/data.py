import sqlite3
import uuid
from dataclasses import dataclass
from datetime import date
from logging import info
from random import choice
from typing import Protocol

from constants import (
    DEPS,
    EMPLOYEE_TABLE_NAME,
    DEPARTMENT_TABLE_NAME,
    DEPENDENT_TABLE_NAME,
)

dep_ids: list[str] = []
random_names: list[str] = []


class Insertable(Protocol):
    def sql_insert_str(self) -> str: ...


class Creatable(Protocol):
    @classmethod
    def sql_create_table_str(cls) -> str: ...


@dataclass
class Employee(Insertable, Creatable):
    id: str
    name: str
    birth_date: date
    department_id: str

    @classmethod
    def new_fake(cls, department_id: str | None = None) -> "Employee":
        if department_id is None:
            department_id = random_dep_id()

        return cls(
            id=str(uuid.uuid4()),
            name=random_name(),
            birth_date=generate_random_birth_date(),
            department_id=department_id,
        )

    def sql_insert_str(self) -> str:
        return f"INSERT INTO {EMPLOYEE_TABLE_NAME} VALUES ('{self.id}', '{self.name}', '{str(self.birth_date)}', '{self.department_id}');"

    @classmethod
    def sql_create_table_str(cls) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {EMPLOYEE_TABLE_NAME} (
            id            TEXT PRIMARY KEY NOT NULL,
            name          TEXT NOT NULL,
            birth_date    TEXT NOT NULL,
            department_id TEXT NOT NULL,

            FOREIGN KEY (department_id) REFERENCES DEPARTMENT(id)
        );
        """


@dataclass
class Dependent(Insertable, Creatable):
    id: str
    name: str
    parent_id: str

    @classmethod
    def new_fake(cls, parent_id: str) -> "Dependent":
        return cls(id=str(uuid.uuid4()), name=random_name(), parent_id=parent_id)

    def sql_insert_str(self) -> str:
        return f"INSERT INTO {DEPENDENT_TABLE_NAME} VALUES ('{self.id}', '{self.name}', '{self.parent_id}');"

    @classmethod
    def sql_create_table_str(cls) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {DEPENDENT_TABLE_NAME} (
            id        TEXT PRIMARY KEY,
            name      TEXT NOT NULL,
            parent_id TEXT NOT NULL,

            FOREIGN KEY (parent_id) REFERENCES EMPLOYEE(id)
        );
        """


@dataclass
class Department(Insertable, Creatable):
    id: str
    name: str

    @classmethod
    def new_fake(cls, name: str) -> "Department":
        return cls(id=str(uuid.uuid4()), name=name)

    def sql_insert_str(self) -> str:
        return (
            f"INSERT INTO {DEPARTMENT_TABLE_NAME} VALUES ('{self.id}', '{self.name}');"
        )

    @classmethod
    def sql_create_table_str(cls) -> str:
        return f"""
        CREATE TABLE IF NOT EXISTS {DEPARTMENT_TABLE_NAME} (
            id   TEXT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL
        );
        """


def random_name() -> str:
    return choice(random_names)


def random_dep_id() -> str:
    return choice(dep_ids)


def generate_random_birth_date() -> date:
    day = choice(range(1, 29))
    month = choice(range(1, 13))
    year = choice(range(1970, 2010))
    return date(year, month, day)


def load_random_data() -> None:
    info("Loading data from data directory")

    info("Fetching fake names...")
    random_names.clear()

    with open("test-data/names.txt", "r") as file:
        name_bytes = file.readlines()
        random_names.extend([str(name.strip()) for name in name_bytes])


def generate_departments(cur: sqlite3.Cursor):
    dep_ids.clear()

    for d in DEPS:
        info(f"Generating {d} department object...")
        dep = Department.new_fake(d)

        insert_statement = dep.sql_insert_str()
        dep_ids.append(dep.id)

        cur.execute(insert_statement)


def generate_employees(cur: sqlite3.Cursor, n: int = 200) -> None:
    for i in range(n):
        info(f"Generating employee without dependents number {i+1}...")
        insert_statement = Employee.new_fake().sql_insert_str()
        cur.execute(insert_statement)


def generate_employees_with_dependents(cur: sqlite3.Cursor, n: int = 300) -> None:
    for i in range(n):
        info(f"Generating employee with dependents number {i+1}...")
        employee = Employee.new_fake()

        # Generate up to 3 dependents per employee
        child_num: int = choice(range(1, 4))
        dependents: list[Dependent] = [
            Dependent.new_fake(employee.id) for _ in range(child_num)
        ]

        cur.execute(employee.sql_insert_str())

        for dependent in dependents:
            info(f"Generating depedent for employee with id {employee.id}...")
            cur.execute(dependent.sql_insert_str())
