import sys
import os

# Lấy đường dẫn tuyệt đối đến thư mục thu_vien_chung
thu_vien_chung_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "thu_vien_chung")
)

sys.path.append(thu_vien_chung_path)

import xu_ly_so

print("Đã import xu_ly_so thành công!")

so = 17
print(xu_ly_so.kiem_tra_so_nguyen_to(so))
