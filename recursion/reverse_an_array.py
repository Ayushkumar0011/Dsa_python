class Reverse:
    def reverse_an_arr(self,arr:list[int]):
        l=0
        r=len(arr)-1
        print(self.rev(l,r,arr))
    def rev(self,l,r,arr):
        if l >= r:
            return arr
        temp=arr[l]
        arr[l]=arr[r]
        arr[r]=temp
        return self.rev(l+1,r-1,arr)

l=[1,2,3,4,5,6,7,8,9,10]
r=Reverse()
r.reverse_an_arr(l)