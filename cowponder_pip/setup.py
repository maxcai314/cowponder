from setuptools import setup

def read_file(filename):
    try:
        with open(filename) as readme_file:
            return readme_file.read()
    except:
        return ''

requirements = read_file('requirements.txt')

setup(
    name="cowponder",
    description="A simple command that displays randomly selected philosophical thoughts from a cow",
    url="https://max.xz.ax/cowponder",
    version="0.0.2",
    scripts=["src/cowponder/cowponder.py", "src/cowponder/ponder.py"],
    install_requires=requirements,
    keywords="cow philosophical ponder cowponder ascii ascii-art fun",
)