f = open("iiec.txt")
print(f.read())
f.seek(0)
print("second time reading the file by seeking to the first character : ")
print(f.read())
f.seek(0)
print("reading just 4 characters from first character")
print(f.read(4))
print("using tell() to see where our pointer points to :",f.tell())
f.close()