#python script to generate raw.githubuser... links for specified folder in this repo
#run the script from root directory of the repo

import os


BASE_LINK = 'https://raw.githubusercontent.com/DSC-TCET/Assets/main/'

#todo -> add target directory from where to generate the content links
# example -> "image/events/"
TARGET_DIR = "image/events/"


def generate():

	if not TARGET_DIR:
		print('Please add TARGET_DIR and run again')
		return;


	content = os.listdir(TARGET_DIR)
	generated_links = [(BASE_LINK + TARGET_DIR + i + " \n") for i in content]
	with open(TARGET_DIR + "links.txt", "w") as file1:
		file1.writelines(generated_links)
		print(f"added links.txt at {TARGET_DIR}")

generate()






