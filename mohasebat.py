def i_input(x):
    print(x, end="")
    str_var = input("")
    str_var2 = int(str_var)
    return str_var2


def f_input(x):
    print(x, end="")
    str_var = input("")
    str_var2 = float(str_var)
    return str_var2


while True:
    print("method 1) TWO PART \nmethod 2) NABEJAYI\nmethod\n")
    method = i_input("choose a method: ")
    if (method == 1) is True:
        a = f_input("a? ")
        b = f_input("b? ")
        fa = f_input(f"f({a})? ")
        fb = f_input(f"f({b})? ")
        n = i_input("number of proccess? ")
        print("  n\ta\tb\tF(a)\tF(b)\tXn\tF(Xn)\tF(a)*F(Xn)  ")
        print("-----\t-----\t-----\t-----\t---------\t-------------")
        for i in range(n):
            Xn = (a+b)/2
            FXn = f_input(f"f({Xn})?")
            t = FXn * fa
            print(f"  {i+1}\t{a}\t{b}\t{fa}\t{fb}\t{Xn}\t{FXn}\t{t}")
            if (t) < 0:
                b = Xn
                fb = FXn
            elif (t) > 0:
                a = Xn
                fa = FXn
    if (method == 2) is True:
        a = f_input("a?")
        b = f_input("b?")
        fa = f_input(f"f({a})?")
        fb = f_input(f"f({b})?")
        n = i_input("number of repeats?")
        for i in range(n):
            x = (((a*fb)-(b*fa))/(fb-fa))
            fx = f_input(f"f({x})?")
            print(
                f"a=({a}), b=({b}), f(a)=({fa}), f(b)=({fb}), x{i+1}=({x}), f(x{i})=({fx})\nf(a)*f(x{i}) = f({a})*f({x}) = {fa*fx}")

            if (fa*fx) < 0:
                b = x
                fb = fx
            elif (fa*fx) > 0:
                a = x
                fa = fx
