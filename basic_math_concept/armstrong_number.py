class ArmStrong:
    def armstrong_number(self,num):
        c=self.count(num)
        total=0
        n=num
        while( n > 0):
            total = total + (n % 10) ** c
            n= n//10

        if total == num:
            return True
        else:
            return False
    def count(self,num):
        counter=0
        while(num > 0 ):
            counter+=1
            num=num // 10
        return counter


if __name__ =='__main__':
    n=int(input('Enter the value'))
    if n:    
        a=ArmStrong()
        print(a.armstrong_number(n))
        

