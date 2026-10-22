class Pallindrome:
    def pallindrome(self,message):
        l=0
        r=len(message)-1
        return self.rev(l,r,message)
    def rev(self,l,r,message):
        if l >= r:
            return True
        if message[l] != message[r]:
            return False
        return self.rev(l+1,r-1,message)

if __name__ =='__main__':
    st=input('Enter the text: \n ')
    p=Pallindrome()
    print(p.pallindrome(st))