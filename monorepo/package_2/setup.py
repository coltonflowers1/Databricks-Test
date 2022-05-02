import os
from pathlib import Path
import sys
from setuptools import setup
IN_DATABRICKS = "DATABRICKS_RUNTIME_VERSION" in os.environ
local_install_requirement_location =  "/databricks/driver/Databricks-Test/monorepo" if IN_DATABRICKS else Path.cwd().parent
setup(
  name='package_2',
  version='0.1.0',
  python_requires='>=3.8',
  packages=["package_2"],
  install_requires=[f"package_1 @ file://localhost/{local_install_requirement_location}/package_1#egg=package_1"] 
)