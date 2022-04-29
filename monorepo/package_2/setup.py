from pathlib import Path
from setuptools import setup
home = str(Path.home())
setup(
  name='some_more_code',
  version='0.1.0',
  python_requires='>=3.8',
  modules=["some_more_code"],
  install_requires=[f"some_code @ file://localhost/{Path(__file__).parents[1].resolve()}/Databricks-Test/monorepo/package_1#egg=some_code"]
)
