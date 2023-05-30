# Apparel360 - Database Management System

Apparel360 is a database management system built using Python as the frontend and MySQL as the backend. It provides a user-friendly interface to efficiently manage apparel-related data. This README file provides an overview of the system, instructions for setting it up, and a brief explanation of its features.

## Features

- User Authentication: Allows users to register and log in with secure authentication.
- Apparel Management: Provides functionalities to add, update, and delete apparel items in the database.
- Inventory Management: Enables users to track the inventory of apparel items, including stock levels and availability.
- Order Management: Allows users to create and manage customer orders, including order details, payment information, and order status.


## Technologies Used

- Frontend: Python
- Backend: MySQL
- Database Connectivity: MySQL Connector/Python

## Setup Instructions

To set up and run the Apparel360 database management system, follow these steps:

1. Install Python: Make sure Python is installed on your system. You can download it from the official Python website (https://www.python.org).

2. Install MySQL: Install MySQL database server on your system. Refer to the MySQL documentation for installation instructions specific to your operating system.

3. Install MySQL Connector/Python: Install the MySQL Connector/Python package using pip, the package installer for Python. Open a terminal or command prompt and run the following command:
 <br>&nbsp;&nbsp;`pip install mysql-connector-python`


4. Database Setup: Create a new MySQL database and import the required SQL schema and sample data. You can find the SQL script in the `database` directory of the project.

5. Configure Connection: In the Python code, update the database connection details (such as host, port, username, password, and database name) to match your MySQL configuration. The file to modify is usually named `config.py` or similar.

6. Run the Application: Run the Python script that serves as the frontend of the application. Open a terminal or command prompt, navigate to the project directory, and execute the following command:
<br>&nbsp;&nbsp;`python storemanagement.py`

## Usage
- Login: Log in using your registered credentials to access the system.
- Apparel Management: Add, update, and delete apparel items in the database.
- Inventory Management: Track the inventory of apparel items, including stock levels and availability.
- Order Management: Create and manage customer orders, including order details, payment information, and order status.

## Contributions

Contributions to the Apparel360 database management system are welcome. If you find any issues or have ideas for improvements, please submit them to the repository or make a pull request.

## License

The Apparel360 database management system is open-source and distributed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use the code according to your needs.
