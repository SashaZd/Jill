# Test script for interacting with IBM's Watson
# by Bryan Wiltgen, started 1/11/2015
# Uses the Requests library

# This file is just meant to represent a way to
# interact with Watson.  I'm learning this all
# with you all, so there may be misunderstandings
# in this file and it may not represent best practices.
# Please just view it as a starting point. :)
# -Bryan

import json
import requests

def askWatson(question):
    data={"question": {"questionText" : question}}

    username="gat_administrator"
    password="KYpDpl0e"

    url="https://watson-wdc01.ihost.com/instance/522/deepqa/v1/question"
    headers={"Content-type": "application/json",
             "Accept": "application/json",
             "X-SyncTimeout": "30"}

    print("Asking Watson: " + question)

    response = requests.post(url, data=json.dumps(data), auth=(username, password), headers=headers)
    
    jsonResponse = response.json();

    return jsonResponse;

    

#How to parse the json

print("===== Starting the test ======\n\n")

jsonResponse = askWatson("How do pinecones work?")

evidences = jsonResponse["question"]["evidencelist"]

#the answer
firstAnswer = evidences[0]["text"]

#the document
document = evidences[0]["document"]

print("Watson's answer: " + firstAnswer);

print("\n\n")

print("Document: " + document);
