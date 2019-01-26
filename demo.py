from matrix import Matrix, Vector

a = Matrix(
    [
        [1,7],
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


print(a.matrix) # all of the matrix in list format

b.vector = [1,2,6,8,9,7]

a().show() # all of the matrix in lists format
print(a(1,1)) # elem (1,1)

a(0).show() # all of line 0
a(None, 0).show() # all of column 0
print(b(4))

print(a.trace())
print(b.trace())

print(a.size())
print(b.size())