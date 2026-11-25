"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
ten = "An"          # str
tuoi = 15           # int
diem_tb = 8.5       # float
dang_hoc = True     # bool

print("Giá trị và kiểu dữ liệu:")
print(ten, type(ten))
print(tuoi, type(tuoi))
print(diem_tb, type(diem_tb))
print(dang_hoc, type(dang_hoc))

# TODO 2: Hoán đổi giá trị 2 biến không dùng biến tạm
a = 10
b = 20
a, b = b, a
print("Sau khi hoán đổi: a =", a, ", b =", b)

# TODO 3: Augmented assignment
# Thực hiện lần lượt phép cộng, trừ, nhân và chia lấy phần nguyên.
x = 100
x += 20
print("Sau += 20:", x)
x -= 10
print("Sau -= 10:", x)
x *= 2
print("Sau *= 2:", x)
x //= 5
print("Sau //= 5:", x)

# TODO 4 (Thử thách): Multiple assignment
ho, ten, tuoi = "Nguyen", "An", 15
print(f"Họ tên: {ho} {ten}, {tuoi} tuổi")
