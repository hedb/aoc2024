import os

def create_empty_file(file_name):
    directory = os.path.dirname(file_name)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_name, "w") as f:
        f.write("")

for i in range (2,30):
    create_empty_file(f"d{i}.py")
    create_empty_file(f"input/d{i}_sample")
    create_empty_file(f"input/d{i}")