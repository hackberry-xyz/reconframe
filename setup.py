from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('src/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='reconframe',
    version=main_ns['__version__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'ptpython>=3.0',
		'pycurl>=7.43',
		'SQLAlchemy>=1.3',
		'click>=7.1.2',
        'colorama',
    ],
    package_dir={'reconframe':'src'},
    packages=['reconframe'],
    entry_points='''
        [console_scripts]
        reconframe=reconframe.Cli:cli
    ''',
)
