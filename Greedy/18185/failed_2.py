import sys, time

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
length = len(data) - 1

result = 0

class A():
    def __init__(self, data, length, result):
        self.data = data
        self.length = length
        self.result = result

    def proc(self, n, num):
        self.result += 2*n + 1
        for i in range(n):
            self.data[num+i] -= 1

    def main(self):
        #while True:
        for num in range(n):
            if num+2 <= self.length and self.data[num+2] > 0 and self.data[num+1] > 0 and self.data[num] > 0:
                dn, dn1, dn2 = self.data[num], self.data[num+1], self.data[num+2]
                if dn2 and dn1 and dn <= dn1 and dn1 <= dn2:
                    self.proc(3, num)
                    break
                elif dn1 and dn <= dn1:
                    self.proc(2, num)
                    break
                else:
                    self.proc(1, num)
                    break
            elif num+1 <= self.length and self.data[num+1] > 0 and self.data[num] > 0:
                dn, dn1 = self.data[num], self.data[num+1]
                if dn1 and dn <= self.data[num+1]:
                    self.proc(2, num)
                    break
                else:
                    self.proc(1, num)
                    break
            elif self.data[num] > 0:
                self.proc(1, num)

        c = 0
        #c = sum(self.data)
        for i in data:
            c += i
        print(f"data : {data}")
        if c == 0:
            return
        else:
            self.main()



a = time.time()
b = A(data, length, result)
b.main()
print(b.result)
a = time.time() - a
print(a)
            

        

