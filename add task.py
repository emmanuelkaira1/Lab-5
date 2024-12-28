import re


file_path = 'task_add.txt'
with open(file_path, 'r') as file:
    text = file.read()


date_pattern = r'\s(?:\d{4}[-/.]\d{2}[-/.]\d{2}|\d{2}[-/.]\d{2}[-/.]\d{4})'
email_pattern = r'\s[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
website_pattern = r'\shttps?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


dates = re.findall(date_pattern, text)
emails = re.findall(email_pattern, text)
websites = re.findall(website_pattern, text)


dates = [date.strip() for date in dates]
emails = [email.strip() for email in emails]
websites = [website.strip() for website in websites]


print("Dates found:", dates[:5])
print("Emails found:", emails[:5])
print("Websites found:", websites[:5])