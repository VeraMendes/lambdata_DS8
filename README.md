# lambdata_DS8

## about this test package

This package was created in order to have useful functions to apply in the data science world!
It is in constant construction and it is open source.

## how to install
Go to [TestPyPI API](https://test.pypi.org/project/lambdata-veramendes/) where the package is hosted. Install the last version available for this package.

e.g.: `pip install -i https://test.pypi.org/simple/ lambdata-veramendes`

## how to use
Use `import lambdata_veramendes` to import the module available at the moment.

## an example of use:

```
>>> RANDINT
    0
0  33
1  31
2  58
3  50
4  41
5   9
6  82
7  28
8  26
9  53
>>> from lambdata_veramendes import Date
>>> Date
<class 'lambdata_veramendes.Date'>
>>> date = Date()
>>> date()
>>> date.get_year()
1900
>>> date.get_month()
1
>>> date.get_day()
1
>>> from lambdata_veramendes import increment
>>> increment(3)
4
