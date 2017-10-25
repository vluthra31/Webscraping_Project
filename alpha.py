# Website we want to scrape is: https://www.verizonwireless.com/smartphones/samsung-galaxy-s7/
# The documentatio of selenium is here: http://selenium-python.readthedocs.io/index.html

# Please follow the instructions below to setup the environment of selenium
# Step #1
# Windows users: download the chromedriver from here: https://chromedriver.storage.googleapis.com/index.html?path=2.30/
# Mac users: Install homebrew: http://brew.sh/
#			 Then run 'brew install chromedriver' on the terminal
#
# Step #2
# Windows users: open Anaconda prompt and switch to python3 environment. Then run 'conda install -c conda-forge selenium'
# Mac users: open Terminal and switch to python3 environment. Then run 'conda install -c conda-forge selenium'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome('/Users/FlexLex/chromedriver')


csv_file = open('alpha3.csv', 'w')
# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
writer = csv.writer(csv_file)
writer.writerow(['stock', 'ticker', 'date', 'author', 'title', 'link'])
# Page index used to keep track of where we are.
index = 321
while index < 541:
	time.sleep(10)
	try:
		driver.get("https://seekingalpha.com/stock-ideas/quick-picks?page=" + str(index))
		print("Scraping Page number " + str(index))
		index = index + 1

		# Find all the reviews.
		rows = driver.find_elements_by_xpath('//ul[@class="articles-list"]/li')
		print(len(rows))
		for row in rows:
			# Initialize an empty dictionary for each review
			review_dict = {}
			# Use Xpath to locate the title, content, username, date.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			try:
				stock = row.find_element_by_xpath('.//div[@class="a-info"]/span/a').get_attribute('title')
			except:
				stock = ''
			try:
				ticker = row.find_element_by_xpath('.//div[@class="a-info"]/span/a').get_attribute('href')
			except:
				ticket = ''
			try:
				date = row.find_element_by_xpath('.//div[@class="a-info"]/span[3]').text
			except:
				date = ''
			try:
				author = row.find_element_by_xpath('.//div[@class="a-info"]/a').text
			except:
				author = ''
			try:
				title = row.find_element_by_xpath('.//a[@class="a-title"]').text
			except:
				title = ''
			try:
				link = row.find_element_by_xpath('.//a[@class="a-title"]').get_attribute('href')
			except: 
				link = ''

			review_dict['stock'] = stock
			review_dict['ticker'] = ticker
			review_dict['date'] = date
			review_dict['author'] = author
			review_dict['title'] = title
			review_dict['link'] = link
			writer.writerow(review_dict.values())

		# Locate the next button on the page.
		#button = driver.find_element_by_xpath('//div[@id="paging"]/ul/li')
		#driver.execute_script("arguments[0].click();", button)
		#button.click()
	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break


	# Better solution using Explicit Waits in selenium: http://selenium-python.readthedocs.io/waits.html?highlight=element_to_be_selected#explicit-waits

	# try:
	# 	wait_review = WebDriverWait(driver, 10)
	# 	reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
	# 								'//ol[@class="bv-content-list bv-content-list-Reviews bv-focusable"]/li')))
	# 	print(index)
	# 	print('review ok')
	# 	# reviews = driver.find_elements_by_xpath('//ol[@class="bv-content-list bv-content-list-Reviews bv-focusable"]/li')
	#
	# 	wait_button = WebDriverWait(driver, 10)
	# 	button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
	# 								'//div[@class="bv-content-list-container"]//span[@class="bv-content-btn-pages-next"]')))
	# 	print('button ok')
	# 	# button = driver.find_element_by_xpath('//span[@class="bv-content-btn-pages-next"]')
	# 	button.click()
	# except Exception as e:
	# 	print(e)
	# 	driver.close()
	# 	break
