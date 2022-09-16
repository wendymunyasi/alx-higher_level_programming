# Object-relational mapping
Project done during **Full Stack Software Engineering studies** at **ALX**. It aims to learn about how to connect to a MySQL database from a Python script, what ORM means and how to map a Python Class to a MySQL table.

## Technologies
* `MySQL 8`.
* `MySQLdb`, version 2.0.x.
* `sqlalchemy`, version 1.4.x.
* Python Scripts are written with Python 3.8.
* Tested on Ubuntu 20.04 LTS.

## Task 1 Example

```
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```

## Files

All the following files are scripts of MySQL:

| Filename | Description |
| -------- | ----------- |
| `0-privileges.py` | Lists all `states` from the database `hbtn_0e_0_usa` |
| `1-filter_states.py` | Lists all `states` with a `name` starting with `N` from the database `hbtn_0e_0_usa` |
| `2-my_filter_states.py` | Takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument |
| `3-my_safe_filter_states.py` | Takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument without injection |
| `4-cities_by_state.py` | Lists all `cities` from the database `hbtn_0e_4_usa` |
| `5-filter_cities.py` | Takes in the name of a state as an argument and lists all `cities` of that state |
| `model_state.py` | Contains the class definition of a `State` and an instance `Base = declarative_base()` |
| `7-model_state_fetch_all.py` | Lists all `State` objects from the database `hbtn_0e_6_usa` |
| `8-model_state_fetch_first.py` | Prints the first `State` object from the database `hbtn_0e_6_usa` |
| `9-model_state_filter_a.py` | Lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa` |
| `10-model_state_my_get.py` | Prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa` |
| `11-model_state_insert.py` | Adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa` |
| `12-model_state_update_id_2.py` | Script that changes the name of a `State` object from the database `hbtn_0e_6_usa` |
| `13-model_state_delete_a.py` | Script that deletes all `State` objects with the name containing the letter `a` from the database `hbtn_0e_6_usa` |
| `model_city.py` | Contains the class definition of a `City`, which inherits from `Base` |
| `14-model_city_fetch_by_state.py` | Prints all `City` objects from the database `hbtn_0e_14_usa` |
| `relationship_city.py` | Same as `model_city.py` |
| `relationship_state.py` | Contains the class definition of a `State` with a relationship with the class `City` |
| `100-relationship_states_cities.py` | Creates the `State` "California" with the `City` "San Francisco" from the database `hbtn_0e_100_usa` |
| `101-relationship_states_cities_list.py` | Lists all `State` objects and corresponding `City` objects, contained in the database `hbtn_0e_101_usa` |
| `102-relationship_cities_states_list.py` | Lists all `City` objects from the database `hbtn_0e_101_usa` |

## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.
