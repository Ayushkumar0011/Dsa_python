import math as m
class CountDigit:
    def count(self,num):
        counter=0
        while(num > 0 ):
            counter+=1
            num=num // 10
        return counter
    # O(n)
    def countUsingLog(self,num):
        return int(m.log10(num)+1)
    # O(log10 n)
    def countUsingLen(self,num):
        return len(str(num))
    #  O(1)


if __name__ =='__main__':
    n=int(input('Enter the value'))
    if n:    
        c=CountDigit()
        print(c.count(n))
        print(c.countUsingLog(n))
        print(c.countUsingLen(n))
    


