import random
from Cryptodome.Util import number
import numpy as np
import math
import tkinter as tk
from tkinter import messagebox
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def frequency_test(sequence):
    print(bcolors.HEADER + "\nЧастотный тест:"  + bcolors.ENDC)
    print("\tШаг 1.")
    # Преобразование последовательности 0 и 1 в последовательность -1 и 1
    x = np.zeros(len(sequence))
    for i in range(len(sequence)):
        x[i] = 2 * int(sequence[i]) - 1
    print("Преобразованная последовательность: ", x)
    print("\tШаг 2.")
    # Вычисление суммы
    sn = sum(x)
    print("Сумма Sn = ",sn)
    app.frequencyfield1.delete(0,'end')
    app.frequencyfield1.insert(0,sn)
    print("\tШаг 3.")
    # Вычисление статистики
    s = abs(sn) / math.sqrt(len(sequence))
    app.frequencyfield2.delete(0, 'end')
    app.frequencyfield2.insert(0, s)
    # Критическое значение для уровня значимости α=0.01
    critical_value = 1.82138636
    print("Статистика S = ", s,"\nКритическое значение для уровня значимости 0.01 = ", critical_value)
    # Вывод результата теста
    return s <= critical_value

def runs_test(sequence_str):
    print(bcolors.HEADER + "\nТест на последовательность одинаковых бит:" + bcolors.ENDC)
    print("\tШаг 1.")
    n = len(sequence_str)
    sequence = np.zeros(n)
    for i in range(n):
        sequence[i] = sequence_str[i]
    pi = sum(sequence) / n
    print("Частота единиц в последовательности = ",pi)
    app.runsfield1.delete(0,'end')
    app.runsfield1.insert(0,pi)
    print("\tШаг 2.")
    v = 1
    for k in range(n - 1):
        if(sequence[k] != sequence[k+1]):
            v += 1
    print("Vn = ",v)
    app.runsfield2.delete(0,'end')
    app.runsfield2.insert(0,v)
    print("\tШаг 3.")
    # Вычисление статистики
    test = abs(v - 2 * n * pi * (1 - pi))
    de = 2 * math.sqrt(2 * n) * pi * (1 - pi)
    s =  abs(v - 2 * n * pi * (1 - pi)) / (2 * math.sqrt(2 * n) * pi * (1 - pi))
    app.runsfield3.delete(0,'end')
    app.runsfield3.insert(0,s)
    # Критическое значение для уровня значимости α=0.01
    critical_value = 1.82138636
    print("\tСтатистика S = ", s,"\n\tКритическое значение для уровня значимости 0.01 = ", critical_value)
    # Вывод результата теста
    return s <= critical_value

