n = 5
def pyramid(n):
    for i in range(1,n+1):
	print ((n-i)*' '+i*'# ')

pyramid(n)

def downPyramid(n):
    for i in range (1, n+1):
        print('# '*(n-i))mmm

downPyramid(n)