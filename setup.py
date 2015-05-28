
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description='Docker-CLI',
    author='Iryna Cherniavska',
    url='http://dockercli.com.',
    download_url='http://github.com/j-bennet/dockercli.',
    author_email='i[dot]chernyavska[at]gmail[dot]com.',
    version='0.2',
    install_requires=[
        'pygments>=2.0.2',
        'prompt-toolkit==0.32',
        'docker-py>=1.2.0',
        'tabulate>=0.7.5',
        'click>=4.0',
        'py-pretty>-0.1',
        'configobj >= 5.0.6'
    ],
    extras_require={
        'testing': ['pytest', 'mock'],
    },
    entry_points={
        'console_scripts': 'dockercli = dockercli.main:cli'
    },
    packages=['dockercli'],
    scripts=[],
    name='dockercli'
)