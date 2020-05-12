from flask import redirect, Blueprint, abort
from flask_login import current_user
from data import db_session, jobs

blueprint = Blueprint('delete_job_handlers', __name__, template_folder='templates')


@blueprint.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
def jobs_delete(id):
    session = db_session.create_session()
    job = session.query(jobs.Jobs).filter((jobs.Jobs.id == id, jobs.Jobs.user == current_user) |
                                          (jobs.Jobs.id == 1)).first()
    if job:
        session.delete(job)
        session.commit()
    else:
        abort(404)
    return redirect('/')
