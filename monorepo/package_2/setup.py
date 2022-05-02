import os
from pathlib import Path
import sys
from setuptools import setup
IN_DATABRICKS = sys.env.contains("DATABRICKS_RUNTIME_VERSION")
# local_install_requirement_location =  os.getcwd() if IN_DATABRICKS else "/databricks/driver/"
local_install_requirement_location =  os.getcwd() #if IN_DATABRICKS else "/databricks/driver/"
setup(
  name='package_2',
  version='0.1.0',
  python_requires='>=3.8',
  packages=["package_2"],
  install_requires=[f"package_1 @ file://localhost/{local_install_requirement_location}/monorepo/package_1#egg=package_1"] 
)
