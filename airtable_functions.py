import os
import pyairtable
import pandas as pd

def list_all_emails(table):
    all_email = []
    """if email address attribute exists, add to all_emails"""
    for records in table.all():
        if 'Email' in records['fields'].keys():
            all_email.append(records['fields']['Email'])
    return all_email

def report_missing_emails(table):
    """if email address attribute does not exists, add to records_missing_email"""
    records_missing_email = []
    for records in table.all():
        if 'Email' not in records['fields'].keys():
            records_missing_email.append(records)
    return records_missing_email

def flag_disallowed_emails(all_email, allowed_emails):
    """compares all emails in airtable to list of allowed email"""
    disallowed_emails = []
    for email in all_email:
        if email not in allowed_emails['Email Address'].to_list():
            disallowed_emails.append(email)
    return disallowed_emails

def flag_duplicate_emails(all_email):
    """count number of duplicate emails and flag them"""
    dup_email = []
    duplicate_count = 0
    for email in all_email:
        if (all_email.count(email) > 1) and (email not in dup_email):
            dup_email.append(email)
            duplicate_count+=1
    return dup_email, duplicate_count

def main():
    # if zsh, store environment variables in .zshrc but if bash, store in .bash_profile
    api_key = str(os.environ.get('AIRTABLE_API_KEY'))
    base_id = str(os.environ.get('BASE_ID'))
    table_name = "poo"
    table = pyairtable.Table(api_key, base_id, table_name)

    allowed_emails = pd.read_csv('V1_allowed_emails.csv')
    all_email = list_all_emails(table)
    records_missing_email = report_missing_emails(table)
    dup_email, duplicate_count = flag_duplicate_emails(all_email)
if __name__ == "__main__":
    main()