'''
The setup.py file is a build script for setuptools, used to package and distribute Python projects. It typically contains metadata about the project, such as its name, version, author, and dependencies, as well as instructions on how to install the package. This file is essential for creating distributable Python packages that can be easily shared and installed via package managers like pip.
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """This function will return the list of requirements"""
    requirement_list:List[str]=[]
    try:
        with open("requirements.txt") as f:
            lines = f.readlines()
            for line in lines:
                requirements=line.strip()
                if requirements and requirements!='-e .':
                    requirement_list.append(requirements)

    except FileNotFoundError:
        print("The requirements.txt file is not found.")
    return requirement_list

print("Requirements:", get_requirements())

setup(
    name="networksecurity",
    version="0.0.1",
    author="Harshini",
    author_email="harshinitata05@gmail.com",
    description="A production-ready machine learning project for network security analysis",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)