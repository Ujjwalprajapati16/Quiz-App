from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import Question, Result

import random

def questions_routes(app, db):
    @app.route('/quiz', methods=['GET', 'POST'])
    @login_required
    def quiz():
        if request.method == 'POST':
            questions = Question.query.all()
            score = 0
            total = 10  # Fixed to 10 questions evaluated

            for q in questions[:10]:  # Only check first 10
                selected = request.form.get(str(q.id))
                if selected and selected == q.answer:
                    score += 1

            # Save result
            result = Result(user_id=current_user.id, score=score, date=datetime.now())
            db.session.add(result)
            db.session.commit()

            return render_template('result.html', score=score, total=total)

        # Show 10 random questions
        all_questions = Question.query.all()
        questions = random.sample(all_questions, 10) if len(all_questions) >= 10 else all_questions
        return render_template('quiz.html', questions=questions)

    @app.route('/add-question', methods=['GET', 'POST'])
    @login_required
    def add_question():
        if request.method == 'POST':
            question = request.form['question']
            option1 = request.form['option1']
            option2 = request.form['option2']
            option3 = request.form['option3']
            option4 = request.form['option4']
            answer = request.form['answer']

            if answer not in [option1, option2, option3, option4]:
                flash("Answer must match one of the provided options.", "danger")
                return redirect(url_for('add_question'))

            new_question = Question(
                question=question,
                option1=option1,
                option2=option2,
                option3=option3,
                option4=option4,
                answer=answer
            )
            db.session.add(new_question)
            db.session.commit()

            flash("Question added successfully!", "success")
            return redirect(url_for('add_question'))

        return render_template('add_question.html')
