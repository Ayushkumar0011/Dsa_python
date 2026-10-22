class Subsequences:
    def print_subsequences(self,ind:int,ds:list,arr:list,n:int):
        if ind == n:
            print(ds)
            return
        ds.append(arr[ind])
        self.print_subsequences(ind+1,ds,arr,n)
        ds.pop()
        self.print_subsequences(ind+1,ds,arr,n)

    def print_subsequences_with_sum_k(self,ind:int,ds:list,arr:list,n:int,cur:int,k:int):
        if ind == n:    
            if cur == k:
                print(ds)
                return
            return
        ds.append(arr[ind])
        cur=cur+arr[ind]
        self.print_subsequences_with_sum_k(ind+1,ds,arr,n,cur,k)
        ds.pop()
        cur=cur-arr[ind]
        self.print_subsequences_with_sum_k(ind+1,ds,arr,n,cur,k)

    


p=Subsequences()
# p.print_subsequences(0,[],[3,1,2],3)
p.print_subsequences_with_sum_k(0,[],[1,2,3,4,5],5,0,5)