from fabric.api import *

env.use_ssh_config = True

def production():
    env.host = ['bob']

def prepare_deploy():
    local("git add -p && git commit")
    local("git push")

def deploy():
    run('whoami')