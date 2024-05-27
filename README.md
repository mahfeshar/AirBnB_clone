# AirBnB Clone Project

Welcome to the AirBnB Clone project repository! This project is a part of the Holberton School curriculum and aims to build a full web application, including a dynamic website, database, and a command-line interface (CLI) to manage the application's data.

## Table of Contents
1. [Project Overview](#project-overview)
2. [How to Use the Console](#how-to-use-the-console)
3. [Console Commands](#console-commands)
4. [Web Static](#web-static)
5. [Preview](#preview)

## Project Overview

The AirBnB Clone project is divided into several key parts:
- A command-line interface (CLI) to manage database objects.
- A storage engine that handles long-term storage of objects.
- A dynamic website for users to interact with the application.
- Static HTML and CSS files to build the front-end structure and styling.


## How to Use the Console

The console is a command-line interpreter used to manage the application's data. You can create, update, delete, and retrieve objects using this console.

### Starting the Console

To start the console, run the following command from the root directory of the repository:

```bash
./console.py
```

## Console Commands
The console supports the following commands:

- `help` or `?`: Display a help message with available commands.
- `quit` or `EOF`: Exit the console.
- `create <class_name>`: Create a new instance of a class.
- `show <class_name> <id>`: Display the string representation of an instance based on the class name and ID.
- `destroy <class_name> <id>`: Delete an instance based on the class name and ID.
- `all <class_name>`: Display all instances of a class. If no class name is provided, display all instances of all classes.
- `update <class_name> <id> <attribute_name> <attribute_value>`: Update an instance based on the class name and ID by adding or updating an attribute.
Example Usage:
```bash
$ ./console.py
(hbnb) create User
(hbnb) show User 1234-1234-1234
(hbnb) all User
(hbnb) update User 1234-1234-1234 name "John Doe"
(hbnb) destroy User 1234-1234-1234
(hbnb) quit
```

## Web Static
The web_static directory contains the static files for the web application. This includes HTML files, CSS files, and images. The static files are used to build the front-end structure and styling of the website.

## Preview
To preview the static website, open the index.html file in a web browser. This will display the basic layout and styling of the web application as defined by the HTML and CSS files.
![image](https://github.com/mahfeshar/AirBnB_clone/assets/104142801/9ea32705-47a5-418d-8d4b-3d9b04bd4761)


