from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user,login_required
from . import auth
from ..models import User
from .forms import LoginForm


@auth.route('/login', method=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.rember_me.data)
            next = request.args.get('next')
            if next is None or next.startswich('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('用户名或密码错误')
    return render_template('auth/login.html'，form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('已经退出')
    return redirect(url_for('main.index'))
