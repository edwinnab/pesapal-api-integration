# #import Flask object from flask package
from flask import Flask, jsonify
import requests
import re
from bs4 import BeautifulSoup

# #create flask application instance
app = Flask(__name__)
# #API endpoint
BASE_URL = "https://cybqa.pesapal.com/pesapalv3"

# #create our decorator(converts a py function into a flask view function)
# # view function converts the function return value into an HTTP response to be displayed by the HTTP client
@app.route("/", methods=["GET"])
def api_testing():
    try:
        #JWT authntication
        
        #data from the api
        response = requests.get(BASE_URL)
        response.raise_for_status()
        #parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        #find the container element that wraps the iframes
        script_tags = soup.find_all("script")
        
        
        iframe_urls = [script['src'] for script in script_tags if script.get("src")]
        
        response_data = {
            "iframe_urls": iframe_urls
        }
        #response in json
        return jsonify(response_data), 200
    except requests.exceptions.RequestException as e:
        #handle request errors
        return jsonify({"error": str(e)}), 500
    
    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)