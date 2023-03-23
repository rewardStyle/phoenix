from setuptools import find_packages, setup


with open('phoenix/_version.py') as version_file:
    exec(version_file.read())

with open('README.md') as r:
    readme = r.read()

setup(
    name='ltk_phoenix',
    version=__version__,
    packages=find_packages(exclude=('tests')),
    description='phoenix',
    long_description=readme,
    install_requires=[],
    extras_require={
        'dev': [
            'flake8',
            'flake8-docstrings',
            'flake8-import-order',
            'pip-tools',
            'pytest',
            'pytest-cov',
        ]
    },
)
