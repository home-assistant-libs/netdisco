from setuptools import setup, find_packages

setup(name='netdisco',
      version='0.4.2',
      description='Discover devices on your local network',
      url='http://github.com/balloob/netdisco',
      author='Paulus Schoutsen',
      author_email='Paulus@PaulusSchoutsen.nl',
      license='MIT',
      install_requires=['requests>=2.0', 'zeroconf>=0.17.4'],
      packages=find_packages(),
      zip_safe=False)
