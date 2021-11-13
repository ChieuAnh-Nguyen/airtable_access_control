# airtable_access_control

## About

This project flags duplicate emails and those that are not allowed in your Airtable.

## Additional ideas

1. Delete records whos emails have been flagged.
2. Send records that have been flagged or deleted to admin in an email (gmail API)
3. Parameterize email so it can be any attribute
4. Create daily cron job to send alerts of duplicate and unwanted emails.

## Goals:

1. Learn how to json with csv objects
2. Learn how to use store environmental variables in os
3. Learn how to properly document project: creating venv, documenting in requirements.txt
4. Create reuseable code to keep intruders out of my Airtables!

## Progress tracker:

Start Date: 10/23

🐢 10/23

Stored environment variables. Can flag unwanted emails and duplicate emails.

🐢 10/29

Created functions.

🐢 11/09

Parameterized email so it can be any attribute

🐢 11/12

Added email sender from code snippets repo and added main. Can now send email alerts if Airtable contains duplicates, unwanted emails, or just send all records. Next steps: create cron job to alert
