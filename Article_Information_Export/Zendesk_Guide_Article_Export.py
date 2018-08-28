import requests
import csv
import unicodedata
import getpass

# Set the request parameters
# Change the URL according to what information is desired.
subdomain = input("Enter your Zendesk Subdomain (not full URL, but something such as your company name): ")
url = 'https://' + subdomain +'.zendesk.com/api/v2/help_center/en-us/articles.json?sort_by=title&sort_order=asc'

# Use Your Zendesk Support Sign-On Credentials
user = input("Enter your the Email Address tied to your Zendesk Account: ")
pwd = getpass.getpass("Enter your Zendesk Password: ")

# Path of the outputted csv file
csvfile = 'HelpCenterInformation.csv'

# This loop cycles through all pages of articles, converts the unicode
# to an integer, and writes the integers to an array
output_1 = []
output_1.append("Article ID")
output_2 = []
output_2.append("Article Title")
output_3 = []
output_3.append("URL")
output_4 = []
output_4.append("Vote Sum")
output_5 = []
output_5.append("Vote Count")
output_6 = []
output_6.append("Author ID")
output_7 = []
output_7.append("Section ID")
output_8 = []
output_8.append("Draft (True if Draft, False if not")
while url:
        response = requests.get(url, auth = (user, pwd))
        data = response.json()
        for article in data['articles']:
                article_id = article['id']
                decode_1 = int(article_id)
                output_1.append(decode_1)
        for article in data['articles']:
                title = article['title']
                decode_2 = unicodedata.normalize('NFKD', title)
                output_2.append(decode_2)
        for article in data['articles']:
                article_url = article['html_url']
                decode_3 = unicodedata.normalize('NFKD', article_url)
                output_3.append(decode_3)
        for article in data['articles']:
                vote_sum = article['vote_sum']
                decode_4 = int(vote_sum)
                output_4.append(decode_4)
        for article in data['articles']:
                vote_count = article['vote_count']
                decode_5 = int(vote_count)
                output_5.append(decode_5)
        for article in data['articles']:
                author_id = article['author_id']
                decode_6 = int(author_id)
                output_6.append(decode_6)
        for article in data['articles']:
                section_id = article['section_id']
                decode_7 = int(section_id)
                output_7.append(decode_7)
        for article in data['articles']:
                draft = article['draft']
                decode_8 = bool(draft)
                output_8.append(decode_8)
        print(data['next_page'])
        url = data['next_page']

print("Number of articles:")
print (len(output_1))

# Data Transposition
# nontransposed_data = [("Article ID","Article Title","URL","Vote Sum"), [output_1], [output_2], [output_3],[output_4]]
# transposed_data = zip(*nontransposed_data)

# Write to a csv file
with open(csvfile, 'w') as fp:
    writer = csv.writer(fp, dialect = 'excel')

    #writer.writerow(["Article Id", "Article Title", "URL", "Vote Sum"])
    writer.writerows([output_1])
    writer.writerows([output_2])
    writer.writerows([output_3])
    writer.writerows([output_4])
    writer.writerows([output_5])
    writer.writerows([output_6])
    writer.writerows([output_7])
    writer.writerows([output_8])

