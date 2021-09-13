from setuptools import *
from os import path

this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, "README.md"), encoding = "utf-8") as f:
    long_description = f.read()

with open(path.join(this_dir, "requirements.txt"), encoding = "utf-8") as f:
    requirements = f.readlines()

setup(
    name = "igpy",
    version = "1.0.3",
    author = "Devansh Singh",
    author_email = "devanshamity@gmail.com",
    url = "https://github.com/Devansh3712/InstagramPy",
    description = "Library for scraping basic Instagram data",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license = "MIT",
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = requirements,
)
