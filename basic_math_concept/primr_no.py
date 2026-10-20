from math import sqrt
class Divisons:
    def all_divisons(self,num):
        # linear approach  O(n)
        for i in range(1,num+1):
            if num % i == 0 :
                print(num)


    def all_divisons_factor(self,num):
        #  O(sqrt(n))
        l=[]
        for i in range(1,int(sqrt(num) + 1)):
            if num % i == 0:
                if i not in l:
                    l.append(i)
                if int(num / i ) not in l:
                    l.append(int(num/i))
        print(sorted(l)) #O(n log(no of factors))




if __name__ =='__main__':
    n=int(input('Enter the value'))
    if n:    
        d=Divisons()
        d.all_divisons(n)
        d.all_divisons_factor(n)
        
