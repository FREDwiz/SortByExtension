import os, shutil

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

directory = './'

for entry in files(directory):
	# Getting the extension
	print("File: " + entry)
	extension = entry.split(".")[-1]
	extension = extension.upper()
	print("Extension: " + extension)

	# Checking if the folder for that extension exists
	if not os.path.exists(directory + extension):
		os.makedirs(directory + extension)
		print("Created folder for " + extension + " files")

	src = (directory + entry)
	dest = (directory + extension)
	shutil.move(src, dest)

	print("Moved " + entry + " to " + dest)