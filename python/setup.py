#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

readme = ""
history = ""

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

with open("requirements_dev.txt") as test_requirements_file:
    test_requirements = test_requirements_file.read()


setup_requirements = [
    "pytest-runner",
]


setup(
    author="Przemek Urbanski",
    author_email="przem@gmail.com",
    python_requires="^3.10",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",

        "Programming Language :: Python :: 3.10",
    ],
    description="Copypaster - a tool for copy and paste build using Python and GTK3",
    entry_points={
        "console_scripts": [
            "copypaster=copypaster.cli:main",
            "app=app.cli:main",
            "folders=folders.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="copypaster",
    name="copypaster",
    packages=find_packages(include=["copypaster"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/przor3n/copypaster",
    version="0.1.0",
    zip_safe=False,
)
