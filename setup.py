from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="Nischay",
    author_email="nischay17p@gmail.com",
    packages=find_packages()   # find_package helps to look for the constructor file/function in every folder and whenever it is present then it considers that particular file or folder to be local package
)