# ---------------------
# This script downloads Russian lessons 
#	from https://arabic.rt.com/lessons/russian/  - and saves them as pdf documents
# ---------------------

import pdfkit
import requests
import os
import threading
from bs4 import BeautifulSoup as Soup

global url
global target
target = "C:\\languages\\russian"

url = "https://arabic.rt.com/lessons/russian/"


# Validates that the page exists.
def is_valid_page(url):
	request = requests.get(url)
	soup    = Soup(request.content, "html.parser")
	if soup.title.get_text() == "ERROR 404 - RT Arabic":
		return False
	else:
		return True


# Creates a separate directory, and moves to that directory.
def create_lesson_dir(lesson_number):
	# print("Created directory " + lesson_number + " - in" + os.getcwd())

	os.chdir("C:\\languages\\russian")
	# Tries creation. If the folder exists, do nothing.
	try:
		os.mkdir(str(lesson_number))
	except:
		pass
	path = "C:\\languages\\russian\\" + str(lesson_number)
	# Changing current path, to allow file creation in this path.
	os.chdir(path)


# Saves one page of a lesson into a pdf document.
def download_page(url, lesson_number, counter):
	print("\tPage: " + str(counter))
	file_name = str(lesson_number) + "-" + str(counter) + ".pdf"
	pdfkit.from_url(url, file_name)


# Iterates over the pages of a lesson.
# Some lessons have over 30 pages.
# And some lessons have less than 20.
def iterate_lesson(lesson_number):
	print("Downloading lesson " + str(lesson_number))
	create_lesson_dir(lesson_number)
	url = "https://arabic.rt.com/lessons/russian/" + str(lesson_number)
	counter = 1
	while counter < 50:
		page = url + "/" + str(counter)
		if is_valid_page(page):
			# Saves the page as 'lesson_number-counter.pdf' 
			download_page(page, lesson_number, counter)
		else:
			# Return from the function if the page is not valid.
			# This indicates that the lesson has ended. 
			# 		And no more sublessons/pages exist.
			return
		counter = counter + 1

def main():
	for i in range(14, 35):
		# thread = threading.Thread(target=iterate_lesson, args=i)
		iterate_lesson(i)



if __name__ == "__main__":
main()