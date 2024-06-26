import subprocess


def _run(bash_script):
    return subprocess.call(bash_script, shell=True)


def start_prod():
    return _run("./scripts/start-prod")


def test():
    return _run("./scripts/test")
