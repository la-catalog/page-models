from pathlib import Path
from setuptools import setup, find_packages

long_description = Path("README.md").read_text()

setup(
    name="page-product",
    version="0.0.1",
    description="Create and validate product",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagola92/page-product",
    author="thiagola92",
    author_email="thiagola92@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    keywords="product, create, validate",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "bson==0.5.10",
        "gtin==1.3.1631641032",
        "schema==0.7.5",
    ],
    python_requires=">=3.7",
)
