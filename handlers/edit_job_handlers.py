from flask import redirect, render_template, Blueprint, abort
from flask_login import current_user
from data import db_session, jobs
from forms import add_job

blueprint = Blueprint('edit_job_handlers', __name__, template_folder='templates')


@blueprint.route('/jobs/<int:id>', methods=['GET'])
def get_jobs(id):
    form = add_job.JobForm()
    session = db_session.create_session()
    job = session.query(jobs.Jobs).filter((jobs.Jobs.id == id, jobs.Jobs.user == current_user) |
                                          (jobs.Jobs.id == 1)).first()
    if job:
        form.title.data = job.title
        form.team_leader.data = job.team_leader
        form.work_size.data = job.work_size
        form.collaborators.data = job.collaborators
        form.is_finished.data = job.is_finished
    else:
        abort(404)
    return render_template('news.html', title='Edit_news', form=form)


@blueprint.route('/jobs/<int:id>', methods=['POST'])
def edit_jobs(id):
    form = add_job.JobForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        job = session.query(jobs.Jobs).filter((jobs.Jobs.id == id, jobs.Jobs.user == current_user) |
                                              (jobs.Jobs.id == 1)).first()
        if job:
            form.title.data = job.title
            form.team_leader.data = job.team_leader
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.is_finished.data = job.is_finished
            session.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html', title='Редактирование работы', form=form)
