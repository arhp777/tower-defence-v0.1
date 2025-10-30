from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# Встановіть секретний ключ для використання сесій та флеш-повідомлень
app.secret_key = 'your_secret_key_here' 

# Приклад бази даних користувачів (у реальному додатку використовуйте СУБД)
USERS = {
    'testuser': 'password123',
    'admin': 'adminpass'
}

@app.route('/')
def index():
    # Перенаправлення на сторінку входу за замовчуванням
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Перевірка облікових даних
        if username in USERS and USERS[username] == password:
            # Успішний вхід. Перенаправляємо на інший файл (маршрут 'dashboard')
            flash('Ви успішно увійшли!', 'success')
            return redirect(url_for('dashboard', user=username))
        else:
            # Помилка входу
            error = 'Неправильний логін або пароль'
            flash('Неправильний логін або пароль', 'danger')

    # Відображення сторінки входу (для GET-запиту або невдалого POST-запиту)
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    # Це "інший файл" (інша сторінка), на яку перенаправляємо
    user = request.args.get('user', 'Гість') # Отримуємо ім'я користувача з параметрів URL
    return render_template('dashboard.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)