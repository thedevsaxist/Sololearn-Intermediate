# One way to avoid wasting resources by making sure that files are always closed after they have been used,
# is to use try and finally.

try:
    f = open("filename.txt")
    cont = f.read()
    print(cont)
finally:
    f.close()

# This ensures that the file is always closed, even if an error occurs