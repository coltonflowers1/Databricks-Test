from pathlib import Path
from setuptools import setup
setup(
  name='package_2',
  version='0.1.0',
  python_requires='>=3.8',
  install_requires=[f"package_1 @ file://localhost/{Path.cwd()}/package_1#egg=package_1"]
)
