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
import urllib

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

    # DSLfall2014 & bidstudent

#How to parse the json

print("===== Starting the test ======\n\n")

# jsonResponse = askWatson("How do pinecones work?")

# evidences = jsonResponse["question"]["evidencelist"]

# #the answer
# firstAnswer = evidences[0]["text"]

# #the document
# document = evidences[0]["document"]

# print("Watson's answer: " + firstAnswer);

# print("\n\n")

# print("Document: " + document);

# password_mgr = urllib.HTTPPasswordMgrWithDefaultRealm()
# top_level_url = "http://dilab.cc.gatech.edu/biologue/protected/articles/"
# password_mgr.add_password(None, top_level_url, "bidstudent", "DSLfall2014")

# handler = urllib.HTTPBasicAuthHandler(password_mgr)
# # opener = urllib.build_opener(handler)

# # opener.open(a_url)

# # urllib.request.install_opener(opener)

# proxy_support = urllib.request.ProxyHandler({})
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)

# docList = urllib.urlopen("http://dilab.cc.gatech.edu/biologue/protected/articles/")
# for eachLine in docList:
#     print eachLine



