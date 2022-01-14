name=input("Tên:")

n = int(input('Nhập n bằng độ dài tên: '))
d = dict()
for i in range(1, n+1):
    d[i] = i*i
print(d)