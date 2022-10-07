To be updated
# Project Name
**0x0E. SQL - More queries**

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
Learn how to create a new MySQL user.
How to manage privileges for a user to a database or table.
What’s a `PRIMARY KEY`.
What’s a `FOREIGN KEY`.
How to use `NOT NULL` and `UNIQUE` constraints.
How to retrieve datas from multiple tables in one request.
What are subqueries.
What are `JOIN` and `UNION`.


## How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$ 
```


* **0. My privileges!** - Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`). - `0-privileges.sql`.
* **1. Root user** - Write a script that creates the MySQL server user `user_0d_1`. - `1-create_user.sql`.
* **2. Read user** - Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`. - `2-create_read_user.sql`.
---
* **3. Always a name** - Write a script that creates the table `force_name` on your MySQL server. - `3-force_name.sql`.
  ```
  guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
  Enter password: 
  guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
  Enter password: 
  guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
  Enter password: 
  id  name
  89  Best School
  guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
  Enter password: 
  ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
  guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
  Enter password: 
  id  name
  89  Best School
  guillaume@ubuntu:~/$ 
  ```
---
* **4. ID can't be null** - Write a script that creates the table `id_not_null` on your MySQL server. - `4-never_empty.sql`.
* **5. Unique ID** - Write a script that creates the table `unique_id` on your MySQL server. - `5-unique_id.sql`.
* **6. States table** - Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server. - `6-states.sql`.
* **7. Cities table** - Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server. - `7-cities.sql`.
---
* **8. Cities of California** - Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`. - `8-cities_of_california_subquery.sql`.
  ```
  guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
  Enter password: 
  id  name
  1   California
  2   Arizona
  3   Texas
  4   Utah
  guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
  Enter password: 
  id  state_id    name
  1   1   San Francisco
  2   1   San Jose
  4   2   Page
  6   3   Paris
  7   3   Houston
  8   3   Dallas
  guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
  Enter password: 
  id  name
  1   San Francisco
  2   San Jose
  guillaume@ubuntu:~/$ 
  ```
  ---
* **9. Cities by States** - Write a script that lists all cities contained in the database `hbtn_0d_usa`. - `9-cities_by_state_join.sql`.
---
* **10. Genre ID by show** - Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql). Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. - `10-genre_id_by_show.sql`.
  ```
  guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
  Enter password: 
  title   genre_id
  Breaking Bad    1
  Breaking Bad    6
  Breaking Bad    7
  Breaking Bad    8
  Dexter  1
  Dexter  2
  Dexter  6
  Dexter  7
  Dexter  8
  Game of Thrones 1
  Game of Thrones 3
  Game of Thrones 4
  House   1
  House   2
  New Girl    5
  Silicon Valley  5
  The Big Bang Theory 5
  The Last Man on Earth   1
  The Last Man on Earth   5
  guillaume@ubuntu:~/$ 
  ```
---
* **11. Genre ID for all shows** - Write a script that lists all shows contained in the database `hbtn_0d_tvshows`. - `11-genre_id_all_shows.sql`.
* **12. No genre** - Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked. - `12-no_genre.sql`.
* **13. Number of shows by genre** - Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each. Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`. - `13-count_shows_by_genre.sql`.
* **14. My genres** - Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`. - `14-my_genres.sql`.
* **15. Only Comedy** - Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`. - `15-comedy_only.sql`.
* **16. List shows and genres** - Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`. Each record should display: `tv_shows.title` - `tv_genres.name`. - `16-shows_by_genre.sql`.
* **17. Not my genre** - Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`. - `100-not_my_genres.sql`.
* **18. No Comedy tonight!** - Write a script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`. - `101-not_a_comedy.sql`.
* **19. Rotten tomatoes** - Import the database `hbtn_0d_tvshows_rate` dump to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql). Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating. - `102-rating_shows.sql`.
* **20. Best genre** - Write a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating. - `103-rating_genres.sql`.


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
