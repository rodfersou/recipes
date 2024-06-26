import subprocess


def _run(bash_script):
    return subprocess.call(bash_script, shell=True)


def start_prod():
    return _run("gunicorn -w 4 'app.api:create_app()' --bind 0.0.0.0:5000")


def test():
    return _run("pytest")


def ipython():
    return _run("ipython")


def echo_path():
    return _run("echo $PATH")
