a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
c = [8, 9, 10, 11]
 
# mydict = {}


# mydict['medilenz'] = a
# mydict['Bifulco'] = b
# mydict['medilenz_additional'] = c

# mydict['medilenz'][1] = 45
# print(mydict['medilenz'])

# # for i in mydict['medilenz']:
# #     print(i)

# for val in mydict['Bifulco']: 
#     print(val)

# for i in mydict:
#     print(i)
#     for j in mydict[i]:
#         print(j)
case_name =  "Bell Mitchell "  
if case_name.find(',')!=-1:
            case_name_list  = case_name.split(',')
            casename = case_name_list[-1].strip()
            for each_str in case_name_list[:-1]:
                casename = casename+" "+each_str.strip()
                print('case_name')
                print (casename)
else:
    casename = case_name
    print('else {}'.format(casename))
       