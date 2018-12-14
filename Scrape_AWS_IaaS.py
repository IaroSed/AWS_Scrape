def ExportAWSIaaS_part(LinkAWS,Categorie,SubCategorie,filename_out, filename_in):

	import urllib.request as urllib
	import re
	import time
	import numpy
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

	AWS_L_out = open(filename_in, 'w')
#	print("Truncating...")
#	AWS_L_out.truncate()

	for p in range(1,1000):

		
		while True:
			try:
				print("Reading page: "+LinkAWS+str(p))
				r = urllib.urlopen(LinkAWS+str(p)).read()
				break
			except:
				print("Oops!  Error occured.. Sleeping for 30 seconds and then trying again!")
				time.sleep(30)
					
		print("Server responded!")
		
		L = re.findall('<a href="/marketplace/pp(\S*?)" data-asin=',str(r))
#		print(L[0::2])
		if (len(L)==0):
			break
		Links[len(Links):] = L[0::2]
#		print(Links)
		time.sleep(random.random())	
	
	for l in range(0,len(Links)):	
		#print(Links[l][0:11])
		#print(Links[0])
		Links[l] = Links[l][0:11]
		
		
	Links_clean = list(set(Links))


	for l in range(0,len(Links_clean)):
#		print(len(L))
#		print(l)
		AWS_L_out.write(Links_clean[l])
		AWS_L_out.write("\n")

	print(len(Links))

		
	AWS_L_out.close()


	AWS_L_out = open(filename_in, 'r')

#	print(AWS_L_out[0])
		
	AWS_E_out = open(filename_out, 'a')
#	print("Truncating...")
#	AWS_E_out.truncate()

	
#	Rank=[0]

	for link in AWS_L_out:
		#print('https://aws.amazon.com/marketplace/pp'+link)
		i = 0
		j = 0
		while j < 3:
			try:
				print("Reading page: "+'https://aws.amazon.com/marketplace/pp'+link)
				browser.get('https://aws.amazon.com/marketplace/pp'+link)
				break
			except:
				print("Oops!  Error occured.. Writing error message!")
				AWS_E_out.write(str(Categorie)+"^"+str(SubCategorie)+"^"+"N/A"+"^"+"N/A"+"^"+'https://aws.amazon.com/marketplace/pp/'+str(link))
				time.sleep(5)
				j = j+1
		
		
		while i < 3:			
			try:
				print("Writing the page: "+'https://aws.amazon.com/marketplace/pp'+link+"   "+str(browser.find_element_by_xpath('.//*[@class="sold-by-value"]').text))
				

				print(str(browser.find_element_by_xpath('.//span[@class="sold-by-value"]/a').get_attribute("href")))
						
				AWS_E_out.write(str(Categorie)+"^"+str(SubCategorie)+"^"+str(browser.find_element_by_xpath('.//*[@class="productTitle"]').text)+"^"+str(browser.find_element_by_xpath('.//*[@class="sold-by-value"]').text)+"^"+str(browser.find_element_by_xpath('.//span[@class="sold-by-value"]/a').get_attribute("href"))+"^"+'https://aws.amazon.com/marketplace/pp'+str(link))
				break
			except:
				print("Oops!  Error occured.. Writing error message!")
				AWS_E_out.write(str(Categorie)+"^"+str(SubCategorie)+"^"+"N/A"+"^"+"N/A"+"^"+'https://aws.amazon.com/marketplace/pp'+str(link))
				time.sleep(5)
				i = i+1
		time.sleep(random.random())
#		AWS_E_out.write(str(Categorie)+"^"+str(SubCategorie)+"^"+NA[0]+"^"+P2[0]+"^"+DES2[0]+"^"+V2[0]+"^"+OS2[0]+"^"+DE2[0]+"^"+DA2[0]+"^"+'https://aws.amazon.com/marketplace/pp'+str(link))

		
		
	AWS_E_out.close()

print("1")
Categorie = "Software Infrastructure"
SubCategorie= "Application Development"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649279011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))

SubCategorie= "Application Servers"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649365011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Application Stacks"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649362011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Big Data"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=6153421011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Databases & Caching"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649364011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Migration"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649368011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Network Infrastructure"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649276011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Operating Systems"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649367011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Security"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649363011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))

Categorie = "Business Software"
SubCategorie= "Business Intelligence"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649336011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Collaboration"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=5018785011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Content Management"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649338011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "CRM"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649339011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "eCommerce"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=4988011011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Education & Research"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=9528502011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Financial Services"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=7496938011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "High Performance Computing"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649340011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Healthcare & Life Sciences"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649342011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Media"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649341011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Project Management"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=4988013011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Storage & Backup"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649337011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))

Categorie = "Developer Tools"
SubCategorie= "Issue & Bug Tracking"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649281011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Monitoring"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649280011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Log Analysis"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=4988009011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Source Control"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649282011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))
SubCategorie= "Testing"
ExportAWSIaaS_part('https://aws.amazon.com/marketplace/search/results?filters=fulfillment_options&fulfillment_options=AMI&searchTerms=&category=2649283011&page=',Categorie, SubCategorie, str("Export_IaaS.txt"),str("LinksIaaS.txt"))