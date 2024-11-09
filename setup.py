from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:

    ''' 
    This function will return the list of 
    '''
    requirements = []
    with open ("requirements.txt") as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = "Fabric_Detection_Project",
    version="0.0.1",
    author="Arjun",
    author_email="arjun.gupta.24@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)


