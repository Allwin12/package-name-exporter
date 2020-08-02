# Package name exporter
This python package will let you export your installed packages to txt, pdf and xls format.
This package is the advanced version of the 

```python
pip freeze > requirements.txt
```

## Installation

* Install this package from pypi.org 

```python
pip install package-name-exporter
```
* clone this repo and run 

```python
python setup.py install
```

## Usage

This library helps you to export the installed packages into txt, xls and pdf format

* pdf format

```python
from package_name_exporter.exporter import PackageNameExporter

my_class = PackageNameExporter()
my_class.get_packages_list('pdf', 'filename.pdf')
```
