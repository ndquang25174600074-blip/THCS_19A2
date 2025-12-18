data = {'An': 8, 'Bình': 7, 'Chi': 8, 'Đông': 9}
grouped = {}

for name in data:
    score = data[name]
    if score not in grouped:
        grouped[score] = [name]
    else:
        # Không dùng append() nếu muốn an toàn tuyệt đối, 
        # nhưng đề bài chỉ cấm phương thức list cụ thể (sort, reverse...)
        grouped[score] += [name] 
print(grouped)