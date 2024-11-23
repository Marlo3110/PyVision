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
  name='PythonVisualization',
  version='0.0.1',
  description='A basic library to create easy GUI. Also useable to create games or other visualization',
  #long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
  url='https://github.com/Marlo3110',
  download_url = 'https://github.com/Marlo3110/PythonVisualization/blob/main/pythonvisualization-0.0.1.tar.gz',  
  author='Marlo3110',
  author_email='marlo3110.001@Gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='GUI, UI, Visualization', 
  packages=setuptools.find_packages(),
  install_requires=['screeninfo'] 
)