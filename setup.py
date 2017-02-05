from setuptools import setup, find_packages

setup(name='netdisco',
      version='0.8.1',
      description='Discover devices on your local network',
      url='https://github.com/home-assistant/netdisco',
      author='Paulus Schoutsen',
      author_email='Paulus@PaulusSchoutsen.nl',
      license='Apache License 2.0',
      install_requires=['netifaces>=0.10.0', 'requests>=2.0',
                        'zeroconf==0.17.6',
                        'ipaddress==1.0.18; python_version < "3"'],
      packages=find_packages(),
      zip_safe=False)
