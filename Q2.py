if __name__ == '__main__':
    x = input()
    x = int(x)
    cnt = 0
    for i in range(x):
        x_out = i+1
        if ((x_out%3) == 0) & ((x_out%5) == 0) :
            cnt = cnt+1
        if ((x_out%3) != 0) & ((x_out%5) != 0):
            cnt = cnt+1

    print(cnt)