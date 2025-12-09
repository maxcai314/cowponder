from setuptools import setup, find_packages

def read_file(filename):
    try:
        with open(filename) as readme_file:
            return readme_file.read()
    except:
        return ''

requirements = read_file('requirements.txt')

LONG_DESCRIPTION = read_file('README.md')

setup(
    name="cowponder",
    description="A simple command that displays randomly selected philosophical thoughts from a cow",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://max.xz.ax/cowponder",
    author="Max Cai",
    version="0.1.5",
    packages=find_packages(),
    include_package_data=True,
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