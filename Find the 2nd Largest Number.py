# Find the second largest value from the user input list.
#input: 2 3 6 6 5
#output 5


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) #arr is an object

    scores = list(arr) #use list() to convert it into a list
    maxscore = None # to find the largest value
    for num in scores:
        if maxscore is None or num >maxscore:
            maxscore = num
            
    scores = [x for x in scores if x != maxscore]#remove the largest values
    
    runner_up =None #find the 2nd largest value after removing the 1st largest value
    for num in scores:
        if runner_up is None or num >runner_up:
            runner_up = num
    
    print(runner_up)


i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print (max(lis))
