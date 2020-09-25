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
for filename in os.listdir(source_folder):
	# Udemy version
	img = Image.open(f'{source_folder}{filename}')
	clean_name = os.path.splitet(filename)[0]
	img.save(f'{dest_folder}{clean_name}.png', 'png')
	print('all done!')
	# my version
	'''
	filename, extension = splitext(file)
	try:
		if (extension == ".jpg"):
			sourcefile = os.path.join(source_folder, file)
			destfile = os.path.join(dest_folder, filename)
			print('input: ' + sourcefile)
			print('output: ' + destfile)
			im = Image.open(sourcefile).convert('RGB')
			im.save(destfile + ".png")
	except OSError:
		print('Cannot covert %s' %file)
	'''
#convert images to png
#save to the new folder