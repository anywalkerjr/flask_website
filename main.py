from flask import Flask
import random
from facts import facts_list

app = Flask(__name__)

@app.route('/')
def main_site():
    return '<h1>Привет! <a href="/random_fact">Посмотри</a> случайный факт про технологические зависимости! Или <a href="/head_tail">брось монетку!</a></h1>'
@app.route("/head_tail")
def head_tail():
    return f'<h2>{random.choice(["Орел!", "Решка!"])}</h2><a href="/">Вернуться на главную страницу</a><br><a href="/head_tail">Бросить еще раз!</a>'

@app.route("/random_fact")
def random_fact():
    return f'<h2>{random.choice(facts_list)}</h2><a href="/">Вернуться на главную страницу</a><br><a href="/random_fact">Новый факт</a>'

app.run(debug=True)