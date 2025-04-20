from setuptools import find_packages, setup

setup(
    name="azure-iac-wrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "azure-identity",
        "azure-mgmt-resource",
        "azure-mgmt-compute",
        "azure-mgmt-network",
        "azure-mgmt-storage"
    ],
    author="Daniel Korang",
    author_email="krng.daniel@gmail.com",
    description="A python-wrapper to abstract Azure IaC",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/d-krng/azure-iac-wrapper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)