def arbitrary_deviations_test(sequence):
    print(bcolors.HEADER + "\nТест на произвольные отклонения:" + bcolors.ENDC)
    # Критическое значение для уровня значимости α=0.01
    critical_value = 1.82138636
    print("\tШаг 1.")
    n = len(sequence)
    x = np.zeros(len(sequence))
    for i in range(n):
        x[i] = 2 * int(sequence[i]) - 1
    print("Преобразованная последовательность: ",x)
    print("\tШаг 2.")
    s = np.zeros(n+1)
    L = 1
    # Вычисление сумм S_i
    with open("sumi.txt", "a") as file:
        for i in range(1, n):
            s[i] = sum(x[:i])
            if s[i] == 0:
                L += 1
            file.write("s[%d] = %f\n" % (i, s[i]))
        file.write("\n\n\n")
    print("Суммы Si записаны в файл sumi.txt")
    print("\tШаг 3.")
    print("Количество нулей L = ",L)
    app.arbitraryfield2.delete(0,'end')
    app.arbitraryfield2.insert(0,L)
    print("\tШаг 4.")
    # Подсчет количества посещений каждого из 18 состояний
    xi = []
    for i in range(-9, 10):
        if i != 0:
            count = 0
            for j in range(n):
                if s[j] == i:
                    count += 1
            xi.append(count)
    ksiout = ""
    for i in range(0,18):
        if(i-9<0):
            temp = ""+str(i-9)+": "+str(xi[i])+" | "
            ksiout = ksiout+temp
        else:
            temp = ""+str(i-8)+": "+str(xi[i])+" | "
            ksiout = ksiout+temp
    app.arbitraryfield1.delete(0,'end')
    app.arbitraryfield1.insert(0,ksiout)
    # Расчет 18 статистик Yj
    Y = []
    for elem, j in zip(xi, range(-9, 9)):
        if j < 0:
            test = 2 * L * (4 * abs(j) - 2)
            Y.append(abs(elem - L) / math.sqrt(test))
        else:
            test = 2 * L * (4*abs(j+1)-2)
            Y.append(abs(elem-L)/math.sqrt(test))
        if j<0:
            print("\tКоличество посещений состояния #",j+10,"= ",elem,"\t\tСтатистика Y[",j,"] = ",Y[j+9])
        else:
            print("\tКоличество посещений состояния #",j+10,"= ",elem,"\t\tСтатистика Y[",j,"] = ",Y[j+8])

    app.y1.delete(0,'end')
    app.y2.delete(0,'end')
    app.y3.delete(0,'end')
    app.y4.delete(0,'end')
    app.y5.delete(0,'end')
    app.y6.delete(0,'end')
    app.y7.delete(0,'end')
    app.y8.delete(0,'end')
    app.y9.delete(0,'end')
    app.y10.delete(0,'end')
    app.y11.delete(0,'end')
    app.y12.delete(0,'end')
    app.y13.delete(0,'end')
    app.y14.delete(0,'end')
    app.y15.delete(0,'end')
    app.y16.delete(0,'end')
    app.y17.delete(0,'end')
    app.y18.delete(0,'end')

    app.y1.insert(0,"Y[-9]="+str(Y[0]))
    app.y2.insert(0,"Y[-8]="+str(Y[1]))
    app.y3.insert(0,"Y[-7]="+str(Y[2]))
    app.y4.insert(0,"Y[-6]="+str(Y[3]))
    app.y5.insert(0,"Y[-5]="+str(Y[4]))
    app.y6.insert(0,"Y[-4]="+str(Y[5]))
    app.y7.insert(0,"Y[-3]="+str(Y[6]))
    app.y8.insert(0,"Y[-2]="+str(Y[7]))
    app.y9.insert(0,"Y[-1]="+str(Y[8]))
    app.y10.insert(0,"Y[1]="+str(Y[9]))
    app.y11.insert(0,"Y[2]="+str(Y[10]))
    app.y12.insert(0,"Y[3]="+str(Y[11]))
    app.y13.insert(0,"Y[4]="+str(Y[12]))
    app.y14.insert(0,"Y[5]="+str(Y[13]))
    app.y15.insert(0,"Y[6]="+str(Y[14]))
    app.y16.insert(0,"Y[7]="+str(Y[15]))
    app.y17.insert(0,"Y[8]="+str(Y[16]))
    app.y18.insert(0,"Y[9]="+str(Y[17]))

    print("\tКритическое значение при уровне значимости 0.01 = ",critical_value)
    # Проверка условия прохождения теста
    passed = all(y <= critical_value for y in Y)
    # Вывод результатов теста
    return passed


def rightrotate(i, n):
    return ((i >> n) | (i << (32 - n))) & 0xFFFFFFFF
