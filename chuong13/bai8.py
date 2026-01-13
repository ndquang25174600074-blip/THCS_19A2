import os

# Tao thu muc temp_files
os.mkdir("temp_files")

# Tao file file.txt
f = open("temp_files/file.txt", "w")
f.write("Hello")
f.close()

# Doi ten file
os.rename("temp_files/file.txt", "temp_files/new_file.txt")

# Di chuyen file ra thu muc hien tai
os.rename("temp_files/new_file.txt", "new_file.txt")

# Xoa thu muc temp_files
os.rmdir("temp_files")

print("Da hoan thanh bai 8")
