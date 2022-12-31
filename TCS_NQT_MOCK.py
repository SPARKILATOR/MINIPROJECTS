class TCS:
    def __init__(self):
        self.c = None
        self.a = 1
        self.b = 1
        self.l1 = [1, 1]
        self.l2 = [2, 3]

    def fib(self):
        n = 1
        while n < 100:
            self.c = self.a + self.b
            self.a = self.b
            self.b = self.c
            self.l1.append(self.c)
            n = n + 1
        return self.l1

    def prime(self):
        n = 1000
        for i in range(5, n):
            if len(self.l2) == 100:
                break
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                self.l2.append(i)
        return self.l2


def output():
    t = TCS()
    out = []
    i = 0
    j = 0
    for z in range(30):
        if z % 2 == 0:
            out.append(t.fib()[i])
            i = i + 1
        else:
            try:
                out.append(t.prime()[j])
                j = j + 1
            except IndexError:
                pass
    return out

o = output()
a = int(input("Enter :: "))
print(o[a-1])
