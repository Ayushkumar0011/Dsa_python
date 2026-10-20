from math import sqrt
class GCD:
    # O(min(n1,n2))
    def gcd_no(self,n1,n2):
        l=n1 if n1 > n2 else n2
        s=n1 if n1 < n2 else n2
        n=1
        for i in range(s+1,1,-1):
            if l % i == 0 and s % i == 0:
                return i
        return n
    def gcd_euclidean(self,a,b):
        # O(log(min(a,b)))
        if a == 0:
            return b
        elif b == 0:
            return a
        elif a > b:
            return self.gcd_euclidean(b,a%b)
        else:
            return self.gcd_euclidean(a,b%a)
        

if __name__ =='__main__':
    n1=int(input('Enter the first number'))
    n2=int(input('Enter the second number'))
    if n1 and n2:    
        g=GCD()
        print(g.gcd_no(n1,n2))
        print(g.gcd_euclidean(n1,n2))
        

            