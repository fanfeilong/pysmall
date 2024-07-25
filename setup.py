#!/usr/bin/env python

from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pyeff",
    version="0.1.0",
    description="Small Python lib, User friendly API for daily python code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Fan Fei Long",
    author_email="fanfeilong@gmail.com",
    url="https://github.com/fanfeilong/pyeff.git",
    license="MIT",
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
)
