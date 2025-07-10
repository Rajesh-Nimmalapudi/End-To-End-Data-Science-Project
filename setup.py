from setuptools import find_packages,setup
from typing import List
#here dont forget to run the setup file as to build  using pip install -e . to use our project a package


def get_requirements(file_path : str)-> List[str]:
    """
    this funtion will return the list of the requirements
    """
    requirements=[]
    with open(file_path) as file :
        requirements=file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
       
    return requirements


setup(
name = "ML Project",
version = "0.0.1",
author = "Rajesh",
author_email = "nimmalapudirajesh466@gmail.com",
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)