class Recursion:
    def print_name_multiple_times(self,name,no):
        if no == 0:
            return
        else:
            print(name)
            self.print_name_multiple_times(name,no-1)

    def print_linearly(self,num):
        if num == 1:
            print(1)
        else:
            self.print_linearly(num-1)
            print(num)

    def print_reverse(self,num):
        if num == 1:
            print(1)
        else:
            print(num)
            self.print_reverse(num-1)
    def sum_of_n_number(self,num):
        if num == 0:
            return 0
        return num+self.sum_of_n_number(num-1)
    def factorial(self,num):
        if num == 1:
            return 1
        return num * self.factorial(num-1)

if __name__ =='__main__':
    n=int(input('Enter the value: \n '))
    # name=input('Enter the name:\n')
    r=Recursion()
    # r.print_name_multiple_times(name,n)
    # r.print_linearly(n)
    # r.print_reverse(n)
    print(r.sum_of_n_number(n))
    print(r.factorial(n))
