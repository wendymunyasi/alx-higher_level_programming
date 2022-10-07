# Project Name
**0x0D. SQL - Introduction**

## Author's Details
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel: *+254707240068.*

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be executed on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   All your files must be executable.
*	All your SQL queries should have a comment just before.
*	All your files should start by a comment describing the task.
*	All SQL keywords should be in uppercase (`SELECT`, `WHERE`…).
*   The length of your files will be tested using `wc`.

## Project Description
Learn what’s a database.
What’s a relational database.
What does SQL stand for.
What’s MySQL.
How to create a database in MySQL.
What does `DDL` and `DML` stand for.
How to `CREATE` or `ALTER` a table.
How to `SELECT` data from a table.
How to `INSERT`, `UPDATE` or `DELETE` data.
What are subqueries.
How to use MySQL functions.

Examples of how to run your files:
```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                  
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
```

The database name will be passed as an argument to the mysql command.
```
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$  
```


* **0. List databases** - Write a script that lists all databases of your MySQL server. - `0-list_databases.sql`.
* **1. Create a database** - Write a script that creates the database `hbtn_0c_0` in your MySQL server. - `1-create_database_if_missing.sql`.
* **2. Delete a database** - Write a script that deletes the database `hbtn_0c_0` in your MySQL server. - `2-remove_database.sql`.
* **3. List tables** - Write a script that lists all the tables of a database in your MySQL server. - `3-list_tables.sql`.
* **4. First table** - Write a script that creates a table called `first_table` in the current database in your MySQL server. - `4-first_table.sql`.
* **5. Full description** - Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server. - `5-full_table.sql`.
* **6. List all in table** - Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server. - `6-list_values.sql`.
* **7. First add** - Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server. - `7-insert_value.sql`.
* **8. Count 89** - Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server. - `8-count_89.sql`.
* **9. Full creation** - Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows. - `9-full_creation.sql`.
* **10. List by best** - Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server. - `10-top_score.sql`.
* **11. Select the best** - Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. - `11-best_score.sql`.
* **12. Cheating is bad** - Write a script that updates the score of Bob to `10` in the table `second_table`. - `12-no_cheating.sql`.
* **13. Score too low** - Write a script that lists all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. - `13-change_class.sql`.
* **14. Average** - Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. - `14-average.sql`.
* **15. Number by score** - Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server. - `15-groups.sql`.
* **16. Say my name** - Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server. - `16-no_link.sql`.
* **17. Go to UTF8** - Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server. - `100-move_to_utf8.sql`.
* **18. Temperatures #0** - Import in hbtn_0c_0 database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql). Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature. - `101-avg_temperatures.sql`.
* **19. Temperatures #1** - Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending). - `102-top_city.sql`.
* **20. Temperatures #2** - Write a script that displays the max temperature of each state (ordered by State name). - `103-max_state.sql`.


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
