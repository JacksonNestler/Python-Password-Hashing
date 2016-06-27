'''
Author: Shoe Development - https://github.com/shoedevelopment

Purpose: Hash passwords from a list and write their output to a text file.
Used for security research.

Dependencies: NONE! Works with Python 2.7.x out of the box.
'''
import hashlib

numOfHashes = 0
file = raw_input("Enter the name of the file containing the passwords, "
                 "including the extension. \n >>> ")
hashedValues = open('output.txt', 'w+')
with open(file,'r') as f: #Line stolen from Sam.

    for lines in f.readlines(): #Line also stolen from Sam.
        print "Hashing ", lines , " now \n"
        hashvalue1 = hashlib.sha1(lines)
        print ("Done with the SHA1 for the current value.")
        hashedValues.write("%s\n" % hashvalue1.hexdigest())

        hashvalue2 = hashlib.sha224(lines)
        print("Done with the SHA224 for the current value.")
        hashedValues.write("%s\n" % hashvalue2.hexdigest())

        hashvalue3 = hashlib.sha256(lines)
        print ("Done with the SHA256 for the current value.")
        hashedValues.write("%s\n" % hashvalue3.hexdigest())

        hashvalue4 = hashlib.sha384(lines)
        print("Done with the SHA384 for the current value.")
        hashedValues.write("%s\n" % hashvalue4.hexdigest())

        hashvalue5 = hashlib.sha512(lines)
        print("Done with the SHA512 for the current value.")
        hashedValues.write("%s\n" % hashvalue5.hexdigest())

        hashvalue6 = hashlib.md5(lines)
        print("Done with the MD5 for the current value. *Shivers*")
        hashedValues.write("%s\n" % hashvalue6.hexdigest())

        numOfHashes += 1
        print("Done with this value entirely! Moving on to the next. :D \n")



print ("Okay...we got to this point. Odds are we're done!")
print "Total # of hashes was..... ", numOfHashes
print ("Not bad!")
hashedValues.close()
f.close()
