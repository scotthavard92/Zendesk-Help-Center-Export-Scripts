import requests
import csv
import unicodedata


# Set the request parameters
# Change the URL according to what information is desired. 
url = 'https://yoursubdomain.zendesk.com/api/v2/help_center/en-us/articles.json?sort_by=title&sort_order=asc'

# Use Your Zendesk Support Sign-On Credentials
user = 'ZD Username'
pwd = 'ZD Password'

# Path of the outputted csv file
csvfile = 'localpath/filename.csv'

# This loop cycles through all pages of articles, converts the unicode
# to an integer, and writes the integers to an array
output = []
while url:
	response = requests.get(url, auth = (user, pwd))
	data = response.json()
	for article in data['articles']:
		vote_sum = article['vote_sum']
		decode = int(vote_sum)
		output.append(decode)
	print(data['next_page'])
	url = data['next_page']

# Print number of articles 
print("Number of articles:")
print (len(output))

#Write to a csv file
with open(csvfile, 'w') as fp:
    writer = csv.writer(fp, dialect = 'excel')
    writer.writerows([output]) 
