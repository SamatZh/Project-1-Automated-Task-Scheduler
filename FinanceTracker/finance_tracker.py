from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    expense = request.form['expense']
    amount = request.form['amount']
    conn = sqlite3.connect('finance.db')
    conn.execute('INSERT INTO expenses (expense, amount) VALUES (?, ?)', (expense, amount))
    conn.commit()
    conn.close()
    return 'Expense added!'

if __name__ == '__main__':
    app.run(debug=True)

