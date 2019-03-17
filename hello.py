from flask import Flask, render_template, session, redirect, url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'password'


class NameForm(FlaskForm):
    name = StringField('Whats your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name=session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Look like you have changed your name.')
        session['name']=form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
