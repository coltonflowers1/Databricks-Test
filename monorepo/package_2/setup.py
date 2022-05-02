import os
from pathlib import Path
from setuptools import setup
from pyspark.sql import SparkSession

def get_dbutils(spark):
  from pyspark.dbutils import DBUtils
  return DBUtils(spark)



IN_DATABRICKS = "DATABRICKS_RUNTIME_VERSION" in os.environ
if IN_DATABRICKS: 
  github_api_key = get_dbutils(spark).secrets.get(scope="github", key="coltons_api_key")

def local_pkg(name: str) -> str:
    """Returns a path to a local package."""
    if IN_DATABRICKS: #pull from github repo, will need to specify api key here.
      # TODO: Retrive Github API key using secret. 
      return f'{name} @ git+https://{github_api_key}@github.com/coltonflowers1/Databricks-Test@master#subdirectory=monorepo/{name}'
    else: #pull from local files
      return f'{name} @ file://localhost/{Path.cwd().parent / name}'

local_install_requirement_location =  "/databricks/driver/Databricks-Test/monorepo" if IN_DATABRICKS else Path.cwd().parent
setup(
  name='package_2',
  version='0.1.0',
  python_requires='>=3.8',
  packages=["package_2"],
  install_requires=[local_pkg("package_1")]
)