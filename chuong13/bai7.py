import os

os.makedirs("my_project/src", exist_ok=True)
os.makedirs("my_project/docs", exist_ok=True)
os.makedirs("my_project/data", exist_ok=True)

open("my_project/src/main.py", "w").close()
open("my_project/docs/README.md", "w").close()
open("my_project/data/input.txt", "w").close()

print("my_project:", os.listdir("my_project"))
print("src:", os.listdir("my_project/src"))
print("docs:", os.listdir("my_project/docs"))
print("data:", os.listdir("my_project/data"))
