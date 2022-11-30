inp1 = input("First Number: ")
inp2 = input("Second Number: ")
inp3 = input("Third Number: ")

def sum_number_parts(s):
    while len(s) != 1:
        s = str(sum(map(int, list(s))))

    return s

print (int(sum_number_parts(inp1)) + int(sum_number_parts(inp2)) + int(sum_number_parts(inp3)))


