
friends = {}
amountToPay = {}
friendBalances = {}
totalAmount = 0
currentInput='dummy data'
amountPerPerson = 0

howMany= input('How many friends?\n')
howMany = int(howMany)

for i in range(howMany):
    currentInput = input('Name: ')
    friends[currentInput]=0

# while(currentInput != ''):
#     currentInput = input('Name: ')
#     if currentInput != '':friends[currentInput]=0

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
    amountToPay[friend]=toPay

print('\n')


friendBalances=amountToPay

print('balances')
print(friendBalances)

for friend in friends:

    if friendBalances[friend]==0:
        # nothing to pay
        print(f'{friend} payments are cleared')

    elif friendBalances[friend]<0:
        print('')
        # pay to someone

        for temp in friends:

            if temp!=friend:
                # both are not the same person

                if friendBalances[temp]>0:
                    currentPayment = friendBalances[friend]+friendBalances[temp]
                    if currentPayment>0:
                        amount= abs(friendBalances[friend])
                        print(f'{friend} to {temp} Rs. {amount}')
                        friendBalances[temp]=friendBalances[friend]+friendBalances[temp]
                        friendBalances[friend]=0
                    elif currentPayment<0:
                        amount= abs(friendBalances[temp])
                        print(f'{friend} to {temp} Rs. {amount}')
                        friendBalances[friend]=friendBalances[friend]+friendBalances[temp]
                        friendBalances[temp]=0
                        # print(f'{temp} to {friend} Rs. {friendBalances[temp]}')
                    elif currentPayment==0:
                        amount= abs(friendBalances[temp])
                        print(f'{friend} to {temp} Rs. {amount}')
                        friendBalances[temp]=0
                        friendBalances[friend]=0

        