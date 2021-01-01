from setuptools import setup,find_packages
with open("README.md","r") as f:
  README = f.read()
  f.close()


setup (
  name = 'buck',
  version = '0.1.0',
  description = ' Get started with your projects faster .',
  long_description = README,
  long_description_content_type="text/markdown",
  url = 'https://github.com/Pleasant-tech/Buck/',
  packages= find_packages(),
  package_data={
   # If any package contains *.txt or *.json files, include them:
    "": ["*.txt", "*.json"],
  },
  include_package_data = True,
  license="MIT",
  classifiers =[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
  ],
  entry_points = {
    "console_scripts": [
     " buck = buck.__main__:main",
    ]
  },
  zip_safe=False,
  author = 'Pleasant Tech',
  author_email = 'dummyware2020@gmail.com'
  
  
)