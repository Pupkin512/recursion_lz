def delit(a):
    b = []
    for i in range(1, a):
        if a % i == 0:
            b.append(i)
    return b
def summa(b, c):
    if c == sum(b):
        print('True')
    else:
        print('False')
def main():
    c = int(input('Введите число: '))
    b = delit(c)
    print(b)
    summa(b, c)

if __name__ == '__main__':  
    main()


