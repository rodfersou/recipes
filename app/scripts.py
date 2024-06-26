import subprocess


def _run(bash_script):
    return subprocess.call(bash_script, shell=True)


def start_prod():
    return _run("/app/scripts/start-prod")


def test():
    return _run("/app/scripts/test")


def ipython():
    return _run("/app/scripts/ipython")


def echo_path():
    return _run("echo $PATH")
