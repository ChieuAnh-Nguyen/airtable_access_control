import os
import pyairtable
import pandas as pd


def list_all_values(attribute, table):
    """all_values: lists all values in specified attribute
    records_missing_value: lists records that is missing the specified attribute
    """
    all_values = []
    records_missing_value = []
    for records in table.all():
        if attribute in records['fields'].keys():
            all_values.append(records['fields'][attribute])
        if attribute not in records['fields'].keys():
            records_missing_value.append(records)
    return all_values, records_missing_value


def flag_disallowed_values(csv_name, csv_column_name, all_values):
    """compares all values in airtable to list of allowed values"""
    allowed_values = pd.read_csv(csv_name)
    disallowed_values = []
    for value in all_values:
        if value not in allowed_values[csv_column_name].to_list():
            disallowed_values.append(value)
    return allowed_values, disallowed_values


def flag_duplicate_values(all_values):
    """flag of duplicate occurences. 1 means value exists twice"""
    dup_dict = {}
    for value in all_values:
        duplicate_count = 0
        if (all_values.count(value) > 1) and (value not in dup_dict):
            duplicate_count += 1
            dup_dict[value] = duplicate_count
    return dup_dict


def main():
    # if zsh, store environment variables in .zshrc but if bash, store in .bash_profile
    api_key = str(os.environ.get('AIRTABLE_API_KEY'))
    base_id = str(os.environ.get('BASE_ID'))
    table = pyairtable.Table(api_key, base_id, table_name='poo')

    all_values, records_missing_value = list_all_values('Email', table)
    allowed_values, disallowed_values = flag_disallowed_values(
        'V1_allowed_emails.csv', 'Email Address', all_values)
    dup_dict = flag_duplicate_values(all_values)


if __name__ == "__main__":
    main()
