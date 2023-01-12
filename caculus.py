###روش انتگرال گیری به روش زوذنقه ای
print(" f(x)= x^3 - 3x -1 ")
def intf(x):
    y = ((((x^4)/4)-((3*(x^2))/2)-x))
    return y
def f_input(x):
    print(x, end="")
    y = float(input(""))
    return y
def f(x):
    y = ((((float(x)*float(x)*float(x)*float(x))/4)-((3*(float(x)*float(x)))/2)-float(x)))
    return y
a = f_input("The beginning of the integral interval? ")
b = f_input("The end of the integral interval? ")
n =  int(input("n? "))
h = abs((b-a)/(2*n))
Function = f"Integral[{a},{b}]f(x)"
t=f(a)
i = a
print(f"T({h}) = {h}/2 (", end="")
while i <= b:
    if i%2 != 0:
        t += 2*f(a + (h*i))
        i+=h
    elif i%2 == 0:
        t += f(a + (h*i))
        i+=h
    a+=(h*i)

    print(f"+{t}", end="")
print(f") = {t}")