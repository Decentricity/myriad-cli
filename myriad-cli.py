import requests
import json
import os
import os
import subprocess
import requests
import time
import random
import pywhatkit as kit
from PIL import Image

import html

from datetime import datetime

magiclink=""
anonmode=False
user_email=""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'

try:
    term_size = os.get_terminal_size()
    width=term_size.columns
except:
    width=64
print('♥' * width)
myriadlogo="""
  .=++=:   :+++=.
 *=    =%*#-    =+     ::     .:                              =
++  .=+-  .=+=   #:    @@:   .%@:             =              +@
+=  ++-     -*-  #:    @%%.  %%@  %:  #  %++* %  +#+++%  *#++#@
+=    .=#**=.    #:    @#-%.#=-@   %.#   @    @  @=  =@ -@   *@
+=   -++: -++:   #:    @# +@* -@    @    @    @  %%==%@  %*-=%@
=*===:       :===%:                 #    

Decentralized (web3 and Federated) Free Speech Social Media Blockchain.
Command Line Interface Client for https://app.myriad.social"""

print(f"{bcolors.PURPLE}{myriadlogo}{bcolors.ENDC}")
print('♥' * width)

while user_email=="":
    print(f"{bcolors.BOLD}Please enter your Myriad email or type anon to try Myriad anonymously.{bcolors.ENDC}{bcolors.CYAN}\nIf you do not have a Myriad account, you can create one by going to https://app.myriad.social/login and clicking the Email button.\n{bcolors.BLUE}If you already have a Myriad account that you created with a crypto wallet, go to https://app.myriad.social/settings?section=email to add an email account. \n{bcolors.RED}For security reasons, the CLI client does not support wallet logins yet. (It will. Wen? SOON)")
    print(f"\n{bcolors.ENDC}{bcolors.BOLD}Enter your Myriad email, or 'anon', below:")
    user_email = input("> ")
    
if user_email=="anon": anonmode=True
# Replace with your callback URL
callback_url = "https://app.myriad.social/login"

# Base URL for the Myriad API
base_url = "https://api.myriad.social"

# Function to send a magic link to the user's email address
def send_magic_link(email, callback):
    global magiclink
    # Myriad API endpoint for sending a magic link
    api_endpoint = f"{base_url}/authentication/otp/email"

    # Prepare the payload with the email address and callback URL
    payload = {
        "email": email,
        "callbackURL": callback
    }

    # Send a POST request to the Myriad API to send a magic link
    response = requests.post(api_endpoint, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Magic link successfully sent to {email}.")
        print(f"Click on that link first before continuing.")
        print(f"Then copy the link from the email and put em here:")
        magiclink=input(">")
    else:
        print(f"Error sending magic link: {response.status_code}")
        print(response.text)
        return response.status_code

        
def authenticate(token):
    api_endpoint =f"{base_url}/authentication/login/otp"
    payload = {
        "token": token
    }
    response=requests.post(api_endpoint, json=payload)

    if response.status_code == 200:
        return response.json()
    return None
    
if not anonmode:
# Send a magic link to the user's email address
    try:
        statcode=send_magic_link(user_email, callback_url)
    except:
        user_email=""
        while user_email=="": 
            user_email = input("Unable to send email. Check your email address and give it to me again: ")
            statcode=send_magic_link(user_email, callback_url)
    while statcode==422:
        user_email = input("Email invalid. Check your email address and give it to me again: ")
        statcode=send_magic_link(user_email, callback_url)
    
    auth=magiclink.replace(callback_url+"?token=","")

#print(auth)

    accesstoken=authenticate(auth)
#print(accesstoken)





if not anonmode: 
    at=(accesstoken.get('token').get('accessToken'))
else:
    at=""
#print(at)
if not anonmode: 
    un=(accesstoken.get('user').get('username'))
else:
    un=""
    
    
    


pages="10"
# exampl fr testin
twitter_url = "https://twitter.com/decentricity/status/1655727173351743489"


base_url = "https://api.myriad.social"

base_url = "https://api.myriad.social"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + at,
}

