from math import sqrt
class Prime:
    def prime_no(self,num):
        # linear approach  O(n)
        if num <= 1:
            return False
        for i in range(2,num):
            if num % i == 0 :
                return False
        return True


    def prime_with_sqrt(self,num):
        #  O(sqrt(n))
        if num <= 1:
            return False
        for i in range(2,int(sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True




if __name__ =='__main__':
    n=int(input('Enter the value'))
    if n:    
        p=Prime()
        print(p.prime_no(n))
        print(p.prime_with_sqrt(n))
