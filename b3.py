name=input("Tên đầy đủ:")

def isThuanNghich(n):
    str1 = str(n);  # ep kieu so n thanh chuoi
    str2 = str1[::-1];  # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;

n = int(input("Nhập số nguyên dương n từ họ tên = "));
print("Các chữ số ", n, "thuận nghịch:", isThuanNghich(n));

