
# Interferometry [2019]
[![Build Status](https://travis-ci.org/Ptrskay3/Interferometry.svg?branch=master)](https://travis-ci.org/Ptrskay3/Interferometry)



Interferometry is a UI for interferogram evaluation. Under construction.
I will add an advanced description later on. 

# Lastest upgrades:
  - Added autofit for CFF method, it will be improved later
  - Eval. methods are improved
  - Windows remember their last state, they open as they were closed
  - Added Settings panel for calibration
  - Added SPP Panel

### Known issues
* SPP Panel data storage should be rewritten
* Evaluation methods still performing bad
* The data loading AI sometimes produces unexpected results, currently being reviewed.
* There might be unnecessary imports
* Some buttons has no effect yet.


### To-do list

* ERROR HANDLING!
* Selectable units
* Possible performance enhancement by improving algorithms
* Possible new data manipulating features + new options for existing ones


### Installation

Interferometry requires [Python 3](https://www.python.org/downloads/) to run.

Please install the following packages:
* [PyQt5](https://pypi.org/project/PyQt5/)
* numpy, scipy, matplotlib, pandas
With command line:
```sh
$ pip install PyQt5
$ pip install numpy
$ pip install scipy
$ pip install pandas
$ pip install matplotlib
```
or conda run:
```sh
conda install -c dsdale24 pyqt5
```
Optional packages:
* [lmfit](https://lmfit.github.io/lmfit-py/), numdifftools

With command line:
```sh
$ pip install lmfit
$ pip install numdifftools
```
or conda run:

```sh
conda install -c conda-forge lmfit
or conda install -c conda-forge/label/gcc7 lmfit
or conda install -c conda-forge/label/broken lmfit
or conda install -c conda-forge/label/cf201901 lmfit 

conda install -c omnia numdifftools
```

## To Run
Run main.py
