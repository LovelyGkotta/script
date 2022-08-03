import requests
import json
import os

query = """
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            userStatus
            link
            question {
                acRate
                difficulty
                freqBar
                frontendQuestionId: questionFrontendId
                isFavor
                paidOnly: isPaidOnly
                status
                title
                titleSlug
                hasVideoSolution
                hasSolution
                topicTags {
                    name
                    id
                    slug
                }
            }
        }
    }
"""

url = 'https://leetcode.com/graphql/'
r = requests.post(url, json={'query': query})

json_data = json.loads(r.text)
df_date = json_data['data']['activeDailyCodingChallengeQuestion']['date']
df_link = json_data['data']['activeDailyCodingChallengeQuestion']['link']
df_diff = json_data['data']['activeDailyCodingChallengeQuestion']['question']['difficulty']

questionLink = 'https://leetcode.com' + df_link
os.system("open -a 'Google Chrome' " +questionLink)
