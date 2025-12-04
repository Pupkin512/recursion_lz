def main():
    def Evklid(a,b):                       
        if b == 0:
            return a
        else:
            return Evklid(b, a % b)                         
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    print('НОД этих чисел:', Evklid(a, b))
if __name__ == "__main__":          
    main()

