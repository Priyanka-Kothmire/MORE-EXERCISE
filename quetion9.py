num=int(input("enter the number :"))
rem=sum=0
num_digit=list(str(num))
# n=num
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
if num%sum==0:
    print(num_digit,"it is the harashad number")
else:
    print(num_digit,"it is not harshad number")






