# Coffee Shop

Coffee Shop is a web application developed with Django that allows users to explore, order, and manage coffee products online.

## Prerequisites

- Python 3.x
- Git

## Installation Instructions

Follow these steps to clone the project, create and activate a virtual environment, install the necessary dependencies, and run the application.

### 1. Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone <URL_DEL_REPOSITORIO>
```
### 2.  Create and Activate a Virtual Environment

Create a virtual environment for the project (recommended for managing dependencies in isolation):

```bash
python -m venv env
```

* Windows
```bash
\env\Scripts\activate
```

* Linux
```bash
source \env\Scripts\activate
```
### 3. Install Requirements

```bash
pip install -r requirements.txt

```

### 4. Apply Migrations

```bash
python manage.py migrate

```

### 5. Run the Project

```bash
python manage.py runserver

```

Open your browser and go to http://127.0.0.1:8000 to view the application in action.

-> http://127.0.0.1:8000/docs: to view Swagger documentation.