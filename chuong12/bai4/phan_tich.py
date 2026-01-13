from du_lieu.danh_sach import sap_xep_tang_dan
from du_lieu.tu_dien import lay_gia_tri

ds = [5, 2, 9, 1, 7]
td = {"a": 10, "b": 20}

print("Danh sách sau sắp xếp:", sap_xep_tang_dan(ds))
print("Giá trị khóa 'a':", lay_gia_tri(td, "a"))
