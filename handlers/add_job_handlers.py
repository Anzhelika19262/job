from flask import redirect, render_template, Blueprint
from data import db_session, jobs
from forms import add_job

blueprint = Blueprint('add_job_handlers', __name__, template_folder='templates')


@blueprint.route('/add_job',  methods=['GET', 'POST'])
def add_jobs():
    form = add_job.JobForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        job = jobs.Jobs()
        job.title = form.title.data
        job.team_leader = form.team_leader.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        session.commit()
        return redirect('/jobs')
    return render_template('add_job.html', title='Добавление работы',
                           form=form)
