from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a DataFrame
questions_df = pd.read_csv('quizfragen.csv')


@app.route('/')
def quiz():
    # Randomly select 10 questions
    selected_questions = questions_df.sample(10).to_dict(orient='records')
    return render_template('quiz.html', questions=selected_questions)


@app.route('/result', methods=['POST'])
def result():
    correct_answers = 0
    results = []

    # Iterate over the form data and compare answers
    for i in range(1, 11):
        user_answer = request.form.get(f'question{i}')
        correct_answer = request.form.get(f'correct_answer{i}')
        question_text = request.form.get(f'question_text{i}')
        if user_answer == correct_answer:
            correct = True
            correct_answers += 1
        else:
            correct = False

        results.append({
            'question': question_text,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
            'correct': correct
        })

    return render_template('result.html', correct_answers=correct_answers, results=results)


@app.route('/retry')
def retry():
    return redirect(url_for('quiz'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=7007)
