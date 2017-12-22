n=raw_input("Enter a sentence or word, and I will check if its a palindrome or not!: ")
def palindrome(n):
    index=0
    check=True
    while index<len(n):
        if n[index]==n[-1-index]:
            index+=1
            return True
        return False
if palindrome(n)==True:
    print "It is a Palindrome"
else:
    print "It is not a Palindrome"