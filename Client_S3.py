'''
import boto3
import json


with open("Credit.json") as  json_file:
    cred = json.load(json_file)


# créer un client s3
#s3 = boto3.client(
#   's3',
#  aws_access_key_id = cred["aws_access_key_id"],
#  aws_secret_access_key = cred["aws_secret_access_key"]
#   )


# téléchargement de fichiers:
name = "nx-datafactory-test-technique"

s3.download_file(name, "dataengineering/statistics.csv", "statistics.csv")
s3.download_file(name, "dataengineering/european_countries_list.txt", "countries.txt")

print("DONE")

'''