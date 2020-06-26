#Fetch Internet Resources Using The urllib Package


import urllib.request   #This module for opening and reading URLs
response = urllib.request.urlopen('http://www.google.com') #the urlopen method with request object returns a response object for the URL requested.
the_page = response.read() #Read the content of the file "response"
print(the_page)
