n = int(input("Input your number: "))
w = len("{0:b}".format(n))
print("{dec:{width}} {oct:{width}} {hex:{width}} {bin:{width}}".format(dec="Decimal", oct="Octal", hex="Hexadecimal", bin="Binary", width=w))
for i in range(1, n + 1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
