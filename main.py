import os
import pyairtable
from airtable_functions import list_all_values, flag_disallowed_values, flag_duplicate_values
from code_snippet.email_credentials import email_address, email_password
from code_snippet.email_sender import create_email, send_email

""" Seting Airtable variables"""
api_key = str(os.environ.get('AIRTABLE_API_KEY'))
base_id = str(os.environ.get('BASE_ID'))
table_name = 'poo'
table = pyairtable.Table(api_key, base_id, table_name)

"""Calling airtable_functions"""
attribute = 'Email'
csv_name = 'csv/V1_allowed_emails.csv'
csv_column_name = 'Email Address'
all_values, records_missing_value = list_all_values(attribute, table)
allowed_values, disallowed_values = flag_disallowed_values(
    csv_name, csv_column_name, all_values)
dup_dict = flag_duplicate_values(all_values)


print(records_missing_value)
""" Email logic"""
# if Airtable contains duplicate
if len(dup_dict) != 0:
    msg = create_email(
        f"Your Airtable '{table_name}' Contains Duplicates in Attribute: {attribute}", email_address, email_address, str(dup_dict))
    send_email(email_address, email_password, msg)
    print(msg)

# if Airtable contains unwanted attribute
if len(disallowed_values) != 0:
    msg = create_email(
        f"Your Airtable '{table_name}' Contains Unwanted Records in Attribute: {attribute}", email_address, email_address, str(disallowed_values))
    send_email(email_address, email_password, msg)
    print(msg)
