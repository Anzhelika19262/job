from flask import render_template, Blueprint
from data import db_session, jobs

blueprint = Blueprint('all_jobs_handlers', __name__, template_folder='templates')


@blueprint.route("/jobs")
def work_log():
    session = db_session.create_session()
    log = session.query(jobs.Jobs).all()
    return render_template("work_log.html", title='Jobs', logs=log)