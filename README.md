# SQL Playground
As a beginner is hard to get started using SQL, because there is a lot of things you have to understand before using SQL itself, which can be frustrating and demotivating. So I've decided to create a simple playground using Python, to help those which are starting :D

## Tools you'll need
I'll assume that you're able to install those yourself, so I'll just leave the links. If help is needed I'm very sure you'll find resources on YouTube!

- Database manager: [Intelijj professional](https://www.jetbrains.com/idea/) / [DBeaver](https://dbeaver.io/) / [Dadbod.nvim](https://github.com/tpope/vim-dadbod) 
- [Python](https://www.python.org/)
- [SQLite](https://www.sqlite.org/)

## How the playground is built?
The playground is build with Python using no dependencies for easier usage between environments, and SQLite3 as the database, that gets the job done. In the future I might add some `PostgreSQL` to it but I will require me to add dependencies, so will be sticking with the basics for now.

## Database Tables
Database tables are: `Employee`, `Dependents`, `Department`. Those are the most basic examples you'll probably find on the internet, you can give the schema of the database for Chatgpt, and it can generate useful exercises.

## Python
Python version must be 3.13.0 or greater.

## Docker
No docker for now buddy, beginners haven't learned about containers yet, might add it later btw.

## How to run
It must as simple as typing the command bellow (assuming you are on the root of the directory), that should trigger the database creation + initial dataload. A `test.db` will be created at the root of the project, that will be your database.

```
python src/main.py
```

## Common Questions
As a beginner I expect you to have a lot of questions, some about the setup of the project, some are the commons that I'd think of if I was in your position

- How do I connect my database manager of choice to my SQLite DB?
- How to format a SQLite connection string.
- What is a database manager.
- How to install different versions of Python (Use Pyenv)

Those are simple questions to ask to a LLM, I'm sure you're capable of finding out yourself! But don't be bother to ask for help if really needed!
