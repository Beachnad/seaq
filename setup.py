import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="seaq",
    version="0.0.1",
    author="Danny Beachnau",
    author_email="DannyBeachnau@gmail.com",
    description="Easily integrate pandas data frame and sqlite.",
    license="MIT",
    keywords="db pandas sqlite",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['seaq'],
    install_requires=["pandas"],
    long_description=read('README')
)
