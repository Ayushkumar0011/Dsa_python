class Fibonnaci:
    def fib(self,n):
        if n <= 1:
            return n
        return self.fib(n-1)+self.fib(n-2)

if __name__ =='__main__':
    n=int(input('Enter the value: \n '))
    f=Fibonnaci()
    print(f.fib(n))