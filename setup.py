from setuptools import setup,find_packages
with open("README.md","r") as f:
  README = f.read()
  f.close()


setup (
  name = 'buck',
  version = '0.2.7',
  description = ' Get started with your projects faster .',
  long_description = README,
  long_description_content_type="text/markdown",
  url = 'https://github.com/Pleasant-tech/Buck/',
  keywords='productivity, setuptools, bucket, cli',
  #package_dir={'': 'src'},
  package = find_packages(),
  include_package_data = True,
  package_data={  
   '': ['data.json'],
  },
  
 data_files=[('my_data', ['data.json'])],
 
  license="MIT",
  classifiers =[
    "License :: OSI Approved :: MIT License",
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3 :: Only',
  ],
  entry_points = '''
    [console_scripts]
    buck = buck.cli:main
    
  ''',
  zip_safe=False,
  author = 'Pleasant Tech',
  author_email = 'dummyware2020@gmail.com'
  
  
  
)