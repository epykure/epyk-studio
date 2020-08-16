"""
packaging module to install: python.exe -m pip install --upgrade setuptools wheel
to create the tar.gz: python.exe setup.py sdist
to create the weels: python.exe setup.py sdist bdist_wheel --universal
"""

import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

def install_required():
  return [line for line in open('requirements.txt')]

setuptools.setup(
    name="epyk_studio",
    author="epykure",
    version="0.0.8",
    author_email="smith.pyotr@gmail.com",
    description="A simple way to create rich interactive websites from Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/epykure/epyk-studio",
    project_urls={
        "Documentation": "http://www.epyk-studio.com",
        "Code": "https://github.com/epykure/epyk-studio",
        "Issue tracker": "https://github.com/epykure/epyk-studio/issues"
    },
    package_data={'epyk_studio': [os.path.join('static', 'images', '*')]},
    entry_points={"console_scripts": [
      "epyk_studio = epyk_studio.core.cli.cli_pages:main", # For common quick page transformation
    ]},
    packages=setuptools.find_packages(),
    install_requires=install_required(),
    python_requires=">=2.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: IronPython",
    ],
)