# Repetion - While Loops 
# Inputs: 5, 20, 2, -1 
# Outputs: 27, 9, 20
# Written by: SHIRLEY HUANG 
# Date: Feb 19, 2019

bug = []
count = 1
days = int(input('Enter the number of butterflies for day %d (or -1 to end):' %count))

if days != -1:
    while days != -1:
        bug.append(days)
        count += 1
        days = int(input('Enter the number of butterflies for day %d (or -1 to end):' %count))
    print('')
    print("HERE ARE THE RESULTS OF YOUR BUTTERFLY COLLECTING")
    print('Total bugs collected: ', sum(bug))
    print('Average bugs collected per day: ', sum(bug)/len(bug))
    print('Maximum bugs collected in a day: ', max(bug))
else:
    print('')
    print("HERE ARE THE RESULTS OF YOUR BUTTERFLY COLLECTING")
    print('You entered no butterfly data')





 
        









    

    


