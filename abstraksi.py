class ya:
    def __init__(iya, a):
        iya.aku = a
        iya.kamu = []
        iya.dia = []
        iya.nilai = 0

    def yes(self):
        if self.aku == "H":
            print("_ _ _ _ _")
            self.dia = [int(x) for x in input("jawaban: ").split()]
            ya.scor(self)

    def haha(self):
        import random

        u = [3,5,4,7,8]#angka
        k = ["s","f","y"]#huruf

        for r in range(len(u)):
            t = random.choice(u)
            self.kamu.append(t)
            u.remove(t)

    def scor(self):
        if self.kamu[0] == self.dia[0]:
            self.nilai += 20
        elif self.kamu[1] == self.dia[1]:
            self.nilai += 20
        elif self.kamu[2] == self.dia[2]:
            self.nilai += 20
        elif self.kamu[3] == self.dia[3]:
            self.nilai += 20
        elif self.kamu[4] == self.dia[4]:
            self.nilai += 20

def output():
    print("selamat datang")
    d = ya(input("ketik H : "))
    d.haha()
    d.yes()
    print("jawaban yang benar", d.kamu)
    print("scor: ", d.nilai)


if __name__ == "__main__":
    while True:
        output()
