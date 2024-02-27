"""
Module: app.py
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
#!/usr/bin/env python
import os
import sys
import shutil
import subprocess
from tempfile import TemporaryDirectory

def fetch_wrap_file(package_name):
    repo_url = "https://github.com/fossil-lib/fossil-lib.github.io.git"
    repo_path = f"upstream/{package_name}/{package_name}.wrap"
    output_directory = "subprojects"
    output_file = os.path.join(output_directory, f"{package_name}.wrap")

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Create a temporary directory to clone the repository
    with TemporaryDirectory() as temp_dir:
        # Clone the repository
        subprocess.run(["git", "clone", "--depth", "1", repo_url, temp_dir], check=True)

        # Check if the file exists in the repository
        wrap_file_path = os.path.join(temp_dir, repo_path)
        if not os.path.isfile(wrap_file_path):
            print(f"Error: Wrap file not found for package '{package_name}'.")
            sys.exit(1)

        # Copy the wrap file to the subprojects directory
        shutil.copy(wrap_file_path, output_file)
        print(f"Wrap file '{package_name}.wrap' fetched and saved in 'subprojects' directory.")
