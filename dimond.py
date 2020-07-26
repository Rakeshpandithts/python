# x = 1
# y =6
def diamond1(x,y):
    for i in range (x, y):
        print(' ' *(y-i))
        print('#' *+x)
        x = x+1

# def diamond2(x,y):
#     for i in range (x, y):
#         print(" " *(i+1))
#         print("#" *(y+1))
#         y = y+1

# diamond1(x,y)
# diamond2(x,y)


n = 5
def pyramid(n):
    for i in range(1,n+1):
	print ((n-i)*' '+i*'# ')

def downPyramid(n):
    for i in range(1, n+1):
        print(+i*'# '(n-i)*' ')

pyramid(n)
downPyramid(n)