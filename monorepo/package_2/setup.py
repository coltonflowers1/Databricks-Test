import os
from pathlib import Path
import sys
from setuptools import setup
IN_DATABRICKS = "DATABRICKS_RUNTIME_VERSION" in os.environ
local_install_requirement_location =  "/databricks/driver/" if IN_DATABRICKS else os.getcwd()
setup(
  name='package_2',
  version='0.1.0',
  python_requires='>=3.8',
  packages=["package_2"],
  install_requires=[f"package_1 @ file://localhost/{local_install_requirement_location}/monorepo/package_1#egg=package_1"] 
)
