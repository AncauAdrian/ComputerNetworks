def prim(x):

    if x == 1 or x == 2:
        return True

    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False

    return True


def sequence(position):
    if position == 1:
        return 1

    count = 1
    n = 1

    while True:
        n += 1
        copy = n

        if prim(n):
            count += 1
            if count == position:
                return n
        else:
            for i in range(2, copy // 2 + 1):
                if copy % i == 0:
                    count += 1
                while copy % i == 0:
                    copy = copy // i

                if count == position:
                    return i


while True:
    pos = int(input("---> "))
    print(str(sequence(pos)))