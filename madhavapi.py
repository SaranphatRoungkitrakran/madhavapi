class Madhava:
    
    def __init__(self , num1):
        self.a = 'I will survive'
        self.inputnumber = num1
        self.countnumber = 0
        self.pinumber = 0
        while True:
            self.pinumber += pow( -1, self.countnumber )/(2*self.countnumber+1 )
            if self.countnumber == self.inputnumber:
                self.pinumber *= 4
                break
            else:
                self.countnumber +=1
                
        print(self.pinumber)
        
if __name__ == '__main__':
    test=Madhava(1)
    

