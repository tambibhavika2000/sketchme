import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sketchme",
    version="1.13",
    description="Converts a real world images into Pencil SKETCH",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Bhavika Tambi",
    author_email="tambibhavika2000@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["sketchit"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "sketchit=sketchit.__main__:main",
        ]
    },
)