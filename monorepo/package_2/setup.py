from pathlib import Path
from setuptools import setup
setup(
  name='package_2',
  version='0.1.0',
  python_requires='>=3.8',
  install_requires=[f"package_1 @ file://localhost/blah/{Path(__file__).parents[1].resolve()}/package_1#egg=package_1"]
)
