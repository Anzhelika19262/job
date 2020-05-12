from flask import Flask, render_template
from data import users, db_session
from handlers import login_handlers, registration_handlers, add_job_handlers, all_jobs_handlers, edit_job_handlers, \
    delete_job_handlers
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(users.User).get(user_id)


def main():
    db_session.global_init("db/mars_one.sqlite")
    app.register_blueprint(login_handlers.blueprint)
    app.register_blueprint(registration_handlers.blueprint)
    app.register_blueprint(add_job_handlers.blueprint)
    app.register_blueprint(all_jobs_handlers.blueprint)
    app.register_blueprint(edit_job_handlers.blueprint)
    app.register_blueprint(delete_job_handlers.blueprint)
    app.run()


@app.route('/')
def index():
    return render_template('base.html', title='Main page')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')