class Extraction_of_digit:
    def extract(self,num):
        while(num > 0 ):
            print(num % 10)
            num=num // 10
# O(n)



if __name__ =='__main__':
    n=int(input('Enter the value'))
    if n:
        e=Extraction_of_digit()
        e.extract(n)


