from setuptools import setup, find_packages

setup(name='netdisco',
      version='0.6.7',
      description='Discover devices on your local network',
      url='http://github.com/balloob/netdisco',
      author='Paulus Schoutsen',
      author_email='Paulus@PaulusSchoutsen.nl',
      license='MIT',
      install_requires=['netifaces>=0.10.0', 'requests>=2.0', 'zeroconf==0.17.5'],
      packages=find_packages(),
      zip_safe=False)
