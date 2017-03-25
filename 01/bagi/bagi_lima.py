def bagi_lima(a):
    result = a / 5
    return result

if __name__ == '__main__':
    a = int(input().strip())
    bagi = bagi_lima(a)
    print(bagi)
