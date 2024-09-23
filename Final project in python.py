    #In this python program, I will be desciphering a substitution cipher
            #The message that will be desciphered is: 

            #      jyn fg jggtwj djtfcn stf sjyn edcyjnc ia zy stes fjqtye z wzdn owcff gstf gsq sjyn edcyjnc gsjg mtgs tg gszi xjqcfg 
            #      owzm gstyc cycxtcf gz gtyq otgf ty gsq xcdhq jyn gsc wzdn ntn edty jyn aczawc ntn lcjfg iazy gsc wjxof jyn fwzgsf jyn hjda jyn 
            #      jyhszktcf jyn zdjyeigjyf jyn odcjvljfg hcdcjwf jyn lditg ojgf jyn gsc wzdn fajvc fjqtye ltdfg fsjwg gszi gjvc zig gsc szwq aty gscy 
            #      fsjwg gszi hziyg gz gsdcc yz xzdc yz wcff gsdcc fsjwg oc gsc yixocd gszi fsjwg hziyg jyn gsc yixocd zl gsc hziygtye fsjwg oc gsdcc 
            #      lzid fsjwg gszi yzg hziyg yctgscd hziyg gszi gmz cphcagtye gsjg gszi gscy adzhccn gz gsdcc ltkc tf dtesg zig zyhc gsc yixocd gsdcc 
            #      octye gsc gstdn yixocd oc dcjhscn gscy wzoocfg gszi gsq szwq sjyn edcyjnc zl jygtzhs gzmjdnf gszi lzc msz octye yjiesgq ty xq 
            #      ftesg fsjww fyill tg


            #When you run this program you will get the output with a list of decrypted words ordred by their length, and the actual 
            # decrypted paragraph below the list of words.





                #START


    #This is the encrypted message below
cipherText = 'jyn fg jggtwj djtfcn stf sjyn edcyjnc ia zy stes fjqtye z wzdn owcff gstf gsq sjyn edcyjnc gsjg mtgs tg gszi xjqcfg owzm gstyc cycxtcf gz gtyq otgf ty gsq xcdhq jyn gsc wzdn ntn edty jyn aczawc ntn lcjfg iazy gsc wjxof jyn fwzgsf jyn hjda jyn jyhszktcf jyn zdjyeigjyf jyn odcjvljfg hcdcjwf jyn lditg ojgf jyn gsc wzdn fajvc fjqtye ltdfg fsjwg gszi gjvc zig gsc szwq aty gscy fsjwg gszi hziyg gz gsdcc yz xzdc yz wcff gsdcc fsjwg oc gsc yixocd gszi fsjwg hziyg jyn gsc yixocd zl gsc hziygtye fsjwg oc gsdcc lzid fsjwg gszi yzg hziyg yctgscd hziyg gszi gmz cphcagtye gsjg gszi gscy adzhccn gz gsdcc ltkc tf dtesg zig zyhc gsc yixocd gsdcc octye gsc gstdn yixocd oc dcjhscn gscy wzoocfg gszi gsq szwq sjyn edcyjnc zl jygtzhs gzmjdnf gszi lzc msz octye yjiesgq ty xq ftesg fsjww fyill tg'

        #This is a function to add a character to a dictionary with a count
def maybeAdd(ch, toDict):   
    if ch in 'abcdefghijklmnopqrstuvwxyz':      #Check if the character is in the alphabet
        toDict[ch] = toDict.setdefault(ch, 0) + 1       #add the character to the dictionary or increment its count


    #This is a function to count neighbor occurances in the text
def neighborCount(text):
    nbDict = {}     #Dictionary to store neighbors and their counts
    text = text.lower()     #Convert text to lowercase
    for i in range(len(text) - 1):
        nbList = nbDict.setdefault(text[i], {})     #Get the list of neighbors for the current character or create an empty dictionary if none 
        maybeAdd(text[i + 1], nbList)               #Add the next character to the current's neighbor list
        nbList = nbDict.setdefault(text[i + 1], {}) #Get the list of neighbors for the next character or create an empty dictionary if none
        maybeAdd(text[i], nbList)                   #Add the current character to the next character's neighbor list
    return nbDict                                  


freqDict = neighborCount(cipherText)                #Generate the frequency dictionary for neighbors

    #for loop to print the frequency of the characters.
        #This was used for every character to find out the frequency. You can do so by putting in the letter you want instead of s
for i in 's':               
    if i in freqDict:
      print(i, freqDict[i])
    else:
        print(f"{i}: Not found in freqDict")


    #Substituting cipher decryption by replacing each character with its mapped and guessed value
cipherText = cipherText.replace('c', 'E')
cipherText = cipherText.replace('y', 'N')
cipherText = cipherText.replace('z', 'O')
cipherText = cipherText.replace('s', 'H')
cipherText = cipherText.replace('g', 'T')
cipherText = cipherText.replace('d', 'R')
cipherText = cipherText.replace('j', 'A')
cipherText = cipherText.replace('t', 'I')
cipherText = cipherText.replace('x', 'M')
cipherText = cipherText.replace('f', 'S')
cipherText = cipherText.replace('n', 'D')
cipherText = cipherText.replace('e', 'G')
cipherText = cipherText.replace('m', 'W')
cipherText = cipherText.replace('w', 'L')
cipherText = cipherText.replace('i', 'U')
cipherText = cipherText.replace('q', 'Y')
cipherText = cipherText.replace('a', 'P')
cipherText = cipherText.replace('o', 'B')
cipherText = cipherText.replace('h', 'C')
cipherText = cipherText.replace('l', 'F')
cipherText = cipherText.replace('p', 'X')
cipherText = cipherText.replace('k', 'V')
cipherText = cipherText.replace('v', 'K')

    #function to sort the words by length
def sortByLen(word):
    return len(word)

    #Split the text into words and sort them by length
cipherWords = cipherText.split()
cipherWords.sort(key = sortByLen)
print()
print(cipherWords)


    #Print the decrypted message
print()
print (cipherText)



