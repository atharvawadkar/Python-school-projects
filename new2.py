def outer_fun():
    outer_var=10
    def inner_fun():
        inner_var=20
        print("outer varaiable",outer_var)
        print("Inner varoable",inner_var)
    inner_fun()
outer_fun()
print("outer variable",outer_var)
print("inner variable",inner_var)
