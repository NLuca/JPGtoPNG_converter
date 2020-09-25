import sys
import os
from os.path import splitext
from PIL import Image

#grab first and second arguments
source_folder = sys.argv[1]
dest_folder = sys.argv[2]

#check is new/ exists, if not create
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

#loop through Pokedex
for file in os.listdir(source_folder):
	filename, extension = splitext(file)
	try:
		if (extension == ".jpg"):
			sourcefile = os.path.join(source_folder, file)
			destfile = os.path.join(dest_folder, filename)
			print(sourcefile)
			print(destfile)
			im = Image.open(sourcefile).convert('RGB')
			im.save(destfile + ".png")
	except OSError:
		print('Cannot covert %s' %file)

#convert images to png
#save to the new folder