import urllib.request as urllib
import re
import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import sys
import pandas as pd

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
profile = webdriver.FirefoxProfile()
path = "C:\\Python36\\selenium\\geckodriver.exe"
	
browser = webdriver.Firefox(executable_path=path, firefox_profile=profile,firefox_binary=binary)
Links=list()
Links_clean = list()
Solutions = list()

AWS_L_out = open('LinksSaaS.txt', 'w')
print("Truncating...")
AWS_L_out.truncate()

for p in range(1,78):
	print("Reading page: "+str(p))
	r = urllib.urlopen('https://aws.amazon.com/marketplace/search/results?searchTerms=&filters=fulfillment_options&fulfillment_options=SAAS&page='+str(p)).read()
	L = re.findall('<a href="/marketplace/pp(\S*?)" data-asin=',str(r))
#	print(L[0::2])
	Links[len(Links):] = L[0::2]
#	print(Links)
	time.sleep(random.random())

for l in range(0,len(Links)):	
	Links[l] = Links[l][0:11]
		
		
Links_clean = list(set(Links))


for l in range(0,len(Links_clean)):
#	print(len(L))
#	print(l)
	AWS_L_out.write(Links[l])
	AWS_L_out.write("\n")


	
AWS_L_out.close()


AWS_L_out = open('LinksSaaS.txt', 'r')
	
AWS_E_out = open('ExportAWSSaaS.txt', 'w')
print("Truncating...")
AWS_E_out.truncate()


for link in AWS_L_out:

	print("Reading page: "+'https://aws.amazon.com/marketplace/pp'+link)
	browser.get('https://aws.amazon.com/marketplace/pp'+link)
			
	try:
		print("Writing the page: "+'https://aws.amazon.com/marketplace/pp'+link)			
		AWS_E_out.write(str(browser.find_element_by_xpath('.//*[@class="productTitle"]').text)+"^"+str(browser.find_element_by_xpath('.//*[@class="sold-by-container"]').text)+"^"+str(browser.find_element_by_xpath('.//span[@class="sold-by-container"]/a').get_attribute("href"))+"^"+'https://aws.amazon.com/marketplace/pp'+str(link))
		#break
	except:
		print("Oops!  Error 1 occured.. Writing error message!")
		time.sleep(2)
		try:
			print("Writing the page: "+'https://aws.amazon.com/marketplace/pp'+link)
			AWS_E_out.write(str(browser.find_element_by_xpath('.//h1[@id="title"]').text)+"^"+str(browser.find_element_by_xpath('.//ul[@id="vendor-info-links"]/li').text)+"^"+str(browser.find_element_by_xpath('.//ul[@id="vendor-info-links"]/li/a').get_attribute("href"))+"^"+'https://aws.amazon.com/marketplace/pp'+str(link))
			#break
		except:
			print("Oops!  Error 2 occured.. Writing error message!")
			AWS_E_out.write("N/A"+"^"+"N/A"+"^"+"N/A"+"^"+'https://aws.amazon.com/marketplace/pp'+str(link))
			time.sleep(2)

	time.sleep(3)


