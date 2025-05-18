from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'A template project to learn GitHub Actions'

setup(
    name='myproject',
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pytest'
    ],
)

