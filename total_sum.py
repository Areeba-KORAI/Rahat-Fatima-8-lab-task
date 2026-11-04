def total(*args):
    total_sum = 0
    for i in args:
        total_sum = total_sum + i
    print("Sum =", total_sum)

total(10, 20, 30, 40)