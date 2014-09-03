from fabric.api import *


env.roledefs = {
    'staging': [],
    'production': [],
}


@roles('staging')
def deploy_staging():
    # Remove this line when you're happy that this Fabfile is correct
    raise RuntimeError("Please check the fabfile before using it")

    base_dir = '/usr/local/django/{{ project_name }}'
    virtualenv_dir = '/usr/local/django/virtualenvs/{{ project_name }}'
    python = virtualenv_dir + '/bin/python'
    pip = virtualenv_dir + '/bin/pip'

    supervisor_task = '{{ project_name }}'

    with cd(base_dir):
        run('git pull origin master')
        run(pip + ' install -r requirements.txt')
        run(python + ' {{ project_name }}/manage.py syncdb --settings={{ project_name }}.settings.production --noinput')
        run(python + ' {{ project_name }}/manage.py migrate --settings={{ project_name }}.settings.production --noinput')
        run(python + ' {{ project_name }}/manage.py collectstatic --settings={{ project_name }}.settings.production --noinput')
        run(python + ' {{ project_name }}/manage.py compress --settings={{ project_name }}.settings.production')
        run(python + ' {{ project_name }}/manage.py update_index --settings={{ project_name }}.settings.production')

    sudo('supervisorctl restart ' + supervisor_task)


@roles('production')
def deploy_production():
    # Remove this line when you're happy that this Fabfile is correct
    raise RuntimeError("Please check the fabfile before using it")

    base_dir = '/usr/local/django/{{ project_name }}'
    virtualenv_dir = '/usr/local/django/virtualenvs/{{ project_name }}'
    python = virtualenv_dir + '/bin/python'
    pip = virtualenv_dir + '/bin/pip'

    supervisor_task = '{{ project_name }}'

    with cd(base_dir):
        run('git pull origin master')
        run(pip + ' install -r requirements.txt')
        run(python + ' {{ project_name }}/manage.py syncdb --settings={{ project_name }}.settings.production --noinput')
        run(python + ' {{ project_name }}/manage.py migrate --settings={{ project_name }}.settings.production --noinput')
        run(python + ' {{ project_name }}/manage.py collectstatic --settings={{ project_name }}.settings.production --noinput')
        run(python + ' {{ project_name }}/manage.py compress --settings={{ project_name }}.settings.production')
        run(python + ' {{ project_name }}/manage.py update_index --settings={{ project_name }}.settings.production')

    sudo('supervisorctl restart ' + supervisor_task)
