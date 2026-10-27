# SQL vs NoSQL Decision Guide

## Abstract
Databases store and organize information for applications. SQL databases typically organize structured information into related tables. NoSQL is a family of models that includes document, key-value, graph, and other designs. This guide compares their strengths and trade-offs and provides a practical checklist for choosing a database. The sample data is fictional.

## 1. Relational databases
Relational databases store records in tables made of rows and columns. Primary keys identify rows, while foreign keys can connect related tables. SQL supports filtering, joining, grouping, and transactions. SQLite and PostgreSQL are examples. Relational databases are often a good starting point when relationships, constraints, and reliable multi-step updates are important.

## 2. Document databases
Document databases store records as documents, commonly using JSON-like structures. Documents can contain nested fields and arrays. They can suit product catalogs, user profiles, and content systems where records may have different attributes. MongoDB is an example. Flexible structure does not remove the need for validation and good data modeling.

## 3. Key-value databases
A key-value store maps a key to a value. It can be useful for caching, session data, and counters when the application retrieves values by key. Redis is a common example. It is not automatically a replacement for a relational database when joins and relational constraints are central.

## 4. Graph databases
Graph databases represent entities as nodes and relationships as edges. They can help with social networks, recommendation paths, fraud-link analysis, and dependency relationships where queries traverse connections. A graph database is not necessary for every dataset that contains relationships.

## 5. CAP theorem
The CAP theorem concerns distributed systems during a network partition. During such a partition, a system cannot guarantee both full consistency and full availability for every request. Consistency means reads follow the system's specified latest-write guarantees; availability means requests to non-failing nodes receive responses; partition tolerance concerns communication failures between nodes. Real products offer different architectures and consistency options, so it is inaccurate to label all SQL systems as one category and all NoSQL systems as another.

## 6. Comparison
| Feature | SQL / relational | NoSQL family |
|---|---|---|
| Data model | Tables and relationships | Documents, key-value, graphs, and others |
| Schema | Usually explicitly defined | Often flexible; depends on product |
| Relationships | Joins, keys, constraints | Embedded data, references, or graph links |
| Transactions | Mature support in many systems | Support and scope vary by product |
| Queries | SQL concepts, with product differences | Product-specific APIs and query languages |
| Typical fit | Related structured data and integrity rules | Workloads matching a particular non-relational model |
| Examples | SQLite, PostgreSQL | MongoDB, Redis, graph databases |

## 7. Example use cases
1. **E-commerce orders:** SQL is a sensible starting choice for customers, orders, order items, and payments because relationships and transactions matter.
2. **Chat messages:** A document or key-value model may fit message history and fast retrieval, depending on search, retention, and consistency needs. SQL can also work.
3. **Social connections:** A graph database may fit frequent friend-of-friend or relationship-traversal queries.
4. **Cache/session storage:** A key-value store can suit short-lived values retrieved by key.

These are starting recommendations, not universal rules. Traffic, query patterns, cost, and operational skills can change the decision.

## 8. Prototype overview
The repository includes a small SQLite prototype and a JSON document-style prototype using the same fictional products. Both filter products by category. The JSON program is a file-based demonstration, not a MongoDB deployment. Neither program is a performance benchmark or production system.

## 9. Selection checklist
- What entities and relationships exist?
- Are multi-record transactions and integrity constraints required?
- Which queries are most common?
- Is the data tabular, nested, key-value, or relationship-heavy?
- How frequently will fields change?
- Are joins, full-text search, geospatial queries, or graph traversal needed?
- What consistency guarantees are required?
- What are the expected read/write rates and data size?
- How will backups, recovery, monitoring, and security be handled?
- What are the hosting costs and team skills?
- Can the design be tested with representative fictional data?
- What evidence supports the decision, and what assumptions remain?

## 10. Responsible AI use
AI tools can help draft explanations, schemas, and tests, but they may produce fabricated citations, incorrect claims, insecure code, or outdated information. Verify claims using official documentation, run code, inspect output, and keep a record of prompts and corrections. Use fictional data and never paste passwords, API keys, or confidential information into AI tools. Do not claim a benchmark unless it was actually performed and documented.

## Conclusion
SQL and NoSQL models overlap but have different strengths. Choose based on data shape, query patterns, consistency needs, operational constraints, and cost—not popularity alone. For a small order system, SQLite or PostgreSQL is a reasonable starting point. A document database may fit flexible product attributes, while a key-value store may help with caching. Multiple database types should be combined only when there is a clear, tested reason.

## References
- PostgreSQL documentation: https://www.postgresql.org/docs/
- MongoDB documentation: https://www.mongodb.com/docs/
- Redis documentation: https://redis.io/docs/
- SQLite documentation: https://www.sqlite.org/docs.html

Before submitting, check the official pages and add exact page titles and access dates according to your college's citation format.
