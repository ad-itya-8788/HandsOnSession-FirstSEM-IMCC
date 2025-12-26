def toh(n, a, b, c):
    if n == 1:
        print("Move Disk 1 from", a, "to", c)
        return
    toh(n-1, a, c, b)
    print("Move Disk", n, "from", a, "to", c)
    toh(n-1, b, a, c)
toh(3, 'A', 'B', 'C')
