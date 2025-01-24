import requests

def api_request(username):
    url = "https://api.github.com/users/"+username+"/events"
    response = requests.get(url)

    if response.status_code == 200:
        return fetch_data(response.json())
    elif response.status_code == 404:
        return "Username not found! Verify it and try again!"
    else:
        return "Error. Status code = " + str(response.status_code)

def fetch_data(events):
    print('Output: ')
    for event in events:
        repo = event['repo']['name']

        if event['type'] == 'IssueCommentEvent':
            print(f"- commented on issue {event['payload']['issue']['number']}")
        elif event['type'] == 'PushEvent':
            if len(event['payload']['commits']) == 1:
                print(f"- pushed {len(event['payload']['commits'])} commit to {repo}")
            else:
                print(f"- pushed {len(event['payload']['commits'])} commits to {repo}")
        elif event['type'] == 'IssuesEvent':
            print(f"- created issue {event['payload']['issue']['number']} on {repo}")
        elif event['type'] == 'WatchEvent':
            print(f"- starred {repo}")
        elif event['type'] == 'PullRequestEvent':
            print(f"- created pull request {event['payload']['pull_request']['number']} on {repo}")
        elif event['type'] == 'PullRequestReviewEvent':
            print(f"- reviewed pull request {event['payload']['pull_request']['number']}")
        elif event['type'] == 'PullRequestReviewCommentEvent':
            print(f"- commented on pull request {event['payload']['pull_request']['number']}")
        elif event['type'] == 'CreateEvent':
            print(f"- created {event['payload']['ref_type']} {event['payload']['ref']} on {repo}")
        else:
            print(f"{event['type']}")
    return ''