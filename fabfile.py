from fabric.api import *

env.use_ssh_config = True
env.hosts = 'bob'

def production():
    env.hosts = ['bob']

def prepare_deploy():
    local('git add -p && git commit')
    local('git push')

def clone():
    with cd('/var/www'):
        run('git clone https://github.com/bryndav/DjangoManta.git myproject')

def checkout(branch):
    with cd('/var/www/myproject'):
        run('git checkout %s' % branch)

def pull():
    with cd('/var/www/myproject'):
        run('git pull')

def migrate():
    with cd('/var/www/myproject'):
        run('python manage.py migrate')

def start():
    run('/var/www/myproject/apache2/start')

def stop():
    run('/var/www/myproject/apache2/stop')

def restart():
    run('/var/www/myproject/apache2/restart')

def static():
   with cd('var/www/myproject'):
       run('python manage.py collectstatic --noinput')

#TODO fix these commands
def update_host():
    sudo('apt-get update')
    sudo('apt-get upgrade -y')

def deploy():
    run('pwd')
