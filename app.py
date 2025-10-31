from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, text

app = Flask(__name__)

DATABASE_URL = 'postgresql://neondb_owner:npg_vWoGATj8f3YH@ep-noisy-heart-a4m5rbaa-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

engine = create_engine(DATABASE_URL)

@app.route('/')
def index():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        users = result.fetchall()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO users (name, email) VALUES (:n, :e)"),
            {"n": name, "e": email}
        )
        conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
