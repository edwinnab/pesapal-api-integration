#import necessary modules
from flask import Flask, jsonify, request
import requests
import re
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
@app.route("/", methods=["GET"])
def get_pesapal_iframe_url():
    try:
        #data from the api
        response = requests.get(BASE_URL)
        response.raise_for_status()
        
        #parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        
        #find all the scripts withing the body
        script_tags = soup.find_all("script")
        
        #extract the iframe urls from the script tag
        iframe_urls = [script['src'] for script in script_tags if script.get("src")]
        
        #construct the response to be in json 
        #response returns URLS of the static assests as the reponse has no <iframe> tags
        response_data = {
            "iframe_urls": iframe_urls
        }
        #response in json
        return jsonify(response_data), 200
        # Return the HTML doc response as the API response
        # return Response(response.content, content_type='text/html')
        
        
    except requests.exceptions.RequestException as e:
        #handle request errors
        return jsonify({"error": str(e)}), 500
    
    
