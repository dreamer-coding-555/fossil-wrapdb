"""
Module: main.py
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
from code.app import fetch_wrap_file
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: fossil-wrap.py <package_name_1> <package_name_2> ...")
        sys.exit(1)

    package_names = sys.argv[1:]
    
    for package_name in package_names:
        fetch_wrap_file(package_name)

if __name__ == "__main__":
    main()
