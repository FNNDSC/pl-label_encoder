
import sys
import os


# Make sure we are running python3.5+
if 10 * sys.version_info[0] + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")


from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   'label_encoder',
      # for best practices make this version the same as the VERSION class variable
      # defined in your ChrisApp-derived Python class
      version          =   '0.1',
      description      =   'An app to encode labels found in segmented brain MRI images',
      long_description =   readme(),
      author           =   'Sandip Samal',
      author_email     =   'sandip.samal@childrens.harvard.edu',
      url              =   'http://wiki',
      packages         =   ['label_encoder'],
      install_requires =   ['chrisapp', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['label_encoder/label_encoder.py'],
      license          =   'MIT',
      zip_safe         =   False
     )
