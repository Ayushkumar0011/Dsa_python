import math as m
class ReverseNumber:
    def reverse(self,num):
        rev=0
        while(num >0):
            rev= rev * 10 + num % 10
            num = num // 10
        return rev

#  O(n)
if __name__ =='__main__':
    n=int(input('Enter the value: \n '))
    r=ReverseNumber()
    print(r.reverse(n))
       


