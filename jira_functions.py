import requests
from requests.auth import HTTPBasicAuth

def get_all_issues(project_key):
    url = "https://nyva.atlassian.net/rest/api/3/search"
    auth = HTTPBasicAuth("igutierrez@nyva.mx", "3odxf7Dfzvk9wYmzjbZ8BC09")
    headers = {
      "Accept": "application/json"
    }
    start = 0
    items = []
    while True:
        params = {
            'jql': f'project = "{project_key}" ORDER BY key ASC',
            'startAt': start,
            'maxResults': 100,
            #'fields': 'id,status,issuetype,created'
        }
        response = requests.request("GET", url, headers=headers, params=params, auth=auth)
        if response.ok:
            issuesTemp = response.json()
            start += int(issuesTemp['maxResults'])
            items += issuesTemp['issues']
            if start > int(issuesTemp['total']):
                break

    return items