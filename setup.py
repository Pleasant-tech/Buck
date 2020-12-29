from setuptools import setup,find_packages

setup (
  name = 'buck',
  version = '0.0.1',
  description = ' Get started with your projects faster',
  long_description = 'Store buckets of cli commands and run them with a custom keyword of your choice.',
  long_description_content_type="text/markdown",
  packages = find_packages(),
  include_package_data = True,
  entry_points ='''
    [console_scripts]
    buck = buck.src.cli:main
  ''',
  author = 'Pleasant Tech',
  author_email = 'dummyware2020@gmail.com'
  
  
)