# SQL vs NoSQL Decision Guide

A beginner-friendly CSE capstone project comparing relational SQL databases with NoSQL data models.

## Project goals
- Explain relational, document, key-value, and graph databases.
- Summarize CAP theorem and common trade-offs.
- Compare database choices for practical use cases.
- Demonstrate the same fictional product data using SQLite and JSON documents.
- Provide a database selection checklist and quiz.
- Encourage verification of AI-generated claims using official documentation.

## Repository structure
```text
SQL_vs_NoSQL_Decision_Guide/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── src/
│   ├── sqlite_prototype.py
│   └── document_store_prototype.py
├── docs/
│   ├── decision_guide.md
│   ├── database_selection_checklist.md
│   ├── quiz_answer_key.md
│   └── prompt_library_verification.md
└── tests/
    └── test_prototypes.py
```

## Requirements
- Python 3.9 or newer
- SQLite is included with Python's standard library
- No third-party Python packages are required

## Run the prototypes
Open a terminal in the repository folder and run:

```bash
python src/sqlite_prototype.py
python src/document_store_prototype.py
```

The SQLite program creates `shop.db` in the current working directory. The document example writes `products.json`.

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Sample output
SQLite prototype:
```text
Stationery products:
('Notebook', 45.0)
('Pen', 10.0)
```

JSON document prototype:
```text
Stationery products:
Notebook 45.0
Pen 10.0
```

## Important limitations
- The JSON example is a tiny document-style demonstration, not a MongoDB server.
- These examples are educational prototypes, not production systems.
- No performance benchmark is claimed.
- Add screenshots from your own test run and verify sources before college submission.

## Official documentation
- PostgreSQL: https://www.postgresql.org/docs/
- MongoDB: https://www.mongodb.com/docs/
- Redis: https://redis.io/docs/
- SQLite: https://www.sqlite.org/docs.html

## Suggested GitHub upload steps
1. Sign in to GitHub and create a new repository.
2. Give it a name such as `SQL-vs-NoSQL-Decision-Guide`.
3. Extract this ZIP file on your computer.
4. Upload the files/folders to the new repository, or use Git commands.
5. Add your own name, college details, screenshots, and verified references before submitting.
