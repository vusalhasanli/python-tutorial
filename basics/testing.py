
path = "files.timestamp"

with open(path, "+r") as plain_text:
    data = plain_text.readlines()
    print(data)
