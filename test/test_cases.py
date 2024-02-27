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
from code.app import fetch_wrap_file
import unittest
import subprocess
import os
import tempfile
from unittest.mock import patch

class TestFossilWrapScript(unittest.TestCase):
    def test_fetch_wrap_file_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            package_name = "test_package"
            script_path = os.path.join(os.path.dirname(__file__), "fossil-wrap.py")
            output_directory = os.path.join(temp_dir, "subprojects")
            output_file = os.path.join(output_directory, f"{package_name}.wrap")

            with patch("subprocess.run") as mock_run:
                mock_run.return_value.returncode = 0

                with patch("shutil.copy") as mock_copy:
                    with patch("os.makedirs") as mock_makedirs:
                        with patch("os.path.isfile") as mock_isfile:
                            mock_isfile.return_value = True

                            subprocess.run(["python", script_path, package_name])

                            mock_makedirs.assert_called_once_with(output_directory, exist_ok=True)
                            mock_copy.assert_called_once()
                            mock_run.assert_called_once_with(["git", "clone", "--depth", "1", "https://github.com/fossil-lib/fossil-lib.github.io.git", f"{temp_dir}/temp_repo"], check=True)
                            mock_isfile.assert_called_once_with(f"{temp_dir}/temp_repo/upstream/{package_name}/{package_name}.wrap")

                            self.assertTrue(os.path.exists(output_file))

    def test_fetch_wrap_file_missing_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            package_name = "missing_package"
            script_path = os.path.join(os.path.dirname(__file__), "fossil-wrap.py")

            with patch("subprocess.run") as mock_run:
                mock_run.return_value.returncode = 0

                with patch("shutil.copy") as mock_copy:
                    with patch("os.makedirs") as mock_makedirs:
                        with patch("os.path.isfile") as mock_isfile:
                            mock_isfile.return_value = False

                            with self.assertRaises(SystemExit) as cm:
                                subprocess.run(["python", script_path, package_name])

                            mock_makedirs.assert_called_once_with(os.path.join(temp_dir, "subprojects"), exist_ok=True)
                            mock_copy.assert_not_called()
                            mock_run.assert_not_called()
                            mock_isfile.assert_called_once_with(f"{temp_dir}/temp_repo/upstream/{package_name}/{package_name}.wrap")

                            self.assertEqual(cm.exception.code, 1)

if __name__ == "__main__":
    unittest.main()
