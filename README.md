# Matrix7

a library in pure python3 that allows you to use matrices and vectors easily

## Setup

```
sudo pip install matrix7
```

## How to use

#### Declarations

```python
from matrix7 import Matrix, Vector

a = Matrix([
    [1,2,3,4,5,6,7],
    [101,102,103,104,105,106,107],
    [201,202,203,204,205,206,207],
])

b = Vector( [2,4,7,9] )

c = Vector( [2,4,7,9] , transpose = True )
```

#### printing

- `print(a)` :

```text
|   1.00   2.00   3.00   4.00   5.00   6.00   7.00 |
| 101.00 102.00 103.00 104.00 105.00 106.00 107.00 |
| 201.00 202.00 203.00 204.00 205.00 206.00 207.00 |
```

- `print(b)` :
  
```text
|   2.00 |
|   4.00 |
|   7.00 |
|   9.00 |
```

- `print(c)` :
```text
|   2.00   4.00   7.00   9.00 |
```

#### properties

```python
a.size    # (nb lines, nb cols)
a.trace   # only for nxn matricies
a.raw     # matrix or vector in normal python list format
a.gravity # only for vectors
```

#### operations

- normal python operations are used
- Matrix or Vector object is returned
- regular matrix/vector calculation rules apply

```python
c = a + b
c = a - b
c = a * b
```

#### trasponse of matrix or vector

```python
a.transpose()
```

#### generation

```python
# vector containing 6 threes
vect = Vector.gen(6, 3)

# 3x4 matrix of zeroes
mat = Matrix.gen(3, 4, 0)
```

#### navigation

```python
# matrix line 0 (Vector) or vector element (int, float ..etc)
a[0]
# matrix column 0 (Vector)
a(0)
# matrix element (0,0) (int, float ..etc)
a[0][0]
```
