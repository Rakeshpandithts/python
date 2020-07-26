# get input Donor or Recipient
donordetailslist = []
recipientDetailslist = []

def getuserdetails():
    while True:
        user = input("Are you a donor or Recipient: ")
        print(user)

        if (user == 'donor'):
            print('user is donor')
            donorDetails = {'Blood_group' : input("enter blood group = "),
                            'City': input('enter city = '),
                            'name': input('enter name = '),
                            'phone': input('enter phone no = ')}
            donordetailslist.append(donorDetails) 
            print(donordetailslist)        
            
        else: 
            print('user is Recipient')
            recipientDetails = {'Blood_group' : input("enter blood group = "),
                                'City': input('enter city = ')}
            recipientDetailslist.append(recipientDetails)
            if(recipientDetails['Blood_group'] == donordetailslist['Blood_group'] ):
                print('Blood group matched')
            else:
                print('Blood group matched')
            

        

getuserdetails()

