import os
from pathlib import Path
import sys
from setuptools import setup

IN_DATABRICKS = "DATABRICKS_RUNTIME_VERSION" in os.environ
def local_pkg(name: str) -> str:
    """Returns a path to a local package."""
    if IN_DATABRICKS: 
      return f'{name} @ file://localhost/databricks/driver/Databricks-Test/monorepo/name'
    else:
      return f'{name} @ file://localhost/{Path.cwd().parent / name}'

local_install_requirement_location =  "/databricks/driver/Databricks-Test/monorepo" if IN_DATABRICKS else Path.cwd().parent
setup(
  name='package_2',
  version='0.1.0',
  python_requires='>=3.8',
  packages=["package_2"],
  install_requires=[local_pkg("package_1")] 
)