# ------------------------------- Introduction ------------------------------- #
# ---------------------------------------------------------------------------- #
#                                   typecode
#                                 #i-integer,f-float(4),d-float(8),unicode-(2)
# ---------------------------------------------------------------------------- #
import array as arr  # importing  array package
newarray = arr.array('i', [1, 2, 3, 4])  # Specifying type of array
print(newarray)
for i in range(len(newarray)):  # iteratiing through loop
    print(newarray[i], end=",")
# ---------------------------- accessing elements ---------------------------- #
# list-->array

x = list(range(1, 100))  # created list
print(x)
listarray = arr.array('i', x)  # list to array
print('listed array', listarray)
print(newarray[3])  # using index values
# ---------------------------- length of an array ---------------------------- #
print(len(newarray))
# ------------------------------ Adding elements ----------------------------- #
# append()(single element at end)
newarray.append(7)
print(newarray)
# extend()(multiple elements at end)
newarray.extend([7, 90, 34])
# insert()(element at specified position)
newarray.insert(5, 87)
print(newarray)
# ------------------------------ remove elemnts------------------------------ #
# pop(pos)(returns popped value,one or no parameter(lastvalue),parameter is position)
print(newarray.pop())
# remove()(takes param element to be removed)first occurence
newarray.remove(7)
print(newarray)
# ---------------------------- Array Concatenation --------------------------- #
# ---------------------------------------------------------------------------- #
#                               using + operator
#                               should have same datatype(both arrays)
# ---------------------------------------------------------------------------- #
secondnewArray = arr.array('i', [4, 5, 3, 21, 34, 67])
resultarray = arr.array('i')
resultarray = newarray+secondnewArray
print('added arrray is')
for i in range(len(resultarray)):
    print(resultarray[i], end=' ')
# ------------------------------- slicing array ------------------------------ #
# ---------------------------------------------------------------------------- #
#                               [0:3]
#                               using : operator
#                              includes starting(0) and excludes last(till 2)
# ---------------------------------------------------------------------------- #
print(resultarray[0:3])
# to reverse
print('reversed', resultarray[::-1])
# --------------------------- loop through array --------------------------- #
for x in resultarray:
    print(x, end=',')
for x in resultarray[2:6:2]:  # along with indexing
    print(x, end=',')
# ------------------------------------- . ------------------------------------ #
# to check typecode
print(newarray.typecode)
# ------------------------------------- inserting element ------------------------------------ #
# insert(position,valuetoinsert)
newarray.insert(3, 1000)
print(newarray)
# append(value)-->this will be at end only
newarray.append(900)
print(newarray)
# ------------------------------ updating array ------------------------------ #
newarray[3] = 2500  # using index value
print(newarray)
# --------------------------------- searching -------------------------------- #
# index(value) we can know the index of the value
address = newarray.index(2500)
print(address)
valueeeee = newarray[address]
print(valueeeee)

# ---------------------------------- sorting --------------------------------- #
# convert array to list
sort_array = newarray.tolist()
sort_array.sort()  # default ascending,reverse=True-->descending
sort_array.sort(reverse=True)
print(sort_array)



