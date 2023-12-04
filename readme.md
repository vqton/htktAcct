# GL Accounting Web App

## Overview

This is a General Ledger (GL) accounting web application built using Flask. It allows users to manage financial transactions, track expenses, and generate financial reports.

## Features

- **Transaction Management:** Add, edit, and delete financial transactions.
- **Expense Tracking:** Categorize transactions and track expenses.
- **Financial Reports:** Generate and view financial reports for better insights.
- **User Authentication:** Secure login system to protect sensitive financial data.
- **Responsive Design:** User-friendly interface that works on various devices.

## Getting Started

### Prerequisites

- Python 3.x
- [Virtualenv](https://pypi.org/project/virtualenv/) (recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/gl-accounting-app.git
    cd gl-accounting-app
    ```

2. **Create a virtual environment:**

    ```bash
    virtualenv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Create a `.env` file in the root directory and configure the following:**

    ```env
    FLASK_APP=app
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    DATABASE_URI=your_database_uri
    ```

    Replace `your_secret_key` and `your_database_uri` with your actual secret key and database URI.

### Database Setup

1. **Initialize the database:**

    ```bash
    flask db init
    ```

2. **Apply migrations:**

    ```bash
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

### Running the Application

```bash
flask run
