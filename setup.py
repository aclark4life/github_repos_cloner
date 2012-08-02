from setuptools import setup, find_packages
import sys, os

version = '0.0.0'

setup(name='org_repos_cloner',
      version=version,
      description="Clone all the repos of an org for backup purposes",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Alex Clark',
      author_email='aclark@aclark.net',
      url='https://github.com/plone/org_repos_cloner',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'requests',
      ],
      entry_points={
        'console_scripts': 'org_repos_cloner=org_repos_cloner:clone_org_repos',
      }
      )
