from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1",
    packages=find_packages(where="src/main/python"),
    package_dir={"": "src/main/python"},
    install_requires=open("requirements.txt").read().splitlines(),
)