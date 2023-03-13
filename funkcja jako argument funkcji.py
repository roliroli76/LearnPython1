def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(how,objs):
    for obj in objs:
        print(how(obj))

objs = [1,2,5,10,20,50]
print(generate_values(double, objs))
print(generate_values(square, objs))
print(generate_values(negative, objs))
print(generate_values(div2, objs))