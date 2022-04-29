from pathlib import Path
from setuptools import setup
home = str(Path.home())
setup(
  name='package_2',
  version='0.1.0',
  python_requires='>=3.8',
  packages=["."],
  install_requires=[f"package_1 @ file://localhost/{Path(__file__).parents[1].resolve()}/Databricks-Test/monorepo/package_1#egg=package_1"]
)
