from setuptools import setup, find_packages

setup(
    name='dbdd',
    version='0.12',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='DBD Desktop Python Wrapper',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'asyncio', 'uwuify', 'ascii_magic', 'requests', 'pathlib', 'colorama', 'datetime', 'discord', 'codecs', 'typing', 'logging'],
    url='https://github.com/bambikuu/dbdd.py',
    author='BambiKu',
    author_email='bambikuuu@gmail.com'
)