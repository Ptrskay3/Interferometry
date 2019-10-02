try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


MAJOR = 0
MINOR = 0
MICRO = 2
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

setup(
    name="interferometry",
    version=VERSION,
    author="Péter Leéh",
    author_email="leeh123peter@gmail.com",
    description="UI for spectrally refined interferometry",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ptrskay3/Interferometry",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Optics"
    ],
    install_requires=[
        'numpy',
        'scipy', 
        'matplotlib',
        'pandas', 
        'lmfit'
      ],


)
