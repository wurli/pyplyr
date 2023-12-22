# pyplyr

An experimental data wrangling toolkit for Python, built on Numpy and inspired by dplyr.

## Usage:


```python
import pyplyr as pyp

# Initialise a dataframe:
df = pyp.DataFrame(
    x=['foo', 'foo', 'bar'], 
    y=[1, 2, 3], 
    z=[3, 4, 5]
)

df
```




    A DataFrame: 3 x 3
      x             y       z
      <str96> <int32> <int32>
    0 foo           1       3
    1 foo           2       4
    2 bar           3       5




```python

# Columns can be mutated and replaced, or new columns can be created:
df2 = df \
    .mutate(
        y=lambda y: y*2
    ) \
    .mutate(
        _by='x',
        a=lambda z: z.max(),
        b=lambda a, y: a + y
    )

df2
```




    A DataFrame: 3 x 5
      x             y       z       a       b
      <str96> <int32> <int32> <int32> <int32>
    0 bar           6       5       5      11
    1 foo           2       3       4       6
    2 foo           4       4       4       8




```python
df3 = df2 \
    .filter(
        lambda a: a % 2 == 0,
        lambda b: b % 2 == 0
    )

df3
```




    A DataFrame: 2 x 5
      x             y       z       a       b
      <str96> <int32> <int32> <int32> <int32>
    0 foo           2       3       4       6
    1 foo           4       4       4       8



## Motivation

* I thought this would be a good way to learn more about Python.

* While pandas is extremely powerful, I don't find it to be particularly
  user-friendly. I wanted to think about what my ideal alternative syntax
  might look like.

* Compared to many data toolkits (e.g. pandas or R's data.table), dplyr doesn't
  play so many tricks under the surface to speed things up for you, 
  in particular it doesn't index tables or do 'in place' transformations.
  However, at the expense of speed you get a simple and intuitive syntax which
  makes working with data enjoyable. This project is a place for me to play
  around with ideas for what this might look like in python.

## Similar work

* [siuba](https://github.com/machow/siuba) is a very cool attempt at a dplyr
  implementation in python:
  *  siuba implements 'siu expressions' - a sophisticated system for performating
     calculations using special syntax - and overloads `>>` as a pipe operator. 
     In contrast to this, I'd like to build something which feels closer to 
     idiomatic Python.

* [dplython](https://pythonhosted.org/dplython/) attempts to implement dplyr 
  syntax on top of a pandas backend.

* [datar](https://github.com/pwwang/datar) attempts to implement dplyr syntax
  on top of multiple backends, and also provides some ggplot2-style plotting
  functionality.

