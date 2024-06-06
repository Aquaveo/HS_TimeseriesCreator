import os
import sys
from setuptools import setup, find_packages, find_namespace_packages
from tethys_apps.app_installation import find_all_resource_files
from tethys_apps.base.app_base import TethysAppBase

### Apps Definition ###
app_package = 'hydroshare_resource_creator'
release_package = f'{TethysAppBase.package_namespace}-{app_package}'

### Python Dependencies ###
dependencies = []

# -- Get Resource File -- #
resource_files = find_all_resource_files(app_package, TethysAppBase.package_namespace)

setup(
    name=release_package,
    version='1',
    description='Creates a HydroShare resource from the CUAHSI data client',
    long_description='',
    keywords='',
    author='Matthew Bayles',
    author_email='mmbayles@gmail.com',
    url='',
    license='',
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)
