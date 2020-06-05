from setuptools import setup, find_packages

setup(name='shogun_live_api',
      version='1.2.1.109184h Beta',
      url='https://www.vicon.com',
      author='Vicon Motion Systems Ltd',
      author_email='support@vicon.com',
      packages=find_packages(),
      install_requires=['vicon_core_api'])
