#import necessary modules
from flask import Flask, jsonify
import requests
import re
from bs4 import BeautifulSoup


app = Flask(__name__)
BASE_URL = "https://cybqa.pesapal.com/pesapalv3"


@app.route("/", methods=["GET"])
def get_pesapal_iframe_url():
    try:
        #JWT authntication
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
    
    
if __name__ == '__main__':
    app.run(host='localhost', port=5000)