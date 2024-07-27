# Event Management API

A simple RESTful API for managing events, attendees, and check-ins, built using Flask. This project provides endpoints for registering events, adding attendees, and handling check-ins.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Contributing](#contributing)

## Features

- **Event Management**: Create and retrieve events.
- **Attendee Management**: Register attendees, get badges, and retrieve attendees for a specific event.
- **Check-Ins**: Record check-ins for attendees.

## Prerequisites

- Python 3.6 or higher
- Flask
- SQLAlchemy (for ORM)
- A SQL database (configured in `src/models/settings/connection.py`)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/event-management-api.git
   cd event-management-api
    ```

2. **Create a Virtual Environment:**
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Set Up the Database:**

Ensure the database settings are correctly configured in src/models/settings/connection.py. Apply any migrations or initial setup required by your database.

4. **Usage:**

Run the application:

    ```bash
    python3 app.py
    ```

5. **Test the API Endpoints:**

You can use tools like Postman or curl to test the various endpoints.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to contribute to this project.

## Author

Project made by Gabriela Alvarenga.


