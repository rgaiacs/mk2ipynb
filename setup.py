from distutils.core import setup
from setuptools import setup

setup(
    name='mk2ipynb',
    version='0.1.0',
    author='Raniere Silva',
    author_email='ra092767@ime.unicamp.br',
    packages=['mk2ipynb'],
    url='',
    license='COPYING',
    description='Convert a markdown file to IPython Notebook.',
    long_description=open('README').read(),
    entry_points={
        'console_scripts':['mk2ipynb = mk2ipynb.main:main']}
)
