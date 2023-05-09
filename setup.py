from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in athletic_classic/__init__.py
from athletic_classic import __version__ as version

setup(
	name="athletic_classic",
	version=version,
	description="Athletic Classic",
	author="Athletic Classic",
	author_email="amarratvaknitwearsonline@gmail.com\",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
