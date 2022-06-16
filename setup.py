from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()

setup(
    name="page-models",
    version="0.0.1",
    description="Sku model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagola92/page-models",
    author="thiagola92",
    author_email="thiagola92@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="models, sku, query",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "bson>=0.5.10",
        "gtin>=1.3.1631641032",
        "pydantic>=1.9.0",
    ],
    python_requires=">=3.10",
)
