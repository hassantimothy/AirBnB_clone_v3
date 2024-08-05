# AirBnB Clone - RESTful API

The RESTful API represents the third phase of the AirBnB project at Holberton School. This segment focuses on implementing fundamental concepts in higher-level programming, ultimately aiming to deploy a server that mimics the AirBnB website (HBnB). The API developed in this phase will manage objects for the HBnB website.

### Key Features
* **Create**: Add new objects (e.g., users, places).
* **Retrieve**: Fetch objects from files or databases.
* **Operations**: Perform actions on objects (e.g., counting, computing statistics).
* **Update**: Modify object attributes.
* **Destroy**: Remove objects.

## Table of Contents
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples](#examples)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is developed and tested on Ubuntu 20.04 LTS using Python 3.4.3.

## Installation
1. Clone the repository: `git clone "https://github.com/hassantimothy/AirBnB_clone_v3.git"`
2. Navigate to the directory: `cd AirBnB_clone_v3`
3. Run the application interactively: `python3 -m api.v1.app`
4. Run the application non-interactively: `HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m api.v1.app`

## File Descriptions
**[console.py](console.py)** - The command interpreter entry point. Commands supported:
* `EOF` - Exits the console.
* `quit` - Exits the console.
* `<emptyline>` - Overwrites the default empty line method (does nothing).
* `create` - Creates a new `BaseModel` instance, saves it to the JSON file, and prints the ID.
* `destroy` - Deletes an instance based on class name and ID, and saves the change to the JSON file.
* `show` - Prints the string representation of an instance based on class name and ID.
* `all` - Prints all instances or instances of a specific class.
* `update` - Updates an instance based on class name and ID by adding or modifying attributes, and saves the change to the JSON file.

**`models/` Directory** - Contains classes for this project:
* **[base_model.py](/models/base_model.py)** - BaseModel class, the foundation for future classes.
  * `__init__(self, *args, **kwargs)` - Initializes the base model.
  * `__str__(self)` - Returns a string representation of the BaseModel class.
  * `save(self)` - Updates the `updated_at` attribute with the current datetime.
  * `to_dict(self)` - Returns a dictionary containing all key-value pairs of the instance.

*Classes inheriting from BaseModel:*
  * [amenity.py](/models/amenity.py)
  * [city.py](/models/city.py)
  * [place.py](/models/place.py)
  * [review.py](/models/review.py)
  * [state.py](/models/state.py)
  * [user.py](/models/user.py)

**`/models/engine/` Directory** - Contains the File Storage class for JSON serialization and deserialization:
* **[file_storage.py](/models/engine/file_storage.py)** - Handles serialization of instances to a JSON file and deserialization back to instances.
  * `all(self)` - Returns the `__objects` dictionary.
  * `new(self, obj)` - Adds an object to `__objects` with the key `<obj class name>.id`.
  * `save(self)` - Serializes `__objects` to the JSON file (path: `__file_path`).
  * `reload(self)` - Deserializes the JSON file to `__objects`.

**`/api/` Directory** - Contains Flask web applications for the RESTful API:
* **[app.py](/api/v1/app.py)** - Main Flask application.
  * `create_app(test_config=None)` - Flask application factory.
  * `teardown_appcontext(exception)` - Closes the database session after each request.
  * `not_found(error)` - Handles 404 errors.

* **`views/` Directory** - Contains API views:
  * [index.py](/api/v1/views/index.py) - Index view for the API.
  * [states.py](/api/v1/views/states.py) - View for State objects.
  * [cities.py](/api/v1/views/cities.py) - View for City objects.
  * [amenities.py](/api/v1/views/amenities.py) - View for Amenity objects.
  * [users.py](/api/v1/views/users.py) - View for User objects.
  * [places.py](/api/v1/views/places.py) - View for Place objects.
  * [places_reviews.py](/api/v1/views/places_reviews.py) - View for Review objects.

## Examples
* **Get all states**: `curl -X GET http://0.0.0.0:5000/api/v1/states`
* **Get a specific state**: `curl -X GET http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99`
* **Delete a state**: `curl -X DELETE http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99`
* **Create a new state**: `curl -X POST http://0.0.0.0:5000/api/v1/states/ -H "Content-Type: application/json" -d '{"name": "California"}'`
* **Update a state**: `curl -X PUT http://0.0.0.0:5000/api/v1/states/8f165686-c98d-46d9-87d9-d6059ade2d99 -H "Content-Type: application/json" -d '{"name": "California is so cool"}'`

## Bugs
No known issues at the moment.

## Authors
Hassan Timothy - [GitHub](https://github.com/hassantimothy)

## License
This project is in the public domain. No copyright protection.
