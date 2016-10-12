from setuptools import setup, find_packages

setup(name='netdisco',
      version='0.7.3',
      description='Discover devices on your local network',
      url='https://github.com/home-assistant/netdisco',
      author='Paulus Schoutsen',
      author_email='Paulus@PaulusSchoutsen.nl',
      license='MIT',
      install_requires=['netifaces>=0.10.0', 'requests>=2.0',
                        'zeroconf==0.17.6'],
      packages=find_packages(),
      zip_safe=False)
