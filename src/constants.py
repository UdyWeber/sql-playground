DEPS: list[str] = [
    "Finance",
    "Development",
    "E-commerce",
    "DevOps",
    "Customer Service",
    "Compliance",
    "Legal",
]

DEPARTMENT_TABLE_NAME = "DEPARTMENT"
EMPLOYEE_TABLE_NAME = "EMPLOYEE"
DEPENDENT_TABLE_NAME = "DEPENDENTS"

# NOTE: It's ordered regarding dependencies between the tables
ORDERED_DB_TABLE_NAMES: list[str] = [
    DEPENDENT_TABLE_NAME,
    EMPLOYEE_TABLE_NAME,
    DEPENDENT_TABLE_NAME,
]
