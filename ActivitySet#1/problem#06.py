
# Loops & Iterators
def input():
    largest = None
    smallest = None

def logic():
     while True:
        try:
            num = raw_input("Enter a number: ")
            if num == 'done':
                break
            n = int(num)
        largest = num if largest >num or largest == None else              largest
        smallest = num if smallest < num or smallest == None else     smallest
    except:
        print "Invalid input"
def output():
    print "Maximum number is ", largest
    print "Minimum number is ", smallest