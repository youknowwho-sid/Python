from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Set your API key
api_key = '' 

# Set the path to your client secrets JSON file
client_secrets_file = ''

# Set the API service name and version
api_service_name = 'youtubeAnalytics'
api_version = 'v2'

# Set the OAuth 2.0 scopes
scopes = ['https://www.googleapis.com/auth/youtube.readonly']

# Authenticate using OAuth2 with InstalledAppFlow
flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes=scopes)
credentials = flow.run_local_server(port=8080)

# Save the credentials for later use
with open('', 'w') as token:
    token.write(credentials.to_json())

# Create a YouTube Analytics API service
youtube_analytics = build(api_service_name, api_version, credentials=credentials)

# Example: Get the number of views for a specific video
response = youtube_analytics.reports().query(
    ids=f'', #Set Channel ID 
    startDate='2023-01-01',
    endDate='2023-01-31',
    metrics='views'
).execute()

# Extract statistics from the response
print(f"Number of Views: {response['rows'][0][0]}")
