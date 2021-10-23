import os
from pyairtable import *
import pandas as pd

# if zsh, store environment variables in .zshrc but if bash, store in .bash_profile
api_key = str(os.environ.get('AIRTABLE_API_KEY'))
base_id = str(os.environ.get('BASE_ID'))
table_name = "V1"
table = Table(api_key, base_id, table_name)

all_email = []
missing_email = []

# if email address attribute exists, add to all_emails
for records in table.all():
    if list(records['fields'])[0] == 'Email Address':
        all_email.append(list(records['fields'].values())[0]) 
        # print((list(records['fields'].values())[0]))
# # if email address attribute does not exists, add to missing_email
    else:
        missing_email.append(records)


allowed_emails = pd.read_csv('V1_allowed_emails.csv')
disallowed_emails = []

# flagging disallowed emails
for email in all_email:
    if email not in allowed_emails['Email Address'].to_list():
        disallowed_emails.append(email)
print(disallowed_emails)

# flagging duplicate emails
dup_email = []
count = 0
for email in all_email:
    if (all_email.count(email) > 1) and (email not in dup_email):
        print(email)
        dup_email.append(email)
        count+=1
print("Number of duplicate emails:", count)
