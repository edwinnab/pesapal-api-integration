#import necessary modules
from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from functools import wraps
import jwt



app = Flask(__name__)
# Change to a secure secret key
app.config['SECRET_KEY'] = 'your-secret-key'



BASE_URL = "https://cybqa.pesapal.com/pesapalv3"

# JWT authentication decorator
def jwt_authentication_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "JWT token is missing"}), 401
        
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "JWT token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid JWT token"}), 401
        
        return f(*args, **kwargs)
    return decorated_function

# API route with JWT authentication
# @app.route("/", methods=["GET"])
# def get_pesapal_iframe_url():
#     try:
#         #data from the api
#         response = requests.get(BASE_URL)
#         response.raise_for_status()
        
#         #parse the HTML response using BeautifulSoup
#         soup = BeautifulSoup(response.content, "html.parser")
        
#         # #find all the scripts withing the body
#         script_tags = soup.find_all("script")
#         #check if the script is found
#         if script_tags:
#             #extract the iframe urls from the script tag
#             iframe_urls = [script['src'] for script in script_tags if script.get("src")]
#             #construct the response to be in json 
#             #response returns URLS of the static assests as the reponse has no <iframe> tags
#             response_data = {
#                 "iframe_urls": iframe_urls
#             }
#             #response in json
#             return jsonify(response_data), 200
#         else:
#             return jsonify({"error": "Iframe URL not found"}), 500
    
#         # Return the HTML doc response as the API response
#         # return Response(response.content, content_type='text/html')        
#     except requests.exceptions.RequestException as e:
#         #handle request errors
#         return jsonify({"error": str(e)}), 500

# POST Request 
# Authentication endpoint 
#generate the access_token 
#endpoint https://cybqa.pesapal.com/pesapalv3/api/Auth/RequestToken

api_url = f"{BASE_URL}/api/Auth/RequestToken"

consumer_key = "qkio1BGGYAXTu2JOfm7XSXNruoZsrqEW"
consumer_secret = "osGQ364R49cXKeOYSpaOnT++rHs="

def generate_access_token():
    #Request Headers
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    #Request Payload
    payload = {
    "consumer_key": consumer_key,
    "consumer_secret": consumer_secret
    }
    
    #response with the token
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        access_token = response.json()["token"]
        print("Access Token", access_token)
    else:
        print("Failed to generate access token. Status code:", response.status_code)
        
generate_access_token()

#POST Request 
# register an IPN (Instant Payment Notification) URL 
# endpoint https://cybqa.pesapal.com/pesapalv3/api/URLSetup/RegisterIPN
api_url = f"{BASE_URL}/api/URLSetup/RegisterIPN"
bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3VzZXJkYXRhIjoiZWQ2MTkwMGYtZGNiMy00NjM2LWIxNGUtY2U1MGQwYzk2M2I1IiwidWlkIjoicWtpbzFCR0dZQVhUdTJKT2ZtN1hTWE5ydW9ac3JxRVciLCJuYmYiOjE2ODM4NzYyMjksImV4cCI6MTY4Mzg3OTgyOSwiaWF0IjoxNjgzODc2MjI5LCJpc3MiOiJodHRwOi8vY3licWEucGVzYXBhbC5jb20vIiwiYXVkIjoiaHR0cDovL2N5YnFhLnBlc2FwYWwuY29tLyJ9.MB7rLpOvWCHOq3WfPKydR2LoRCirmQFjUuBKhjLNnP8"
url = input("Enter url")
notification_type="GET"
def register_ipn_url(url, notification_type):
    # Request Headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    
    # Request Payload
    payload = {
        "id": url,
        "ipn_notification_type": notification_type
    }
    
    # Make the POST request to register IPN URL
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("IPN URL registered successfully!")
    else:
        print("Failed to register IPN URL. Status code:", response.status_code) 

# Example usage
register_ipn_url(url, notification_type)

