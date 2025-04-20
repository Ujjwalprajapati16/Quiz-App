# Quiz Master

Quiz Master is a web-based application that allows users to test their knowledge across various categories by taking quizzes. Users can register, log in, and track their progress over time. The app also features a leaderboard to showcase top performers.

## Features

- **User Authentication**: Register, log in, and log out securely.
- **Take Quizzes**: Answer random questions and get instant feedback on your score.
- **Add Questions**: Contribute new questions to the quiz database.
- **Leaderboard**: View the top performers and their scores.
- **User Progress**: Track completed quizzes, average scores, and best scores.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite (via SQLAlchemy)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Migrations**: Flask-Migrate, Alembic

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/quiz-master.git
   cd quiz-master
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   Create a `.env` file in the root directory with the following content:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URI=sqlite:///quizdb.db
   ```

5. Initialize the database:
   ```bash
   flask db upgrade
   ```

6. Run the application:
   ```bash
   python main.py
   ```

7. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Folder Structure

```
Quiz App/
├── app.py               # Application factory and configuration
├── main.py              # Entry point for running the app
├── models.py            # Database models
├── routes/              # Application routes
│   ├── __init__.py
│   ├── auth_routes.py   # Authentication-related routes
│   └── questions_routes.py # Quiz-related routes
├── templates/           # HTML templates
│   ├── index.html       # Base template
│   ├── home.html        # Home page
│   ├── quiz.html        # Quiz page
│   ├── result.html      # Result page
│   ├── auth/            # Authentication templates
│   │   ├── base.html
│   │   ├── login.html
│   │   └── register.html
│   └── add_question.html # Add question page
├── static/              # Static files (CSS, JS, images)
├── migrations/          # Database migration files
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md            # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)