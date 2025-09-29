
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
        return requirements
    except FileNotFoundError:
        print(f"Error: {file_path} not found")
        return []

setup(
    name='mlproject',
    version='0.0.1',
    author='jyoshitha',
    author_email='sravanijyoshithav@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)