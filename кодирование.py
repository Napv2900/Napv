def converter():
    import math
    number = int(input("Выберите тип задачи, которую надо решить:"
                       "\n1. Кодирование информации"
                       "\n2. Кодирование звука"
                       "\n3. Кодирование изображения\n"))
    def infa():
        x = str(input("Что вы хотите найти? "))
        if x == "N":
            i = int(input("Введите значение i(битов): "))
            print(2 ** i)
        if x == "i":
            N = int(input("Введите значение N(битов), если оно известно, если нет, то 0: "))
            if N != 0:
                print(math.log2(N))
            else:
                I = int(input("Введите значение I(битов): "))
                K = int(input("Введите значение K(кол-во символов): "))
                print(I // K)
        if x == "I":
            K = int(input("Введите значение K(кол-во символов): "))
            i = int(input("Введите значение i(битов), если оно известно, если нет, то 0: "))
            if i != 0:
                print(K * i)
            else:
                print(K * math.log2(N))
        if x == "K":
            I = int(input("Введите значение I(битов): "))
            i = int(input("Введите значение i(битов), если оно известно, если нет, то 0: "))
            if i != 0:
                print(I // i)
            else:
                print(I // math.log2(N))

    def audio():
        x = str(input("Что вы хотите найти? "))
        if x == "K":
            b = int(input("Введите значение b(битов): "))
            print(2 ** b)
        if x == "b":
            K = int(input("Введите значение K(кол-во ур. квант. звука), если оно извсетно, если нет, то 0: "))
            if K != 0:
                print(math.log2(K))
            else:
                I = int(input("Введите значение I(битов): "))
                H = int(input("Введите значение H(Гц): "))
                t = int(input("Введите значение t(с): "))
                print(I / (H * t))
        if x == "I":
            H = int(input("Введите значение H(Гц): "))
            t = int(input("Введите значение t(с): "))
            b = int(input("Введите значение b(битов), если оно извсетно, если нет, то 0: "))
            if b != 0:
                print(H * t * b)
            else:
                K = int(input("Введите значение K(кол-во ур. квант. звука): "))
                print(H * t * math.log2(K))
        if x == "H":
            I = int(input("Введите значение I(битов): "))
            t = int(input("Введите значение t(с): "))
            b = int(input("Введите значение b(битов), если оно извсетно, если нет, то 0: "))
            if b != 0:
                print(I / (t * b))
            else:
                K = int(input("Введите значение K(кол-во ур. квант. звука): "))
                print(I / (t * math.log2(K)))
        if x == "t":
            I = int(input("Введите значение I(битов): "))
            H = int(input("Введите значение H(Гц): "))
            b = int(input("Введите значение b(битов), если оно извсетно, если нет, то 0: "))
            if b != 0:
                print(I / (H * b))
            else:
                K = int(input("Введите значение K(кол-во ур. квант. звука): "))
                print(I / (H * math.log2(K)))

    def image():
        x = str(input("Что вы хотите найти? "))
        if x == "K":
            b = int(input("Введите значение b(битов):"))
            print(2 ** b)
        if x == "b":
            K = int(input("Введите значение K(кол-во оттенков): "))
            print(math.log2(K))
    if number==1:
        infa()
    if number==2:
        audio()
    if number==3:
        image()
