with open("data.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as destination:
    destination.write(content)

print("File copied successfully.")

