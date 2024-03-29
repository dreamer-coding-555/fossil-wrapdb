"""
Module: setup.py
Description: This Python source file is part of the Native Python Application, which is a project under the Trilobite Coder Lab.

Author:
- Name: Michael Gene Brockus (Dreamer)
- Email: michaelbrockus@gmail.com
- Website: https://trilobite.code.blog

License: This software is released under the Apache License 2.0. Please refer to the LICENSE file for more details.

Purpose:
- This Python source file contains the implementation for the Native Python Application.
- It includes the main logic and functionality required for the application to run.
- Review and modify this file as needed for your specific project requirements.

For more information on the Native Python Application and the Trilobite Coder Lab project, please refer to the project documentation and website.
"""
from setuptools import setup, find_packages

setup(
    name="fossil-wrapdb",
    version="0.1.0",
    author="Michael Gene Brockus (Dreamer)",
    author_email="michaelbrockus@gmail.com",
    description="Fossil Logic WrapDB tool allows installing Fossil Logic Wrap files.",
    long_description="Fossil Logic WrapDB tool, this allows users to download Meson build wrap files that have been loaded to upstream from a CLI interface into your project.",
    url="https://github.com/dreamer-coding-555/fossil-wrapdb",
    packages=find_packages(),  # Automatically find and include all packages
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apchie 2.0 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires=">=3.7",  # Specify the minimum Python version required
)
