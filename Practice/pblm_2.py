# def find_result(prices,eps,index):
#     # pe=prices[index]/eps[index]
#     return prices[index]/eps[index]
# this have o(1) complexty
 
num=[1,2,3,1,43,5,2]

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]==num[j]:
            print(num[i],"is a duplicate")
            break
        
duplicates=[]       
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if(num[i]==num[j]):
            duplicates.append(num[i])
            break
        
print(duplicates)