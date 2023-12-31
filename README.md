# pyplyr

An experimental data wrangling toolkit for Python, built on Numpy and
inspired by dplyr.

## Installation

The development version of pyplyr can currently be installed from GitHub
using pip:

``` bash
python -m pip install git+https://github.com/wurli/pyplyr
```

## Usage:

### DataFrame creation:

``` python
import numpy as np
from pyplyr import DataFrame

df = DataFrame(
    origin=['spain', 'england', 'colombia', 'spain'],
    fruit=['apple', 'apple', 'banana', 'pear'],
    n_units=[1, 1, 3, 2],
    unit_price=[3, 4, 3, 5]
)

df
```

    # A DataFrame: 4 x 4
      origin   fruit    n_units unit_price
      <str256> <str192> <int64>    <int64>
    0 spain    apple          1          3
    1 england  apple          1          4
    2 colombia banana         3          3
    3 spain    pear           2          5

### Adding columns

To make use of an existing column, you need to use a lambda function
with an argument which shares that column’s name. Columns can be created
and used within the same call. The `_by` keyword can be used to apply
operations with a *grouping*:

``` python
df1 = df.mutate(
    origin=lambda origin: np.char.capitalize(origin),
    total_price=lambda n_units, unit_price: 
        unit_price * n_units,
    price_pct_of_total_by_origin=lambda total_price:
        total_price / total_price.sum(),
    _by='origin'
)

df1
```

    # A DataFrame: 4 x 6
      origin   fruit    n_units unit_price total_price price_pct_of_total_by_origin
      <str256> <str192> <int64>    <int64>     <int64>                    <float64>
    0 Spain    apple          1          3           3          0.23076923076923078
    1 England  apple          1          4           4                          1.0
    2 Colombia banana         3          3           9                          1.0
    3 Spain    pear           2          5          10           0.7692307692307693

### Summarising results:

Values can be summarised to a single row, and grouping can also be
applied:

``` python
df2 = df1.summarise(
    n_units=lambda n_units:
        n_units.sum(),
    mean_price=lambda total_price, n_units:
        total_price.sum() / n_units,
    _by='origin'
)

df2
```

    # A DataFrame: 3 x 3
      origin   n_units        mean_price
      <str256> <int64>         <float64>
    0 Spain          3 4.333333333333333
    1 England        1               4.0
    2 Colombia       3               3.0

## Subsetting and arranging rows

Rows can be subsetted using the `filter()` method, and reordered using
the `arrange()` method. This also demonstrated how methods can be
chained:

``` python
df3 = df2 \
    .filter(lambda n_units: n_units > 1) \
    .arrange('origin')

df3
```

    # A DataFrame: 2 x 3
      origin   n_units        mean_price
      <str256> <int64>         <float64>
    0 Colombia       3               3.0
    1 Spain          3 4.333333333333333

## Motivation

- I thought this would be a good way to learn more about Python.

- While pandas is extremely powerful, I don’t find it to be particularly
  user-friendly. I wanted to think about what my ideal alternative
  syntax might look like.

- Compared to many data toolkits (e.g. pandas or R’s data.table), dplyr
  doesn’t play so many tricks under the surface to speed things up for
  you, in particular it doesn’t index tables or do ‘in place’
  transformations. However, at the expense of speed you get a simple and
  intuitive syntax which makes working with data enjoyable. This project
  is a place for me to play around with ideas for what this might look
  like in python.

## Similar work

- [siuba](https://github.com/machow/siuba) is a very cool attempt at a
  dplyr implementation in python:

  - siuba implements ‘siu expressions’ - a sophisticated system for
    performating calculations using special syntax - and overloads `>>`
    as a pipe operator. In contrast to this, I’d like to build something
    which feels closer to idiomatic Python.

- [dplython](https://pythonhosted.org/dplython/) attempts to implement
  dplyr syntax on top of a pandas backend.

- [datar](https://github.com/pwwang/datar) attempts to implement dplyr
  syntax on top of multiple backends, and also provides some
  ggplot2-style plotting functionality.
