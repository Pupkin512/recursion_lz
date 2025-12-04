def treugolnik_pascalya(a):                                
    if a == 0:
        return [1]
    else:
        ryad = [1]
        pred_ryad = treugolnik_pascalya(a - 1)
        for i in range(len(pred_ryad) - 1):
            ryad.append(pred_ryad[i] + pred_ryad[i + 1])    
        ryad.append(1)
        return ryad
def main():                                       
    a = int(input('Введите число : '))
    for i in range(a):
        print(treugolnik_pascalya(i))

if __name__ == '__main__':                              
    main()