def sha256(message):
    bytes = ""

    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
         0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
         0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
         0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
         0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
         0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
         0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
         0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

    for n in range(len(message)):
        bytes += '{0:08b}'.format(ord(message[n]))
    bits = bytes+"1"
    pBits = bits
    while len(pBits)%512 != 448:
        pBits += "0"
    pBits += '{0:064b}'.format(len(bits)-1)

    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    for c in chunks(pBits, 512):
        words = chunks(c, 32)
        w = [0]*64
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 64):
            s0 = rightrotate(w[i-15], 7)^rightrotate(w[i-15], 18)^(w[i-15]>>3)
            s1 = rightrotate(w[i-2], 17)^rightrotate(w[i-2], 19)^(w[i-2]>>10)
            w[i] = (w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        for i in range(0, 64):
            s0 = rightrotate(a,2)^rightrotate(a,13)^rightrotate(a,22)
            maj = (a&b)^(a&c)^(b&c)
            t2 = s0 + maj
            s1 = rightrotate(e,6)^rightrotate(e,11)^rightrotate(e,25)
            ch = (e&f)^(~e&g)
            t1 = h + s1 + ch + k[i] + w[i]

            h = g
            g = f
            f = e
            e = (d+t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1+t2) & 0xFFFFFFFF

        h0 = (h0+a) & 0xFFFFFFFF
        h1 = (h1+b) & 0xFFFFFFFF
        h2 = (h2+c) & 0xFFFFFFFF
        h3 = (h3+d) & 0xFFFFFFFF
        h4 = (h4+e) & 0xFFFFFFFF
        h5 = (h5+f) & 0xFFFFFFFF
        h6 = (h6+g) & 0xFFFFFFFF
        h7 = (h7+h) & 0xFFFFFFFF

    return '%08x%08x%08x%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4, h5, h6, h7)

def G(t, z):
    return int(sha256(str(t) + str(z)), 16)
def generate_random_numbers(m, q, b):
    random_numbers = []
    s = random.getrandbits(b)
    t = 0x67452301efcdab8998badcfe10325476c3d2e1f0
    for i in range(m):
        #y_i = random.getrandbits(b)
        y_i = 0
        z_i = (s + y_i) % (2 ** b)
        x_i = G(t, z_i) % q
        s = (1 + s + x_i) % (2 ** b)
        random_numbers.append(x_i)
    return random_numbers


q_r = number.getPrime(160)





class App:
    def __init__(self, root):
        #setting title
        root.title("FIPS-186")
        #setting window size
        width=800
        height=450
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.mlabel=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.mlabel["font"] = ft
        self.mlabel["fg"] = "#333333"
        self.mlabel["justify"] = "left"
        self.mlabel["text"] = "Quantity of pseudorandom numbers to generate - 'm'"
        self.mlabel.place(x=20,y=20,width=300,height=30)

        self.qlabel=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.qlabel["font"] = ft
        self.qlabel["fg"] = "#333333"
        self.qlabel["justify"] = "left"
        self.qlabel["text"] = "160-bit simple integer- 'q'"
        self.qlabel.place(x=20,y=80,width=300,height=30)

        self.blabel=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.blabel["font"] = ft
        self.blabel["fg"] = "#333333"
        self.blabel["justify"] = "left"
        self.blabel["text"] = "Arbitrary number - 'b'"
        self.blabel.place(x=20,y=140,width=300,height=30)

        self.trieslabel=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.trieslabel["font"] = ft
        self.trieslabel["fg"] = "#333333"
        self.trieslabel["justify"] = "left"
        self.trieslabel["text"] = "How many times it took to pass all tests"
        self.trieslabel.place(x=20,y=290,width=300,height=30)

        self.frequencylabel=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.frequencylabel["font"] = ft
        self.frequencylabel["fg"] = "#333333"
        self.frequencylabel["justify"] = "left"
        self.frequencylabel["text"] = "Frequency test"
        self.frequencylabel.place(x=360,y=20,width=160,height=30)

        self.frequencylabel1=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.frequencylabel1["font"] = ft
        self.frequencylabel1["fg"] = "#333333"
        self.frequencylabel1["justify"] = "left"
        self.frequencylabel1["text"] = "Sn ="
        self.frequencylabel1.place(x=360,y=60,width=30,height=30)

        self.frequencylabel2=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.frequencylabel2["font"] = ft
        self.frequencylabel2["fg"] = "#333333"
        self.frequencylabel2["justify"] = "left"
        self.frequencylabel2["text"] = "S = "
        self.frequencylabel2.place(x=360,y=110,width=30,height=30)

        self.runslabel=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.runslabel["font"] = ft
        self.runslabel["fg"] = "#333333"
        self.runslabel["justify"] = "left"
        self.runslabel["text"] = "Identical bits' sequence test"
        self.runslabel.place(x=360,y=180,width=160,height=30)

        self.runslabel1=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.runslabel1["font"] = ft
        self.runslabel1["fg"] = "#333333"
        self.runslabel1["justify"] = "left"
        self.runslabel1["text"] = "Pi = "
        self.runslabel1.place(x=360,y=220,width=30,height=30)

        self.runslabel2=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.runslabel2["font"] = ft
        self.runslabel2["fg"] = "#333333"
        self.runslabel2["justify"] = "left"
        self.runslabel2["text"] = "Vn = "
        self.runslabel2.place(x=360,y=260,width=30,height=30)

        self.runslabel3=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.runslabel3["font"] = ft
        self.runslabel3["fg"] = "#333333"
        self.runslabel3["justify"] = "left"
        self.runslabel3["text"] = "S = "
        self.runslabel3.place(x=360,y=300,width=30,height=30)

        self.arbitrarylabel=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.arbitrarylabel["font"] = ft
        self.arbitrarylabel["fg"] = "#333333"
        self.arbitrarylabel["justify"] = "left"
        self.arbitrarylabel["text"] = "Arbitrary deviations test"
        self.arbitrarylabel.place(x=570,y=20,width=160,height=30)

        self.arbitrarylabel1=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.arbitrarylabel1["font"] = ft
        self.arbitrarylabel1["fg"] = "#333333"
        self.arbitrarylabel1["justify"] = "left"
        self.arbitrarylabel1["text"] = "Ksi = "
        self.arbitrarylabel1.place(x=530,y=60,width=30,height=30)

        self.arbitrarylabel2=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.arbitrarylabel2["font"] = ft
        self.arbitrarylabel2["fg"] = "#333333"
        self.arbitrarylabel2["justify"] = "left"
        self.arbitrarylabel2["text"] = "L = "
        self.arbitrarylabel2.place(x=530,y=110,width=30,height=30)

        self.arbitrarylabel3=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.arbitrarylabel3["font"] = ft
        self.arbitrarylabel3["fg"] = "#333333"
        self.arbitrarylabel3["justify"] = "center"
        self.arbitrarylabel3["text"] = "Yn"
        self.arbitrarylabel3.place(x=650,y=170,width=30,height=30)

        self.mfield=tk.Entry(root)
        self.mfield["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.mfield["font"] = ft
        self.mfield["fg"] = "#333333"
        self.mfield["justify"] = "left"
        self.mfield["text"] = "100"
        self.mfield.place(x=20,y=50,width=160,height=30)

        self.qfield=tk.Entry(root)
        self.qfield["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.qfield["font"] = ft
        self.qfield["fg"] = "#333333"
        self.qfield["justify"] = "left"
        self.qfield["text"] = ""
        self.qfield.place(x=20,y=110,width=160,height=30)

        self.bfield=tk.Entry(root)
        self.bfield["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.bfield["font"] = ft
        self.bfield["fg"] = "#333333"
        self.bfield["justify"] = "left"
        self.bfield["text"] = "160"
        self.bfield.place(x=20,y=170,width=160,height=30)

        self.results=tk.Entry(root)
        self.results["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.results["font"] = ft
        self.results["fg"] = "#333333"
        self.results["justify"] = "left"
        self.results["text"] = "Here will be your result"
        self.results.place(x=20,y=230,width=300,height=40)

        self.triesfield=tk.Entry(root)
        self.triesfield["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.triesfield["font"] = ft
        self.triesfield["fg"] = "#333333"
        self.triesfield["justify"] = "left"
        self.triesfield["text"] = "0"
        self.triesfield.place(x=250,y=290,width=40,height=30)

        self.frequencyfield1=tk.Entry(root)
        self.frequencyfield1["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.frequencyfield1["font"] = ft
        self.frequencyfield1["fg"] = "#333333"
        self.frequencyfield1["justify"] = "left"
        self.frequencyfield1["text"] = ""
        self.frequencyfield1.place(x=400,y=60,width=100,height=30)

        self.frequencyfield2=tk.Entry(root)
        self.frequencyfield2["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.frequencyfield2["font"] = ft
        self.frequencyfield2["fg"] = "#333333"
        self.frequencyfield2["justify"] = "left"
        self.frequencyfield2["text"] = ""
        self.frequencyfield2.place(x=400,y=110,width=100,height=30)

        self.runsfield1=tk.Entry(root)
        self.runsfield1["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.runsfield1["font"] = ft
        self.runsfield1["fg"] = "#333333"
        self.runsfield1["justify"] = "left"
        self.runsfield1["text"] = ""
        self.runsfield1.place(x=400,y=220,width=70,height=30)

        self.runsfield2=tk.Entry(root)
        self.runsfield2["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.runsfield2["font"] = ft
        self.runsfield2["fg"] = "#333333"
        self.runsfield2["justify"] = "left"
        self.runsfield2["text"] = ""
        self.runsfield2.place(x=400,y=260,width=70,height=30)

        self.runsfield3=tk.Entry(root)
        self.runsfield3["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.runsfield3["font"] = ft
        self.runsfield3["fg"] = "#333333"
        self.runsfield3["justify"] = "left"
        self.runsfield3["text"] = ""
        self.runsfield3.place(x=400,y=300,width=70,height=30)



        self.arbitraryfield1=tk.Entry(root)
        self.arbitraryfield1["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.arbitraryfield1["font"] = ft
        self.arbitraryfield1["fg"] = "#333333"
        self.arbitraryfield1["justify"] = "left"
        self.arbitraryfield1["text"] = ""
        self.arbitraryfield1.place(x=560,y=60,width=200,height=30)

        self.arbitraryfield2=tk.Entry(root)
        self.arbitraryfield2["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.arbitraryfield2["font"] = ft
        self.arbitraryfield2["fg"] = "#333333"
        self.arbitraryfield2["justify"] = "left"
        self.arbitraryfield2["text"] = ""
        self.arbitraryfield2.place(x=560,y=110,width=200,height=30)


        self.y1=tk.Entry(root)
        self.y1["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y1["font"] = ft
        self.y1["fg"] = "#333333"
        self.y1["justify"] = "left"
        self.y1["text"] = "1"
        self.y1.place(x=550,y=210,width=70,height=30)

        self.y2=tk.Entry(root)
        self.y2["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y2["font"] = ft
        self.y2["fg"] = "#333333"
        self.y2["justify"] = "left"
        self.y2["text"] = "2"
        self.y2.place(x=550,y=250,width=70,height=30)

        self.y3=tk.Entry(root)
        self.y3["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y3["font"] = ft
        self.y3["fg"] = "#333333"
        self.y3["justify"] = "left"
        self.y3["text"] = "3"
        self.y3.place(x=550,y=290,width=70,height=30)

        self.y4=tk.Entry(root)
        self.y4["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y4["font"] = ft
        self.y4["fg"] = "#333333"
        self.y4["justify"] = "left"
        self.y4["text"] = "4"
        self.y4.place(x=550,y=330,width=70,height=30)

        self.y5=tk.Entry(root)
        self.y5["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y5["font"] = ft
        self.y5["fg"] = "#333333"
        self.y5["justify"] = "left"
        self.y5["text"] = "5"
        self.y5.place(x=550,y=370,width=70,height=30)

        self.y6=tk.Entry(root)
        self.y6["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y6["font"] = ft
        self.y6["fg"] = "#333333"
        self.y6["justify"] = "left"
        self.y6["text"] = "6"
        self.y6.place(x=550,y=410,width=70,height=30)

        self.y7=tk.Entry(root)
        self.y7["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y7["font"] = ft
        self.y7["fg"] = "#333333"
        self.y7["justify"] = "left"
        self.y7["text"] = "7"
        self.y7.place(x=630,y=210,width=70,height=30)

        self.y8=tk.Entry(root)
        self.y8["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y8["font"] = ft
        self.y8["fg"] = "#333333"
        self.y8["justify"] = "left"
        self.y8["text"] = "8"
        self.y8.place(x=630,y=250,width=70,height=30)

        self.y9=tk.Entry(root)
        self.y9["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y9["font"] = ft
        self.y9["fg"] = "#333333"
        self.y9["justify"] = "left"
        self.y9["text"] = "9"
        self.y9.place(x=630,y=290,width=70,height=30)

        self.y10=tk.Entry(root)
        self.y10["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y10["font"] = ft
        self.y10["fg"] = "#333333"
        self.y10["justify"] = "left"
        self.y10["text"] = "10"
        self.y10.place(x=630,y=330,width=70,height=30)

        self.y11=tk.Entry(root)
        self.y11["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y11["font"] = ft
        self.y11["fg"] = "#333333"
        self.y11["justify"] = "left"
        self.y11["text"] = "11"
        self.y11.place(x=630,y=370,width=70,height=30)

        self.y12=tk.Entry(root)
        self.y12["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y12["font"] = ft
        self.y12["fg"] = "#333333"
        self.y12["justify"] = "left"
        self.y12["text"] = "12"
        self.y12.place(x=630,y=410,width=70,height=30)

        self.y13=tk.Entry(root)
        self.y13["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y13["font"] = ft
        self.y13["fg"] = "#333333"
        self.y13["justify"] = "left"
        self.y13["text"] = "13"
        self.y13.place(x=710,y=210,width=70,height=30)

        self.y14=tk.Entry(root)
        self.y14["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y14["font"] = ft
        self.y14["fg"] = "#333333"
        self.y14["justify"] = "left"
        self.y14["text"] = "14"
        self.y14.place(x=710,y=250,width=70,height=30)

        self.y15=tk.Entry(root)
        self.y15["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y15["font"] = ft
        self.y15["fg"] = "#333333"
        self.y15["justify"] = "left"
        self.y15["text"] = "15"
        self.y15.place(x=710,y=290,width=70,height=30)

        self.y16=tk.Entry(root)
        self.y16["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y16["font"] = ft
        self.y16["fg"] = "#333333"
        self.y16["justify"] = "left"
        self.y16["text"] = "16"
        self.y16.place(x=710,y=330,width=70,height=30)

        self.y17=tk.Entry(root)
        self.y17["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y17["font"] = ft
        self.y17["fg"] = "#333333"
        self.y17["justify"] = "left"
        self.y17["text"] = "17"
        self.y17.place(x=710,y=370,width=70,height=30)


        # bottom right
        self.y18=tk.Entry(root)
        self.y18["borderwidth"] = "1px"
        #ft = tkFont.Font(family='Times',size=10)
        #self.y18["font"] = ft
        self.y18["fg"] = "#333333"
        self.y18["justify"] = "left"
        self.y18["text"] = "18"
        self.y18.place(x=710,y=410,width=70,height=30)

        self.saveparametersbutton=tk.Button(root)
        self.saveparametersbutton["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        #self.saveparametersbutton["font"] = ft
        self.saveparametersbutton["fg"] = "#000000"
        self.saveparametersbutton["justify"] = "center"
        self.saveparametersbutton["text"] = "Save parameters"
        self.saveparametersbutton.place(x=20,y=340,width=100,height=30)
        self.saveparametersbutton["command"] = self.button0_command

        self.loadparametersbutton=tk.Button(root)
        self.loadparametersbutton["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        #self.loadparametersbutton["font"] = ft
        self.loadparametersbutton["fg"] = "#000000"
        self.loadparametersbutton["justify"] = "center"
        self.loadparametersbutton["text"] = "Load parameters"
        self.loadparametersbutton.place(x=20,y=390,width=100,height=30)
        self.loadparametersbutton["command"] = self.button1_command

        self.calculatebutton=tk.Button(root)
        self.calculatebutton["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        #self.calculatebutton["font"] = ft
        self.calculatebutton["fg"] = "#000000"
        self.calculatebutton["justify"] = "center"
        self.calculatebutton["text"] = "Calculate"
        self.calculatebutton.place(x=140,y=340,width=100,height=30)
        self.calculatebutton["command"] = self.button2_command

        self.saveresultsbutton=tk.Button(root)
        self.saveresultsbutton["bg"] = "#f0f0f0"
        #ft = tkFont.Font(family='Times',size=10)
        #self.saveresultsbutton["font"] = ft
        self.saveresultsbutton["fg"] = "#000000"
        self.saveresultsbutton["justify"] = "center"
        self.saveresultsbutton["text"] = "Save results"
        self.saveresultsbutton.place(x=140,y=390,width=100,height=30)
        self.saveresultsbutton["command"] = self.button3_command

        self.resultslabel=tk.Label(root)
        #ft = tkFont.Font(family='Times',size=10)
        #self.resultslabel["font"] = ft
        self.resultslabel["fg"] = "#333333"
        self.resultslabel["justify"] = "left"
        self.resultslabel["text"] = "Results"
        self.resultslabel.place(x=20,y=200,width=70,height=25)



    def button0_command(self):
        print("Saving parameters")
        with open('params.txt', 'w') as file:
            m = self.mfield.get() + "\n"
            q = self.qfield.get() + "\n"
            b = self.bfield.get()
            file.write(m)
            file.write(q)
            file.write(b)



    def button1_command(self):
        print("Loading parameters")
        with open('params.txt', 'r') as file:
            lines = file.readlines()
        self.mfield.delete(0, 'end')
        self.mfield.insert(0, int(lines[0].strip()))
        self.qfield.delete(0, 'end')
        self.qfield.insert(0, int(lines[1].strip()))
        if (int(lines[2].strip()) in range(160, 512)):
            self.bfield.delete(0, 'end')
            self.bfield.insert(0, int(lines[2].strip()))
        else:
            self.bfield.delete(0, 'end')
            self.bfield.insert(0, 160)


    def button2_command(self):
        print("Calculating")
        # Загрузка параметров из полей
        m = int(self.mfield.get())
        q = int(self.qfield.get())
        b = int(self.bfield.get())
        if (b not in range(159, 513)):
            messagebox.showerror('Wrong input', 'b must be in the range 160-512')
            return
        # Очистка файла вывода сумм одного из тестов
        open("sumi.txt", "w").close()
        # Генерация псевдослучайных чисел
        gen = 1
        while (gen != 0):
            print(bcolors.OKBLUE + "Попытка #", gen, "" + bcolors.ENDC)
            random_numbers = generate_random_numbers(m, q, b)

            binary_sequence = ""
            for number in random_numbers:
                binary_number = format(number, 'b')
                binary_sequence += binary_number

            print(bcolors.HEADER + "Количество бит: ", len(binary_sequence), "" + bcolors.ENDC)

            if frequency_test(binary_sequence):
                print(bcolors.OKGREEN + "Последовательность проходит частотный тест" + bcolors.ENDC)
                if runs_test(binary_sequence):
                    print(
                        bcolors.OKGREEN + "Последовательность проходит тест на последовательность одинаковых бит" + bcolors.ENDC)
                    if arbitrary_deviations_test(binary_sequence):
                        print(
                            bcolors.OKGREEN + "Последовательность проходит тест на произвольные отклонения" + bcolors.ENDC)
                        self.triesfield.delete(0, 'end')
                        self.triesfield.insert(0, gen)
                        gen = 0
                    else:
                        print(
                            bcolors.FAIL + "Последовательность не проходит тест на произвольные отклонения" + bcolors.ENDC)
                        gen += 1
                else:
                    print(
                        bcolors.FAIL + "Последовательность не проходит тест на последовательность одинаковых бит" + bcolors.ENDC)
                    gen += 1
            else:
                print(bcolors.FAIL + "Последовательность не проходит частотный тест" + bcolors.ENDC)
                gen += 1

            temp = ""
            for binary_number in binary_sequence:
                temp += str(binary_number)
            self.results.delete(0, 'end')
            self.results.insert(0, temp)


    def button3_command(self):
        print("Saving results")
        with open('random_numbers.txt', 'w') as file:
            binary_sequence = self.results.get()
            for binary_number in binary_sequence:
                file.write(f'{binary_number}')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
