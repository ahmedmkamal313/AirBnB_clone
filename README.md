# AirBnB clone 🛩️
[![Paython: 3.8.10](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://en.wikipedia.org/wiki/Python_(programming_language))

## Introduction 🚀

Welcome to the AirBnB clone project! This is the first step towards building a full web application: **the AirBnB clone.**
This project is a part of ALX Software Engineering Program. 🌍

![airBnB](https://camo.githubusercontent.com/59589bd21e8ec09ef94f2d9bb80d36d144bc487fe4737f8b213d005f3273921b/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)

## Authors 👥
This project was created by:
- [Majda Bouzayd](https://github.com/Magdalina1)
- [Ahmed Kamal](https://github.com/ahmedmkamal313)

## First Step: The Console 💻 (0x00. AirBnB clone - The console 🛩️)

- The first part of this project is to write a **command interpreter** (also called a console) to manage the AirBnB objects.
- The console will allow to create, update, delete, and manipulate different types of objects, such as users, states, cities, places, etc.
- The console will also allow to store and retrieve these objects from a file using **JSON** serialization and deserialization.

![planning](https://user-images.githubusercontent.com/93772775/183030202-7fe98cea-20a5-4da6-9023-018752bdc405.png)

## Installation ⏬

To use this project, you need to clone this repository:
```
git clone https://github.com/ahmedmkamal313/AirBnB_clone.git
```
Then, change directory to the `AirBnB_clone` directory and run the console script:
```
cd AirBnB_clone
./console.py
```
## Usage 📝
The console works in interactive mode and non-interactive mode.

### Interactive Mode
In interactive mode, you can type commands and see the results. To enter interactive mode, run the console script without any arguments:
```
./console.py
```
You will see a prompt `(hbnb)` where you can type commands. To exit interactive mode, type `EOF` or press `Ctrl-D`.
Example:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2023, 8, 13, 18, 13, 20, 268301), 'updated_at': datetime.datetime(2023, 8, 13, 18, 13, 20, 268301)}
(hbnb) update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Barack"
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2023, 8, 13, 18, 13, 20, 268301), 'updated_at': datetime.datetime(2023, 8, 13, 18, 13, 20, 268301), 'first_name': 'Barack'}
(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) EOF
$
```
### Non-Interactive Mode
In non-interactive mode, you can run commands from an input source, such as a file or a pipe. To enter non-interactive mode, run the console script with the input source as an argument:
```
echo "<command>" | ./console.py
```
or
```
./console.py < <file>
```
Example:
```
$ echo "create User" | ./console.py
(hbnb) 49faff9a-6318-451f-87b6-910505c55907
$
```
## Commands 📋
| Command |	Syntax | Description |
| ---     |  ---   |         --- |
|help	|help [command]	|Shows a list of available commands or the help for a specific command |
|quit	|quit	|Exits the console |
|EOF	|EOF	|Exits the console |
|create	|create <class> |	Creates a new instance of a given class and prints its id |
|show	|show <class> <id> | Prints the string representation of an instance based on its class and id |
|destroy	| destroy <class> <id>	| Deletes an instance based on its class and id |
|all	 |all [class]	| Prints the string representation of all instances or all instances of a given class |
|update	| update <class> <id> <attribute> "<value>" | Updates an instance based on its class and id by adding or updating an attribute |
|count | count <class>	|Prints the number of instances of a given class|

The console also supports the following alternative syntax for some commands:
| Command	 | Syntax	| Description |
| ---      |  ---   |         --- |  
| all	| <class>.all()	| Prints the string representation of all instances of a given class |
| count	| <class>.count() | Prints the number of instances of a given class |
| show	| <class>.show(<id>)	| Prints the string representation of an instance based on its class and id |
| destroy |	<class>.destroy(<id>)	| Deletes an instance based on its class and id |
| update	| <class>.update(<id>, <attribute>, <value>) or <class>.update(<id>, <dictionary>)	| Updates an instance based on its class and id by adding or updating an attribute or multiple attributes |
## Classes 🏘️
The project uses the following classes:
| Class	| Attributes |
| ---   |    ---     |
| BaseModel	| id, created_at, updated_at |
| User | email, password, first_name, last_name |
| State	| name |
| City	| state_id, name |
| Amenity	| name |
| Place	| city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| Review	| place_id, user_id, text | 

## Tests ✅
The project includes unittests for all classes and methods. To run the tests, change directory to the tests folder and run the following command:
```
python3 -m unittest discover
```
## Second Step: Web Static 💻 (0x01. AirBnB clone - Web static :house_with_garden:)

This project is part of the **AirBnB clone** project, which aims to create a web application that connects people who have a home to offer with people who need a place to stay temporarily. The **web static** part focuses on creating the front end of the web application using **HTML** and **CSS**.

![thecurrentstage](https://peytonbrsmith.netlify.app/projects/web/airbnb/87c01524ada6080f40fc_hu0d2caa1c6b3d5ace81a9d755296ff01f_123580_700x0_resize_box_3.png)


## Files 📂
This section lists the files and folders in this project and their descriptions.
- [console.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/console.py): The main script that runs the console.
- [models](https://github.com/ahmedmkamal313/AirBnB_clone/tree/master/models): A folder that contains the classes and modules for the objects.
  - [base_model.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/models/base_model.py): The base class for all objects.
  - [user.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/models/user.py): The class for user objects.
  - [state.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/models/state.py): The class for state objects.
  - [city.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/models/city.py): The class for city objects.
  - [amenity.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/models/amenity.py): The class for amenity objects.
  - [place.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/models/place.py): The class for place objects.
  - [review.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/models/review.py): The class for review objects.
  - [engine](https://github.com/ahmedmkamal313/AirBnB_clone/tree/master/models/engine): A subfolder that contains the modules for the storage engine.
    - [file_storage.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/models/engine/file_storage.py): The module for file storage.
- [tests](https://github.com/ahmedmkamal313/AirBnB_clone/tree/master/tests): A folder that contains the unittests for the project.
  - [test_models](https://github.com/ahmedmkamal313/AirBnB_clone/tree/master/tests/test_models): A subfolder that contains the unittests for the classes and modules in the models folder.
    - [test_base_model.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_models/test_base_model.py): The unittests for the base model class.
    - [test_user.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_models/test_user.py): The unittests for the user class.
    - [test_state.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_models/test_state.py): The unittests for the state class.
    - [test_city.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_models/test_city.py): The unittests for the city class.
    - [test_amenity.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_models/test_amenity.py): The unittests for the amenity class.
    - [test_place.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_models/test_place.py): The unittests for the place class.
    - [test_review.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_models/test_review.py): The unittests for the review class.
    - [test_engine](https://github.com/ahmedmkamal313/AirBnB_clone/tree/master/tests/test_models/test_engine): A subfolder that contains the unittests for the modules in the engine subfolder.
      - [test_file_storage.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_models/test_engine/test_file_storage.py): The unittests for the file storage module.
   - [test_console.py](https://github.com/ahmedmkamal313/AirBnB_clone/blob/master/tests/test_console.py): The unittests for the console.
- [web_static](https://github.com/ahmedmkamal313/AirBnB_clone/tree/master/web_static): A folder     that contains the static files for the web application, such as HTML, CSS, and images.
   - [images](https://github.com/ahmedmkamal313/AirBnB_clone/tree/master/web_static/images): a directory contains the images used in the web pages, such as logos, icons, and photos.
   - [styles](https://github.com/ahmedmkamal313/AirBnB_clone/tree/master/web_static/styles): a directory the CSS style sheets for the web pages, such as fonts, colors, and layouts
- `README.md`: This file, which contains an overview of the project and how to use it.


