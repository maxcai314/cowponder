from setuptools import setup, find_packages

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
    version="0.0.5",
    packages=find_packages(),
    py_modules=["cowponder"],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'cowponder=cowponder.cowponder:main',
            'ponder=cowponder.ponder:main',
        ],
    },
    install_requires=requirements,
    keywords="cow philosophical ponder cowponder ascii ascii-art fun",
)