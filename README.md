# RESTfulDB

## Overview
This project is a RESTful API built with Flask and Flask-RESTful for managing computer records. It allows users to create, retrieve, update, and delete computer data stored in a database.

## Project Structure
The project is organized as follows:

```markdown
RESTfulDB/
│
├── app.py
├── models.py
├── resources.py
├── parsers.py
├── schemas.py
├── db_setup.py
├── tests/
│   └── test_api.py
├── requirements.txt
└── README.md
```

## Features

- Add a new computer to the database
- Retrieve all computers or a single computer by ID
- Update computer information
- Delete a computer record
- Input validation using argument parsers
- Structured responses using `marshal_with` and schemas

# Installation
Follow these steps to set up the project locally:

1. Clone the repository:

```bash
git git@github.com:CoderSthe/RESTfulDB.git
cd RESTfulDB
```

2. Create a virtual environment:

```bash
python -m venv <virtual environment name>
source <virtual environment name>/bin/activate  # For Linux/macOS
<virtual environment name>\Scripts\activate     # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the database:

```bash
python db_setup.py
```

5. Run the application:

```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

| Method        | Endpoint               | Description                    |
| :-------------| :--------------------- | :----------------------------- |
| POST          | `/api/computers`       | Add a new computer             |
| GET           | `/api/computers`       | Get all computers              |
| GET           | `/api/computers/<id>`  | Get a single computer by ID    |
| PATCH         | `/api/computers/<id>`  | Update a computer by ID        |
| DELETE        | `/api/computers/<id>`  | Delete a computer by ID        |

## Example JSON Payloads
### Add a New Computer (`POST /api/computers`)

```json
{
    "hard_drive_type": "SSD",
    "processor": "Intel i7",
    "ram_amount": 16,
    "maximum_ram": 32,
    "form_factor": "Laptop"
}
```

### Update a Computer (`PATCH /api/computers/1`)

```json
{
    "hard_drive_type": "HDD",
    "processor": "Intel i5",
    "ram_amount": 8,
    "maximum_ram": 16,
    "form_factor": "Desktop"
}
```

## Running Tests
Run the unit tests located in the `tests/` directory:

```bash
python -m unittest discover tests
```

## Technologies Used

- **Python**: Main programming language
- **Flask**: Web framework
- **Flask-RESTful**: For building the RESTful API
- **SQLAlchemy**: ORM for database operations
- **unittest**: For testing

## License
This project is licensed under the [MIT License](https://opensource.org/license/MIT).