from setuptools import find_packages,setup
from typing import List

#this is supposed to be a marker for, if you have your requirements installed
Hyphen_e_dot = "-e ."

def get_requirements(file_path:str)->List[str]:
    #this function will return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #get rid of \n at the end of lines
        [req.replace("\n","") for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Adnan",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)