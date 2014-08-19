#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst") as readme:
    long_description = readme.read()

with open("HISTORY.rst") as history:
    long_description += "\n\n" + history.read()

setup(name="backports.shutil_get_terminal_size",
      version="1.0.0",
      description="A backport of the get_terminal_size function from Python 3.3's shutil.",
      url="https://github.com/chrippa/backports.shutil_get_terminal_size",
      author="Christopher Rosell",
      author_email="chrippa@tanuki.se",
      license="MIT",
      long_description=long_description,
      packages=find_packages(),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
      ]
)

