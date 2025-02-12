#Copy a image from one file to another file
# using read() and write() functions

def copy_image(source, destination):
    with open(source,"rb") as src_file:                # using "with" statement, opening the source file in read binary mode
        with open(destination, "wb") as dstn_file:
            dstn_file.write(src_file.read())           # using read() and write() functions, reading from src_file and writing to dstn_file


copy_image("source.jpg", "destination.jpg")
print("Image copied successufully")