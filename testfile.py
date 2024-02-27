import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import matplotlib.pyplot as plt
import datetime

api_service_name = 'youtubeAnalytics'
api_version = 'v2'

token_file_path = 'C:/Users/sidja/Downloads/token.json'  
with open(token_file_path, 'r') as token_file:
    credentials_data = json.load(token_file)
    credentials = Credentials.from_authorized_user_info(credentials_data)

# Create a YouTube Analytics API service
youtube_analytics = build(api_service_name, api_version, credentials=credentials)

response = youtube_analytics.reports().query(
    ids=f'channel==UCfdPxIRYf1YdhCda_q-goNQ',
    startDate='2023-01-01',
    endDate='2023-01-31',
    metrics='views,likes,dislikes,shares,comments',
    dimensions='day'
).execute()

# Extract statistics from the response
dates = []
views = []
likes = []
dislikes = []
shares = []
comments = []

for row in response.get('rows', []):
    date, view, like, dislike, share, comment = row
    dates.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
    views.append(int(view))
    likes.append(int(like))
    dislikes.append(int(dislike))
    shares.append(int(share))
    comments.append(int(comment))

plt.figure(figsize=(10, 6))
plt.plot(dates, views, label='Views')
plt.plot(dates, likes, label='Likes')
plt.plot(dates, dislikes, label='Dislikes')
plt.plot(dates, shares, label='Shares')
plt.plot(dates, comments, label='Comments')

plt.title('YouTube Analytics Metrics Over Time')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.show()