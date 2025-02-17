from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ticket/__init__.py
from ticket import __version__ as version

setup(
	name="ticket",
	version=version,
	description="Inhouse ticket system for bulkbox",
	author="Gatura Njenga",
	author_email="gaturanjenga@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
