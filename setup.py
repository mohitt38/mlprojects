from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'



def get_requirements(file_path:str)->list[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove('-e .')
    return requirements


setup(
name='mlproject',
version='0.0.1',
author='MohitNagda',
author_email='mohitnagda83@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)    