import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="trix",
    version="0.0.1",
    author="Manu Pascual",
    author_email="mpascual@stackscale.com",
    description="My first pypi package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitbub.com/blabla/blabalba",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
