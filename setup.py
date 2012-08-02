from setuptools import setup, find_packages
import sys, os

version = '0.0.3'

setup(name='github_repos_cloner',
      version=version,
      description="Clone all the github repos for backup purposes",
      long_description=(
            open('README.rst').read() + '\n' +
            open('CHANGES.txt').read()),
      classifiers=[
        'Environment :: Console',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='backup clone git organization',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='https://github.com/aclark4life/github_repos_cloner',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'pbs',
        'requests',
      ],
      entry_points={
        'console_scripts': 'github_repos_cloner=github_repos_cloner:clone_repos',
      }
      )
