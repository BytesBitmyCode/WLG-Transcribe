import requests
from requests.auth import HTTPBasicAuth
import os

# Set your base URL, username, and password
base_url = 'https://recordings.ipfone.com/api'
username = 'jpozo@gwardlaw.com'
password = 'Julie97!21'

# Authenticate
auth = HTTPBasicAuth(username, password)
headers = {'Accept': 'application/json'}

# Get the list of calls
calls_response = requests.get(f'{base_url}/v2/calls.json', auth=auth, headers=headers)

# Check the status code and print the response
print("Status Code:", calls_response.status_code)
print("Response JSON:", calls_response.json())

if calls_response.status_code == 200:
    # Assuming 'calls' is the correct key, based on correct API documentation
    calls = calls_response.json().get('calls', [])
    
    if not calls:
        print("No calls found in the response.")
    else:
        # Directory to save audio files
        audio_files_directory = r"C:\Users\mbarreau\OneDrive - The Ward Law Group, PL\Documents\Software Engineer\WLG Transcribe\raw mp3 files"
        
        for call in calls:
            call_id = call.get('call_id')  # Adjust based on the actual response structure
            if call_id:
                # Retrieve file for playback - adjust the endpoint as per your API documentation
                file_response = requests.get(f'{base_url}/v2/calls/{call_id}/file', auth=auth, stream=True)
                
                if file_response.status_code == 200:
                    file_path = os.path.join(audio_files_directory, f'call_{call_id}.mp3')
                    
                    with open(file_path, 'wb') as f:
                        for chunk in file_response.iter_content(chunk_size=128):
                            f.write(chunk)
                    
                    print(f'Downloaded call recording to {file_path}')
                else:
                    print(f'Failed to download recording for call {call_id}. Status Code: {file_response.status_code}')
            else:
                print(f'No call_id found for a call in the response.')
else:
    print(f"Failed to retrieve calls. Status Code: {calls_response.status_code}")
    print("Response JSON:", calls_response.json())
    # Handle error based on the API's error response structure
