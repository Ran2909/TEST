'''
year=input('Please input the number of the year')
year=int(year)
if year%4==0 and year%100!=0 or year%400==0 :
    year=str(year)
    print(year+' is a leap year')
else:
    year = str(year)
    print(year+' is a common year')


a=15
if (a%2==0) ^ (a%3==0):
    print('can be zc by one and only one')
'''
#print(list(range(10)))
'''
a=''
while a!='exit' :
    a=input('input a digit:')
    try:
        print('even' if int(a)%2==0 else'odd')
    except:
        print('illegal digit')
'''
s1=input('input scores:').split()
s1=[int(x) for x in s1]
print(sum(s1)/len(s1))