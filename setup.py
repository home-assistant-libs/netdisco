"""Setup file for netdisco."""
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="netdisco",
    version="3.0.0",
    description="Discover devices on your local network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/home-assistant/netdisco",
    author="Paulus Schoutsen",
    author_email="Paulus@PaulusSchoutsen.nl",
    license="Apache License 2.0",
    install_requires=["requests>=2.0", "zeroconf>=0.30.0"],
    python_requires=">=3",
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Topic :: Home Automation",
        "Topic :: System :: Networking",
    ],
)
