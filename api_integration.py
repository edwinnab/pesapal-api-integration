#import necessary modules
from flask import Flask, jsonify, request
import requests
from functools import wraps
import jwt
import json

app = Flask(__name__)
BASE_URL = "https://cybqa.pesapal.com/pesapalv3"

# POST Request 
# Authentication endpoint 
#generate the access_token 
#endpoint /api/Auth/RequestToken
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
        global access_token
        access_token = response.json()["token"]
        print("Access Token: ")
        print(access_token, "\n\n")
    else:
        print("Failed to generate access token. Status code:", response.status_code)     
generate_access_token()

#POST Request 
# register an IPN (Instant Payment Notification) URL 
# endpoint /api/URLSetup/RegisterIPN
api_url = f"{BASE_URL}/api/URLSetup/RegisterIPN"
def register_ipn_url():
    
    url = input("Enter your IPN URL: ")
    notification_type = "GET"
    # Request Headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    # Request Payload
    payload = {
        "id": url,
        "ipn_notification_type": notification_type
    }
    
    # Make the POST request to register IPN URL
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("\n\n", "IPN URL registered successfully!", "\n\n")
        print("Response: ", "\n\n\n", response.json())
    else:
        print("Failed to register IPN URL. Status code:", response.status_code) 
        print("Error: ", "\n\n\n", response.json())
register_ipn_url()

#GET Request
# fetch all registered IPN URLs for a Pesapal merchant account
# endpoint  /api/URLSetup/GetIpnList
api_url = f"{BASE_URL}/api/URLSetup/GetIpnList"
def get_registered_ipns():
    # Request Headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    # Make the GET request to fetch registered IPN URLs
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        ipn_list = response.json()
        print("\n\n", "Registered IPN URLs:")
        for ipn in ipn_list:
            print(ipn)
    else:
        print("\n\n", "Failed to fetch registered IPN URLs. Status code:", "\n\n\n", response.status_code)
get_registered_ipns()

#POST Request
#Submit Order Request Endpoint 
#endpoint  /api/Transactions/SubmitOrderRequest
api_url = f"{BASE_URL}/api/Transactions/SubmitOrderRequest"
def submit_order_request():
    # Request Headers
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    # Request Payload
    #Todo create a form later 
    payload = {
        "id": "AA1122-3345ZU",
        "currency": "KES",
        "amount": 100.00,
        "description": "Payment description goes here",
        "callback_url": "https://www.myapplication.com/response-page",
        "redirect_mode": "",
        "notification_id": "2f1e48ef-de37-4a49-9cd5-deacf4174c39",
        "branch": "Store Name - DUKA",
        "billing_address": {
            "email_address": "john.doe@example.com",
            "phone_number": "0723xxxxxx",
            "country_code": "KE",
            "first_name": "John",
            "middle_name": "",
            "last_name": "Doe",
            "line_1": "Pesapal Limited",
            "line_2": "",
            "city": "",
            "state": "",
            "postal_code": "",
            "zip_code": ""
        }
    }
    
    # Make the POST request to submit order request
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        if "redirect_url" in response_data:
            payment_redirect_url = response_data["redirect_url"]
            json_data = json.dumps({"payment_redirect_url": payment_redirect_url}, indent=4)
            print("\n\n", "Payment redirect URL (JSON): ")
            print(json_data)
        else:
            print("\n\n", "Redirect URL not found in the response.")
    else:
        print("Failed to submit order request. Status code:", response.status_code)
        print("Error:", response.json())    
submit_order_request()

# Change to a secure secret key
app.config['SECRET_KEY'] = 'your-secret-key'
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
jwt_authentication_required(register_ipn_url)



