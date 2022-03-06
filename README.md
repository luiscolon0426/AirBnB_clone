<h1 align="center" >
<br>
<img src="https://user-images.githubusercontent.com/90820795/156004222-8d617b49-62b1-4936-b055-031c7a704d10.png" height="50%" width="40%">
</h1>

# AirBnB_clone - The Console

## Description

Holberton **AirBnB** project, the goal its to make a copy of the AirBnB website. It doesn't have all the features, only some of them to cover all fundamental concepts of higher level programming.

## Usage

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

They should pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

## How to use it

Command | Description | Example
--------|-------------|--------
`help` | Display all commands available | `help`
`create` | Creates new object | `create <class>`
`update` | Updates attribute of an object | `User.update('123', {'name': 'Greg_n_Mel'})`
`all` | Display all objects in class | `User.all()`
`show` | Retrieve an object from a file | `User.show('123')`
`destroy` | Destroy specified object | `User.destroy('123')`
`quit` | Exits | `quit`

## \_\_init__.py

Every directory listed in the AirBnB repository contains a **\_\_init__.py** file in order for the directories be identified as a package. Although some of the \_\_init__.py files may be empty others (as shown below) may contain additional coding.

## Models

The **models/** directory contains the classes used for different models in the project.

File | Description | Attributes
---- | ----------- | ----------
`base_model.py` | BaseModel class for all the sub-classes | `id`, `created_at`, `updated_at`
`user.py` | User class for user information. | `email`, `password`, `first_name`, `last_name`
`amenity.py` | Amenity class for information about amenity. | `name`
`city.py` | City class for information about the city. | `state_id`, `name`
`state.py` | State class for information about the state. | `name`
`place.py` | Place class for details of the AirBnB apartments for rent. | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, `latitude`, `longitude`, `amenity_ids`
`review.py` | Review class for review information from the user/client. | `place_id`, `user_id`, `text`

## File storage

The **engine/** directory handles storage(temporarily), serialization and deserialization of data, using JSON file format.

The class FileStorage, located in **file_storage.py**, is defined with methods to run through the following flow:
```<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>```

Attributes | Description
---- | ----------- |
`__file_path` | (str). String-path to JSON file
`__objects` | (dict). Empty dictionary that will store objects.

Methods | Description
---- | ----------- | 
`all` | Returns the dictionary `__onjects`.
`new` | Sets in `__objects` the obj with key `<objClassName>.id`.
`save` | Serializes `__objects` to the JSON file.
`reload` | Deserializes the JSON file to `__objects`.


**\_\_init__.py** file, located in the **models/** directory, contains the instantiation of a **storage** object of class **FileStorage**, followed by a call to the **reload()** method on said object. The call of this method permits the automated reload of storage during initialization to recover serialized data from JSON file.
