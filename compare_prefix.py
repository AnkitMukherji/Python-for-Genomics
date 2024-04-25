#Checking if two strings have the same prefix
def longestCommonPrefix(s1,s2):
    i=0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i+=1
    print(s1[:i])
longestCommonPrefix('ACCATGT','ACCACAGACG')
#Checking if two strings are identical or not
def match(s1,s2):
    if not len(s1) == len(s2):
        print(False)
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            print(False)
    print(True)
match('ATGCT','ATGCT')
print('AGCT' == 'AGCA') #Can be done directly by this method