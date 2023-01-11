def minion_game(string):
    
    Vocales = 'AEIOU'
    KevPoints  = 0
    StuPoints  = 0
    
    size = len(string)
    
    for i in range(size):
        if (string[i] in Vocales):
            KevPoints += (size-i)
        else:
            StuPoints += (size-i)
        
    if KevPoints > StuPoints:
       print("Kevin", KevPoints)
    elif StuPoints > KevPoints:
        print("Stuart", StuPoints)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)