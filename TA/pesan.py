import binascii
import bitarray

class Pesan:

    def __init__(self):
        self.fileName = "message.txt"
        self.ba = bitarray.bitarray()
        # self.filecontent = ""
        # self.bitmessage = ""
        # self.writeTo = ""

    # def __init__(self, filename):
    #     self.fileName = filename
    #     self.ba = bitarray.bitarray()
    #     self.filecontent = ""
    #     self.bitmessage = ""
    #     self.writeTo = ""

    # def __init__(self, bitmessage):
    #     self.write = ""
    #     self.toMessage(bitmessage)
    #     return self.returnMessage()

    # def setfilename(self):
    #     self.fileName = "message.txt"

    def getBinary(self):
        self.bacaPesan()
        self.toBinary()
        return self.returnBinary()

    def bacaPesan(self):
        with open(self.fileName, mode='rb') as file:
            self.fileContent = file.read()

        self.fileContent = bin(int(binascii.hexlify(self.fileContent), 16))

    def toBinary(self):
        self.bitmessage = self.ba.fromstring(self.fileContent)
        self.bitmessage = self.ba.tolist()
        self.panjangbit = len(self.bitmessage)

    def toMessage(self, bitmessage):
        n = int(bitarray.bitarray(bitmessage).tostring(), 2)
        self.writeTo = binascii.unhexlify('%x' % n)

    def tulisPesan(self):
        f = open('result.txt', 'wb')
        f.write(self.writeTo)
        f.close()

    def returnBinary(self):
        return self.bitmessage

    def returnMessage(self):
        return self.writeTo

    def panjang(self):
        return self.panjangbit