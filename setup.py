from setuptools import setup, find_packages

setup(name='netdisco',
      version='1.3.1',
      description='Discover devices on your local network',
      url='https://github.com/home-assistant/netdisco',
      author='Paulus Schoutsen',
      author_email='Paulus@PaulusSchoutsen.nl',
      license='Apache License 2.0',
      install_requires=['requests>=2.0', 'zeroconf>=0.19.1'],
      packages=find_packages(exclude=['tests', 'tests.*']),
      zip_safe=False)
