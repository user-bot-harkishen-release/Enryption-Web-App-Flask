import random

class decryptor :
    
    def assigning_key(self, data):
        #self.name = input('Enter the Encode file key Name : ')
        #self.name= self.name+ '.txt'
        self.ene = " "
        fk = data
        self.stored_key = {}

        a = 0

        for i in fk.split(" "):
            sub = i
            self.stored_key[sub] = chr(a + 33)
            a = a + 1
        #print(self.stored_key)

    def accessing_en_doc(self, filename):
        '''self.name_file = input('Enter the name of the file to be decrypted')
        self.name_file = self.name_file + '.txt'
        self.f = open(self.name_file,'r')'''
        self.text = filename
        l = len(self.text)

        #conversion starts below  618_encryptCode_Ʀ   618__encrypted_doc_check2
        sub = []
        sub = self.text.split(" ")

        for i in sub:
            #print(i)
            for j,k in self.stored_key.items() :
                if j == i:
                    self.ene =self.ene + k


        #print(self.ene)
        #self.new_extracted_file()

    def new_extracted_file(self):
        #f2 = open('extracted_' + self.name_file[0:3]+'.txt', 'w')
        #f2.write(self.ene)
        return self.ene




