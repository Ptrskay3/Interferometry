try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


MAJOR = 0
MINOR = 0
MICRO = 13
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


setup(
    name="pysprint",
    version=VERSION,
    author="Péter Leéh",
    author_email="leeh123peter@gmail.com",
    description="Spectrally refined interferometry for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ptrskay3/PySprint",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics"        
    ],
    install_requires=[
        'numpy',
        'scipy', 
        'matplotlib',
        'pandas', 
        'lmfit'
      ],
)
