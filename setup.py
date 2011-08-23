from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='switchboard',
      version=version,
      description="A message dispatcher for SharedSolar",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ivan Willig',
      author_email='iwillig@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      test_suite='switchboard.test',
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
        'webob',
	'pyyaml'
      ],
      entry_points= { 
        'console_scripts':
            ['switchboard = switchboard.server:run_server_command']
        }
      )
