import random


alpha = []
al = []
dic = {}
wr = ""
trail = {}
new_file2=""
filename=""

class Encryption():

    def code_allocation2(self):

        ch= ""
        val= ""
        '''
        alpha is an array used for the storing of random values for alphabets
        in form of a secret code
        '''
        # where it is declared from 1 to 26 as reserved for the alphabets
        #  after which it can be used for teh storing for numeric codes

        for i in range(32, 3000) :
            a = [4]
            b = [4]
            for j in range(1,5):    # for the string part of the code
                temp=random.randrange(65, 125)
                a.append(chr(temp))

            for j in range(1,5):
                ch = ch + a[j]

            for j in range(1,5):
                temp= random.randrange(0,9)
                b.append(str(temp))

            for j in range(1,5):
                val = val + b[j]

            alpha.append(ch+val)
            ch=""
            val=""
        self.file_saving()

    r = random.randrange(1, 1000)


    def file_saving(self):
        x=random.randrange(1,1000)
        wx=chr(x)

        wr= "./templates/scriptKey.txt"  # use this variable to get the file of encrypted code
        fw = open(wr, 'w')
        for i in range(0,len(alpha)):
            fw.write(alpha[i]+ "\n")
        fw.close()
        self.dic_alpha_assign()


    def dic_alpha_assign(self):
        for i in range(32, 3000):
            al.append(chr(i))
        self.dic_assign()

    def dic_assign(self):

        for i in range(0,2968): # clever to check this..!!!!hehehehe
            trail[al[i]] = alpha[i]
            dic.update(trail)

    # till here, code works perfectly


    new_file = ""
    new_ch = ''

    def open_file(self, text_transfer):
        # self.name = input("Enter the name of the file you want to encrypt ")
        '''self.name = self.name + ".txt"
        file = open(self.name, 'r')
        '''
        print('Worked')
        text = text_transfer
        length = len(text)
        for i in range(length):
            ch = text[i]

            for j,k in dic.items():

                if ch == j :
                    self.new_file = self.new_file + k + " "
                    break
        h = open('./templates/scriptKey.txt', 'r')
        mm = h.read()
        #print(dic)
        return self.new_file, mm

