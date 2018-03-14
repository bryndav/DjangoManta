from fabric.api import *

env.use_ssh_config = True

def production():
    env.host = ['bob']

def prepare_deploy(message):
    local("git add -p && git commit -m '{}'".format(message))
    local("git push")

def deploy():
    run('whoami')