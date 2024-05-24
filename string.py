# haystack="sadbutasd"
# needle="sad"
# result=haystack.find(needle)

# print(result)


# haystack="leetcode"
# needle="leeto"
# code=needle.find(haystack)
# print(code)


# def code(haystack,needle):
# 	result=haystack.find(needle)
# 	return result
# print(code("sadbutasd","sad"))


# def leetcode(haystack,needle):
# 	cat=haystack.find(needle)
# 	return cat
# print(leetcode("leetcode","leeto"))

# print(leetcode("sadbutasd","sad"))



# def addOne(arr):
# 	arr[-1] = arr[-1] + 1

# 	return arr

# arr = [90,2,3,4,5]

# print(addOne(arr))



# def  addStringNumberically(str1, str2):

# 	return str(int(str1) + int(str2) )

# print(addStringNumberically("33","55"))



# def changeChar(strr):
# 	result=""
# 	for x in strr:
# 		if x.isupper():
# 			result=result + x.lower()
# 		else:
# 			result=result + x.upper()

# 	return result
# print(changeChar("WTFFsufya"))

# list1=[1,3,54,33]
# list2=[1,3,11]

# def code(list1,list2):
# 	result=[]
# 	for i in list1:
# 		if i in list2:
# 			result.append(i)
# 	return result
# print(code(list1,list2))


# def steairs(steps):
# 	if steps % 2 == 0:
# 		return int(steps/2)
# 	total_steps = int((steps - 1)/2)
# 	return f"steps:{total_steps} , and 1 steair"

# print(steairs(20))



# def devidearr(arr):
# 	arr1=[]
# 	arr2=[]
# 	for i in range(len(arr)):
# 		if i % 2 == 0:
# 			arr1.append(arr[i])

# 		else:
# 			arr2.append(arr[i])
# 	return f" new lists are { arr1} and {arr2}"
# print(devidearr([1,3,5,4,6,57,5,"pakistan","source"]))




def minimunvalue(arr):
	first=arr[0]
	
	for i in range(len(arr)):
		if arr[i]<first:
			first=arr[i]
	return first
print(minimunvalue([33,66,33,4,6,5]))



