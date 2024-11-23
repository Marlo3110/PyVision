#from setuptools import setup, find_packages 
import setuptools
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setuptools.setup(
  name='PyVision',
  version='0.0.1',
  description='A basic library to create easy GUI. Also useable to create games or other visualization',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='https://upload.pypi.org/legacy',  
  author='Marlo3110',
  author_email='marlo3110.001@Gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='GUI, UI, Visualization', 
  packages=setuptools.find_packages(),
  install_requires=[''] 
)