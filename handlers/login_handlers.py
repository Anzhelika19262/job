from flask import redirect, render_template, Blueprint
from flask_login import login_user
from data import db_session, users
from forms import login

blueprint = Blueprint('login_handlers', __name__, template_folder='templates')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = login.LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(users.User).filter(users.User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/jobs")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='', form=form)