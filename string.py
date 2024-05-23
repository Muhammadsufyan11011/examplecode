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

list1=[1,3,54,33]
list2=[1,3,11]

def code(list1,list2):
	result=[]
	for i in list1:
		if i in list2:
			result.append(i)
	return result
print(code(list1,list2))





