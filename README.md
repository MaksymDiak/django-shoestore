# ShoeStore Application

## Requirements

- Python 3.13.1
- `pip` installed

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/MaksymDiak/django-shoestore.git
   cd django-shoestore
   ```

2. Create and activate a virtual environment:
    ```
    python -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
    .venv\Scripts\activate  # On Windows
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. In shoestore/shoestore create file (local_settings.py) with next content:
    ```
    django_secret_key = "your_secret_key"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "db_name",
            "USER": "postgres",
            "PASSWORD": "password",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
    ```

5. Run the Application:
    ```
    cd shoestore
    python manage.py runserver
    ```