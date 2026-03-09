import pathlib as pt


# Creating and Checking path with pathlib

file = pt.Path("example.txt")
print(file.exists())  # Check if file exists

file.write_text("Hello, World!This is second time writing into same file")  # Write text
print(file.read_text())  # Read text




# Working with Directories


# folder = pt.Path("my_folder")
# folder.mkdir(exist_ok=True)  # Create directory

# for p in folder.iterdir():
#     print(p.name)



#writing text files

# file = pt.Path("greeting.txt")
# file.write_text("Hello Python!")

#Reading text files
# content = file.read_text()
# print(content)
# print(type(content))

# or this 
# print(file.read_text())

