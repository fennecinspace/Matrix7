from matrix7 import Matrix, Vector

a = Matrix([
    [1,7],
    [3,4],
])

b = Matrix([
    [1,5],
    [10,1],
])

c = Vector( [2,4] )

d = Vector( [1,4] , transpose = True )


print(a,b,c,d)

# mat mat
print( a * b )

# mat vect
print( a * c )

# vect vect
print( c * d )
print( d * c )

# vect mat
print( d * a )


a_t = a.transpose()
print(a_t)


print( a - b )
print( a + b )

print( c - c )
print( d + c.transpose() + 100)

print( a.raw )
print( b.raw )
print( c.raw )
print( d.raw )

print(a[1][1]) # elem (1,1)

print(a[0])

print(a.trace)

print(a.size)

# a[1:2] ... etc