#python script to generate raw.githubuser... links for specified folder in this repo
#run the script from root directory of the repo

import os


BASE_LINK = 'https://raw.githubusercontent.com/DSC-TCET/Assets/main/'

#todo -> add target directory from where to generate the content links
# example -> "image/events/"
# note end with "/"
TARGET_DIRS= ["image/sponsors/","image/events/","image/team/"]

#file names for which we dont want to generate link
EXCLUDE_FILES = ['links.txt','readme.md']

def generate(TARGET_DIR):

	if not TARGET_DIR:
		print('Please add TARGET_DIR and run again')
		return;


	content = os.listdir(TARGET_DIR)

	for ex in EXCLUDE_FILES:
		if ex in content:
			content.remove(ex)

	generated_links = [(BASE_LINK + TARGET_DIR + i + " \n") for i in content]
	with open(TARGET_DIR + "links.txt", "w") as file1:
		file1.writelines(generated_links)
		print(f"added links.txt at {TARGET_DIR}")

for TARGET_DIR in TARGET_DIRS:
	generate(TARGET_DIR)






