from setuptools import setup

setup(name='netdisco',
      version='0.1',
      description='Discover devices on your local network',
      url='http://github.com/balloob/netdisco',
      author='Paulus Schoutsen',
      author_email='Paulus@PaulusSchoutsen.nl',
      license='MIT',
      install_requires=['requests>=2.0', 'zeroconf>=0.17.2'],
      packages=['netdisco'],
      zip_safe=False)
