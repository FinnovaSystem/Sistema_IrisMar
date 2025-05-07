# Flask Land App

This project is a Flask web application that allows users to filter land by city, register and log in, and add new land listings. It also provides contact options via WhatsApp and email. The application uses an SQLite database to manage users, cities, and land data.

## Project Structure

```
flask-land-app
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── add_land.html
│   │   └── contact.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── instance
│   └── config.py
├── migrations
├── app.db
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-land-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the application:**
   Update the `instance/config.py` file with your database URI and secret keys.

5. **Initialize the database:**
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the application:**
   ```
   flask run
   ```

## Features

- **User Authentication:** Users can register and log in to access private features.
- **Land Filtering:** Users can filter available land listings by city.
- **Add Land:** Authenticated users can add new land listings.
- **Contact Options:** Users can contact support via WhatsApp and email.

## License

This project is licensed under the MIT License.