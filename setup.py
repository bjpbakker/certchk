from setuptools import setup

setup(
    name='certchk',
    version='0.1',
    description='List expiry of https certificates',
    long_description=open('README.rst').read(),
    author='Bart Bakker',
    author_email='bart@thesoftwarecraft.com',
    url='https://github.com/bjpbakker/certchk',
    license="BSD-3",
    scripts=['certchk']
)
