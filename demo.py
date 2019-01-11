from matrix import Matrix, Vector

a = Matrix(
    [
        [1,2],
        [3,4],
    ]
)


a.show()

b = Vector( [2,4] )

c = Vector( [1,4] , transpose = True )
c.show()

x = a.mul(b)

y = b.mul(c)

a_t = a.transpose()
a_t.show()


i = Matrix(
    [
        [1,3],
        [1,2],
    ]
)
i.show()

j = Matrix(
    [
        [100,0],
        [10,5],
    ]
)
j.show()


h = i.sub(j)
h.show()

h = i.add(j)
h.show()


print(a.matrix) # all of the matrix in lists format

b.vector = [1,2,6,8,9,7]

print(a()) # all of the matrix in lists format
print(a(1,1)) # elem (1,1)

print(a(0)) # all of line 0
print(a(None, 0)) # all of column 0
print(b(4))