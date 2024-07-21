from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User

@app.route('/login', methods=['GET', 'POST'])  # 修改路由路径
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('用户名或密码无效')
            return redirect(url_for('login'))
        flash('登录成功！')
        return redirect(url_for('welcome'))  # 登录成功后重定向到 welcome 页面
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你，注册成功！')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # 返回 welcome.html 页面

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html')  # 返回 index.html 页面
