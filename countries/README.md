# Countries

## Purpose
Reading csv data and export sqlite database file.

## Useful SQLite commands

| command                                 | description                                               |
| --------------------------------------- | --------------------------------------------------------- |
| > sqlite3 -version                      | show version                                              |
| > sqlite3 country.db                    | switch to database country (create country.db if missing) |
| > sqlite3 country.db .dump > create.sql | export database content to sql-file                       |
| sqlite3> .read create.sql               | run create.sql file inside database                       |
| sqlite3> .quit                          | exit SQLite CLI                                           |