from setuptools import find_packages, setup
from typing import List

def get_requirements(path : str) -> List[str]:
    """
    Returns list of requirements
    """
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]
        requirements.remove("-e .")
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author='harpreet',
    author_email = 'hs762901@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)