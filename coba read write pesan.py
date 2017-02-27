import binascii
import bitarray

ba = bitarray.bitarray()

fileName = "message.txt"

with open(fileName, mode='rb') as file:
    fileContent = file.read()

fileContent = bin(int(binascii.hexlify(fileContent), 16))
# print(fileContent)

bitmessage = ba.fromstring(fileContent)
bitmessage = ba.tolist()
print(bitmessage)

n = int(bitarray.bitarray(bitmessage).tostring(),2)
write = binascii.unhexlify('%x' % n)

f = open('result.txt', 'wb')
f.write(write)
f.close()