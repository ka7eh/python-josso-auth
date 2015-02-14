from setuptools import setup


setup(
    name='python-josso-auth',
    description='A JOSSO backend for python-social-auth',
    keywords='python-social-auth,sso,josso',
    version='0.0.1',
    packages=['josso'],
    install_requires=['suds-jurko'],
    url='https://github.com/consbio/python-josso-auth',
    license='BSD'
)