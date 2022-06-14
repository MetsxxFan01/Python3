Filename_with_fullpath = r"C:\Users\thesi\Desktop\test2.txt"

with open(Filename_with_fullpath, "a") as File_object:
    File_object.write("This is a sentence")
    
with open(Filename_with_fullpath, "r") as File_object:
    print(File_object.read())