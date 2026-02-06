list1  = ['N', 'm', 'l']
list2 = ['N', 'm', 'l']
list3 = ['N', 'm', 'l']
map1= [list1, list2, list3 ]
treasuremark = input ("input the number like b3 where you want to bury you treasure ")
letter = treasuremark[0].lower()
number = int(treasuremark[1])
abc= [ 'a','b', 'c']
integer= ['1', '2', '3']
num = integer.index(str(number))
char= abc.index(letter)
map1[char][num] = 'X'
print(f"Your treasure is buried at\n{map1[0]}\n{map1[1]}\n{map1[2]}\n ")
