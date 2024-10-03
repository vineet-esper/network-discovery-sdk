from setuptools import setup, find_packages

setup(
    name="network_discovery_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "zeroconf",
    ],
    author="Keyur Maru",
    author_email="keyur@esper.io",
    description="A simple SDK for network service discovery using Zeroconf",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vineet-esper/network-discovery-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
