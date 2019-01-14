import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="seaq",
    version="0.0.4",
    author="Danny Beachnau",
    author_email="DannyBeachnau@gmail.com",
    description="Easily integrate pandas data frame and sqlite.",
    license="MIT",
    keywords="db pandas sqlite",
    url="http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    package_data={'seaq': ['sql/*.sql']},
    install_requires=["pandas"],
    long_description=read('README.md')
)
