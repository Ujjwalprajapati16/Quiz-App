from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from models import Result, User
from app import db

def auth_routes(app, db, bcrypt):
    
    @app.route('/')
    def home():
        if not current_user.is_authenticated:
            # Get the leaderboard (top users)
            leaderboard = db.session.query(User.name, db.func.max(Result.score).label('max_score'))\
                .join(Result, Result.user_id == User.id)\
                .group_by(User.id)\
                .order_by(db.desc('max_score'))\
                .limit(5).all()
            return render_template('home.html', leaderboard=leaderboard)
        # Get the latest quiz results for the logged-in user
        results = Result.query.filter_by(user_id=current_user.id).order_by(Result.date.desc()).limit(5).all()

        # Get the leaderboard (top users)
        leaderboard = db.session.query(User.name, db.func.max(Result.score).label('max_score'))\
            .join(Result, Result.user_id == User.id)\
            .group_by(User.id)\
            .order_by(db.desc('max_score'))\
            .limit(5).all()

        # Calculate user progress
        completed_quizzes = len(results)
        average_score = round(sum([r.score for r in results]) / completed_quizzes, 2) if completed_quizzes > 0 else 0
        best_score = max([r.score for r in results], default=0)

        return render_template('home.html', results=results, leaderboard=leaderboard, 
                            completed_quizzes=completed_quizzes, average_score=average_score, best_score=best_score)

    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = User.query.filter_by(email=email).first()

            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid credentials. Please try again.', 'danger')

        return render_template('auth/login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already registered!', 'warning')
                return redirect(url_for('register'))

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))

        return render_template('auth/register.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Logged out successfully.', 'info')
        return redirect(url_for('login'))
