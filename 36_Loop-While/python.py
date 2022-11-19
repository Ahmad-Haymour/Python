#-----------------------------------
#      -- Loop  =>  While --

# while condition_is_true
#   Code will run Until Condition become False
#-----------------------------------

a = 0 

while a < 15 :
    a+=1
    print(a)

print("Loop Done")

while False : 
    print('Will Never Print (It\'s Always False)')

print('='*50)

## Loop List

a = 0
friends = ['Os', 'Ah', 'Sa', 'Su', 'La','Os', 'Ah', 'Sa', 'Su', 'La']

while a < len(friends):
    print('#{}- {}'.format( str( a + 1 ).zfill(3), friends[a] ))
    a += 1

else: print("All friends are printed")
print("All friends are printed")

print('='*50)

## List Manipulation
myFavoriteWebs = []
maximumWebs = 5

while maximumWebs > 0 :
    web = input("Web Site Web: https:// ")
    myFavoriteWebs.append("https://{}".format(web.strip().lower()))
    maximumWebs -= 1
    print("https://{:s} => Added.".format(web))
    print("{:d} Places Left".format(maximumWebs)) 
    print(myFavoriteWebs)

print('Bookmark is full, you can\'t add more')

## Check if list not empty

if len(myFavoriteWebs) > 0  :
    myFavoriteWebs.sort()

    print('Print the List of Web Sites in My Bookmark')

    index = 0

    while index < len(myFavoriteWebs) :
        print(myFavoriteWebs)
        index += 1
