# Pesapal API Integration

This is a sample API implementation that consumes Pesapal API and provides an endpoint to retrieve the Pesapal iframe URL. The API is implemented using [Flask](https://flask.palletsprojects.com/) framework in Python.

## Requirements

- Python 3.x
- Flask
- Requests library
- BeautifulSoup library
- PyJWT library

## Installation

1. Clone the repository:

   ```shell/terminal type in:
   git clone https://github.com/edwinnab/pesapal-api-integration.git

2. Change the project directory 
    cd pesapal_task
3. Install the required dependencies using pip:
    pip install -r <requirements.txt>

## Configuration
1. Open the api_integration.py file in a text editor.
2. Modify the app.config['SECRET_KEY'] value with a secure secret key of your choice. This key is used for JWT token generation and verification.

## Usage 
0. create a virtual environment and activate it 
    ## Windows OS
    >> my_env/Scripts/activate 
    ## UNIX
    >> source env/bin/activate
1. Start the Flask development server from the terminal/shell:
    NB: ensure your virtual environment is active 
    and you execute the following commands from the working directory
    ## Windows OS
    >>1. set FLASK_APP=api_integration.py 
    >>2. $env:FLASK_ENV="development"
    >>3. set FLASK_ENV=development
    >>4.  $env:FLASK_ENV="development"
    >>5. flask run 
    ## UNIX
    >>1. export FLASK_APP=api_integration.py
    >>2. export FLASK_ENV=development
    >>3. flask run 
    
    

   ![run_server_expected_output](https://github.com/edwinnab/pesapal-api-integration/assets/50041140/f0b0aa80-878b-4160-9d39-b38e00b71813)
    

2. The API will be accessible at http://localhost:5000/.
3. To access the Pesapal iframe URL, send a GET request to the API endpoint or click the urls on display on your browser
>> The response will be in JSON format and contain the Pesapal iframe URLs.

   ![iframes_urls_response](https://github.com/edwinnab/pesapal-api-integration/assets/50041140/55156f35-1820-41c2-868e-ccf8cfcc97f9)

 
>>check the endpoint response on postman to be sure what kind of data you should expect as the response
   
   ![postman_api_response](https://github.com/edwinnab/pesapal-api-integration/assets/50041140/1c58f256-6b4c-4996-977f-293dc7a07d38)

## JWT Authentication
>>1.  JWT (JSON Web Token) authentication is implemented to secure the API endpoint.
>>2.  To access the API, you need to include a JWT token in the Authorization header of the request as a bearer token.
>>3.  The token is generated using a secret key and is validated before granting access to the endpoint.
>>4.  To customize the authentication logic, modify the jwt_authentication_required decorator in the api_integration.py file.


