from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, text

app = Flask(__name__)

# 🔹 Sustituye tu cadena real desde Neon.tech (con +pg8000)
DATABASE_URL = "postgresql+pg8000://neondb_owner:npg_jgLvA9Onc6CB@ep-still-mountain-ad6oq9x8-pooler.c-2.us-east-1.aws.neon.tech/neondb"

# 🔹 Crear conexión global
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
