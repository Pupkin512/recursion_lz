def main():
    def perestanovka(posledovatelnost):
        if len(posledovatelnost) == 0: 
            return [[]]
        vsevosmozhnie_perestanovki = [] 
        for i in range(len(posledovatelnost)): 
            one = posledovatelnost[i]
            ostatok = posledovatelnost[:i] + posledovatelnost[i+1:] 
            for a in perestanovka(ostatok): 
                vsevosmozhnie_perestanovki.append([one] + a)
        return vsevosmozhnie_perestanovki
    for i in perestanovka([1, 2, 3]): 
        print(i)
if __name__ == '__main__': 
    main()



