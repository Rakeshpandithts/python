# import re

# # string = '-ganesh /new # ---///123-'

# # newstring = re.findall(r'\w+', string) 

# # print(newstring)


# # newstring1 = str(' '.join([str(elem) for elem in newstring])).replace(" ", "_")

# # print (newstring1)
# string = 'donol__trump'

# string = string.replace("__","_")

# print(string)



file_name = 'patient_1234'


if 'case_' in file_name:
    print('Yes')

else:
    print('NO')