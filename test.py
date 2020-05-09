def recursion(x0):
    global n

    l = 3.30

    x1 = l*x0*(1-x0)

    if n <= 400:

        print("n = ", n, "\nx1 = ", x1)

        n += 1

        return recursion(x1)
    else:
        return


x0 = 0.8

global n
n = 1

recursion(x0)
