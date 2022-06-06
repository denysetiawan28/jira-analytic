# This is a sample Python script.
import http.client
import json
import base64


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

sample_string = "denysetiawan28@gmail.com:HHxwVdAwvCBBSKQZ77FB1359"
sample_string_bytes = sample_string.encode("ascii")
b64 = base64.b64encode(sample_string_bytes)
print(b64)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
conn = http.client.HTTPSConnection("devours.atlassian.net")
payload = json.dumps({
    "expand": [],
    "jql": "project = SC AND issuetype = Epic ORDER BY created DESC",
    "maxResults": 50,
    "fieldsByKeys": False,
    "fields": [
        "issuetype",
        "name",
        "summary",
        "status",
        "assignee",
        "customfield_10015",
        "duedate"
    ],
    "startAt": 0
})
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
conn.request("POST", "/rest/api/3/search", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")

js = json.loads(data)
print(js["expand"])

for i in js["issues"]:
  issue = i["fields"]
  print(issue["summary"])
  print(issue["customfield_10015"])  # start date
  print(issue["duedate"])