base_url = "https://api.myriad.social"
def search_user(username):
    search_url = f"{base_url}/people/search"
    response = requests.get(search_url, params={"id": user_id})

    if response.status_code == 200:
        users = response.json()
        for user in users:
            if user.get("username") == username:
                return user
    return None
def user_id(username):
    api_url = f"{base_url}/users/{username}"
    print(api_url)
    response = requests.get(api_url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        user_id = data["id"]
        print(f"User ID for {username}: {user_id}")
        return user_id
    else:
        print(f"Error: {response.status_code}")
        
def get_all_posts():
    posts_url = f"{base_url}/user/posts?pageLimit={pages}" #?page_number=
    response = requests.get(posts_url)

    if response.status_code == 200:
        return response.json()
    return None

def filter_user_posts(posts, user_id):
    if not user_id=="": 
        return [post for post in posts['data'] if post.get("createdBy") == str(user_id)]
    else:
        return [post for post in posts['data']]




def flatten(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, list):
        return ' '.join(flatten(item) for item in data)
    else:
        if 'children' in data:
            return flatten(data['children'])
        elif 'text' in data and data['text'].strip():
            return data['text']
        else:
            return ''


def display_posts(posts):
    
    post_text=""
    for i, post in enumerate(posts, 1):
        
        print(f"Post {i}")
        data_str = post.get('text')
        try:
        # Try to parse and flatten the data as JSON
            data = json.loads(data_str)
            flattened_data = flatten(data)
        except json.JSONDecodeError:
            # If it's not valid JSON, treat it as plain text
            flattened_data = data_str
        print(f"Text: {flattened_data}")

        
        try:
            imagelist=post.get('asset').get('images')
            imageurl=imagelist[0]['original']
            print(f"Image: {imageurl}")
            
            # Download the image and save it locally
            response = requests.get(imageurl, stream=True)
            response.raise_for_status()
            filename = f"temp_image_.jpg"
            with open(filename, 'wb') as fd:
                for block in response.iter_content(4096):
                    fd.write(block)
            time.sleep(1)  # Wait for a second
            
            # Convert the image to ASCII art
            ascii_art = kit.image_to_ascii_art(filename)
            print(ascii_art)
            
        except Exception as e:
            print("No image. Error:", str(e))
        if post.get('url'):
            print(f"Imported from Twitter URL: {post.get('url')}")
        print("----------")
        post_text=post_text+f"{post.get('text')}\n"
    return post_text



def import_twitter_post(twitter_url, importer, selected_timeline_ids):
    base_url = "https://api.myriad.social"
    api_endpoint = f"{base_url}/user/posts/import"
    

    data = {
        "url": twitter_url,
        "importer": importer,
        "selectedTimelineIds": selected_timeline_ids,
    }
    
    # Send a POST request to the Myriad API to import the Twitter post
    response = requests.post(api_endpoint, headers=headers, json=data)
    

    if response.status_code == 200:
        print("Twitter post successfully imported into Myriad.")
        imported_post_data = response.json()
        return imported_post_data
    else:
        print(f"Error importing Twitter post: {response.status_code}")
        print(response.text)
        return None


def get_user_notifications():
    api_endpoint = f"{base_url}/user/notifications"
    response = requests.get(api_endpoint, headers=headers)
    
    if response.status_code == 200:
        notifications = json.loads(response.text)  
        #print(notifications)
        print(f"You have {len(notifications['data'])} notifications.\n")
        for i, notification in enumerate(notifications['data'], 1):
            print(f"Notification {i}:")
            print(f"ID: {notification.get('id')}")
            print(f"Type: {notification.get('type')}")
            print(f"Message: {notification.get('message')}")
            print(f"Timestamp: {notification.get('createdAt')}") 
            print(f"From: {notification.get('from')}")
            print(f"To: {notification.get('to')}")
            print("----------\n")
    else:
        print(f"Error fetching notifications: {response.status_code}")
        return None

def create_myriad_post(title, text_blocks, platform='myriad', visibility='public'):
    api_endpoint = f"{base_url}/user/posts"

    # obtain the user id of the current user
    response = requests.get(f"{base_url}/users/{un}", headers=headers)
    if response.status_code == 200:
        user_data = json.loads(response.text)
        created_by = user_data.get("id")
    else:
        print("Error retrieving user ID.")
        return None

    # Get the current date and time
    now = datetime.now()

    # Format the datetime object as a string
    createdAt = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    # Format the text as a JSON string
    text = json.dumps([
        {"type": "p", "children": [{"text": block}]} for block in text_blocks
    ])

    post_data = {
        "title": title,
        "text": text,
        "rawText": '\n'.join(text_blocks),
        "platform": platform,
        "createdAt": createdAt,
        "visibility": visibility,
        "createdBy": created_by,
        "metric": {
            "upvotes": 0,
            "downvotes": 0,
            "discussions": 0,
            "debates": 0,
            "comments": 0,
            "tips": 0,
        },
        "isNSFW": False,
        "mentions": [],
        "selectedUserIds": [],
        "selectedTimelineIds": [],
        "banned": False,
        "originCreatedAt": createdAt,
        "createdAt": createdAt,
        "visibility": visibility,
        "createdBy": created_by,
    }
    
    print(post_data)
    response = requests.post(api_endpoint, headers=headers, json=post_data)
    print(response)
    if response.status_code == 200:
        print("Post created successfully!")
    else:
        print(f"Error creating post: {response.status_code}")

command=""
while not command=="exit":
    print(f"{bcolors.PURPLE}")
    print('♥' * width)

    print("p: show posts\nf: filter posts by Myriad username")
    if not anonmode: print("n: notifications\ni: import a Twitter post\nw: write a Myriad post")
    print(f"exit: Go back to the shell.\n\nCurrently searching within last {pages} posts. Type ps to change this setting.")
    command = input(f"> {bcolors.ENDC}")
    print('♥' * width)
    print(myriadlogo)
    print(command)
    print("\n")
    if command=="i" or command.lower() =="import":
        twitter_url = input("Enter Twitter URL to import: ")
        importer = un
        selected_timeline_ids = input("Enter selected timeline IDs (comma-separated if more than one): ").split(',')

        imported_post_data = import_twitter_post(twitter_url, importer, selected_timeline_ids)
    
    elif command=="n" or command.lower()=="notifications":
        get_user_notifications()
        
    elif command=="w":
        content = ["First paragraph", "Second paragraph", "Third paragraph"]
        create_myriad_post("My Post Title", content)
        
    elif command=="ps" or command.lower()=="pages":

        newpages=input("Enter how many posts per search: ")
        if newpages.isnumeric(): 
            pages=newpages 
        else: 
            print("Not a number. Exiting.")
            
    elif command=="p" or command.lower()=="posts":

        target_un=""
        all_posts = get_all_posts()

        userid=""

        filtered_posts = filter_user_posts(all_posts, userid)
        if filtered_posts:
            #print(filtered_posts)
            post_text=display_posts(filtered_posts)
        else:
            print(f"No posts found.")
            
    elif command=="f" or command.lower()=="filter":
        if anonmode:
            print("Enter Myriad username for me to filter for.")
        else:
            print("Whose posts? (Enter blank for your own or * to see all recent posts)")
            
        target_un=input("> ")
        if target_un=="": 
            target_un=un
        elif target_un=="*":
            target_un=""
        all_posts = get_all_posts()
        print(target_un)
        if not target_un=="": 
            user = search_user(target_un)
            print(user)
            if user:
                user_id = user.get("id")
            userid=user_id(target_un)
        else:
            userid=""
#if all_posts:
#    print(f"Raw JSON data of all posts: {all_posts}")
        filtered_posts = filter_user_posts(all_posts, userid)
        if filtered_posts:
            #print(filtered_posts)
            print(f"Filtered posts by user {target_un}/{userid}:")
            post_text=display_posts(filtered_posts)
        else:
            print(f"No posts found for user {target_un}")

    
# Display the imported post data
#    if imported_post_data:
#        print(json.dumps(imported_post_data, indent=2))



