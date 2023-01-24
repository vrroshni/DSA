def get_square(numbers):
    result=[]
    for n in numbers:
        result.append(n*n)
    return result
    # return [n*n for n in numbers]#list comprehension




# can also be return as 
#return [n*n for n in numbers]

n=[1,3,4,5]
print(get_square(n))