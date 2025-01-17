#!/usr/bin/env python3

import fnmatch
import os

from setuptools import setup, find_packages
from setuptools.command.install import install


def build_translations():
    from tuxemon.core.locale import T

    T.collect_languages()


class InstallAndBuildTranslations(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # build_translations()

# Get the version from the README file.
with open("README.md", "r") as f:
    VERSION = f.readline().split(" ")[-1].replace("\n", "")

# Get the dependencies from requirements.text
with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.read().splitlines()

# Configure the setuptools
setup(
    name="tuxemon",
    version=VERSION,
    description="Open source monster-fighting RPG",
    author="William Edwards",
    author_email="shadowapex@gmail.com",
    maintainer="Tuxemon",
    maintainer_email="info@tuxemon.org",
    url="https://www.tuxemon.org",
    include_package_data=True,
    packages=find_packages(),
    license="GPLv3",
    long_description="https://github.com/Tuxemon/Tuxemon",
    install_requires=REQUIREMENTS,
    python_requires=">=3.8",
    entry_points={"gui_scripts": ["tuxemon = tuxemon.__main__:main"]},
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
    cmdclass={"install": InstallAndBuildTranslations},
)
