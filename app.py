
friends = {}
amountToPay = {}
friendBalances = {}
totalAmount = 0
currentInput='dummy data'
amountPerPerson = 0

while(currentInput != ''):
    currentInput = input('Name: ')
    if currentInput != '':friends[currentInput]=0

print('\n')

for friend in friends:
   friends[friend]= int(input(friend + ' Rs.'))
   totalAmount+=friends[friend]

amountPerPerson =int( totalAmount/len(friends))
print(f'\ntotal = {totalAmount}')
print(f'per person = {amountPerPerson}')


# print('\n\n')
for friend in friends:
    toPay = friends[friend]-amountPerPerson
    # print(f'{friend} {toPay}')
    amountToPay[friend]=toPay

print('\n')
# print(amountToPay)

# print('\n')
# print(amountToPay)

friendBalances=amountToPay

print('balances')
print(friendBalances)

for friend in friendBalances:

    if friendBalances[friend]==0:
        # nothing to pay
        print(f'{friend} payments are cleared')

    elif friendBalances[friend]<0:
        print('')
        # pay to someone

        for temp in friendBalances:

            if temp!=friend:
                # both are not the same person

                if friendBalances[temp]>0:      

                    # amountPaid = abs(friendBalances[friend])            

                 
                    #     print(f'{friend} to {temp} Rs. {paidAmount}')
                    #     print(friendBalances)
                   

    else:
        #get from someone
        print('')

        