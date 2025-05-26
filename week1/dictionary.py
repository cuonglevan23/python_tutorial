#  Dictionary là gì?
# Dictionary là một kiểu dữ liệu trong Python cho phép lưu trữ các cặp khóa-giá trị (key-value pairs).
# Mỗi khóa là duy nhất và được sử dụng để truy cập giá trị tương ứng.
# Dictionary có thể chứa các kiểu dữ liệu khác nhau như số, chuỗi, danh sách, tuple, và thậm chí là các dictionary khác.
# Cách tạo một dictionary:
english_to_vn = {
    "hello": "xin chào",
    "goodbye": "tạm biệt",
    "please": "làm ơn",
    "thank you": "cảm ơn bạn",
    "yes": "vâng",
    "no": "không"
    # "key": "value"  # Cặp khóa-giá trị
    # không được thêm trùng lặp các giá trị key
}

print(english_to_vn["hello"])  # Truy cập giá trị bằng khóa
print(english_to_vn["goodbye"])  # Truy cập giá trị bằng khóa
# Thêm một cặp khóa-giá trị mới vào dictionary
english_to_vn["welcome"] = "chào mừng"
# In ra toàn bộ dictionary
print(english_to_vn)
# Cập nhật giá trị của một khóa
english_to_vn["thank you"] = "cảm ơn"
# In ra toàn bộ dictionary sau khi cập nhật
print(english_to_vn)
# Xóa một cặp khóa-giá trị khỏi dictionary
del english_to_vn["no"]
# In ra toàn bộ dictionary sau khi xóa
print(english_to_vn)
# Lặp qua các cặp khóa-giá trị trong dictionary
for key, value in english_to_vn.items():
    print(f"key {key}: value:{value}")

print(english_to_vn.get("hello"))# Sử dụng phương thức get để truy cập giá trị
print(english_to_vn.get("nonexistent_key", "Không tìm thấy khóa"))  # Trả về giá trị mặc định nếu khóa không tồn tại