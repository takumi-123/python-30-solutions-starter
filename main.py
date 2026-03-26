with open("output.txt", mode="w", encoding="utf-8") as f:
    f.write("Hello, Python!")

with open("output.txt", mode="r", encoding="utf=8") as f:
    content = f.read()
    print(content)

with open("output.txt", mode="a", encoding="utf=8") as f:
    f.write("\nThis is a new line.")
with open("output.txt", mode="r", encoding="utf-8") as f:
    print(f.read())