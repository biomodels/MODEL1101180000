from setuptools import setup, find_packages

setup(name='MODEL1101180000',
      version=20140916,
      description='MODEL1101180000 from BioModels',
      url='http://www.ebi.ac.uk/biomodels-main/MODEL1101180000',
      maintainer='Stanley Gu',
      maintainer_url='stanleygu@gmail.com',
      packages=find_packages(),
      package_data={'': ['*.xml', 'README.md']},
    )