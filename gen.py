inp1 = input("First Number: ")
inp2 = input("Second Number: ")
inp3 = input("Third Number: ")


def sum_number_parts(s):
    while len(s) != 1:
        s = str(sum(map(int, list(s))))

    return int(s)


s1 = sum_number_parts(inp1)
s2 = sum_number_parts(inp2)
s3 = sum_number_parts(inp3)

print (sum_number_parts(str(s1 + s2 + s3)))
