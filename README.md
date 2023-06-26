# Requirements 
  1. Python3
  2. PyJWT
  3. Flask
  4. Requests
  5. git
# Step0: Clone the repo 
## Windows HTTP
```
git clone https://github.com/edwinnab/pesapal-api-integration.git
```
## Windows SSH
```
git clone git@github.com:edwinnab/pesapal-api-integration.git
```
## Unix HTTP
```
git clone https://github.com/edwinnab/pesapal-api-integration.git
```
## Unix SSH
```
git clone git@github.com:edwinnab/pesapal-api-integration.git
```
# Step1: Change directory to the working directory
```
cd 
```
# Step2: Create a virtual environment from the working directory 
## Windows 
```
python3 -m venv my_env
```
## Unix
```
python3 -m venv my_env
```
# Step3: Activate the virtual environment from the working directory
## Windows
```
my_env\Scripts\activate
```
## Unix 
```
source my_env/bin/activate
```
# Step6: Install all the requirements 
```
pip install -r requirements.txt
```
# Step5: Setup the develeopment environment
## Windows
```
$env:FLASK_APP="\api_integration.py"
```
## Unix
```
export FLASK_APP=api_integration.py
```
# Step6: Run the flask app
```
flask run
```
# Step7: Output Screen
  1. App outputs the access token
  2. App request Ipn url ** OPTIONAL SKIP --- PRESS ENTER
  3. App lists all the Ipn registered  ***OPTIONAL SKIP --PRESS ENTER
  4. APP displays the redirect url as a JSON -- CLICK ON URL
# Output response of the redirect_url 
![Screenshot 2023-06-26 124231](https://github.com/edwinnab/pesapal-api-integration/assets/50041140/f7e0a8d5-29e0-41da-9fb2-b1f105eee461)

# Step8: Click on the URL to view the iframe for payment
example screen
![Screenshot 2023-06-23 193425](https://github.com/edwinnab/pesapal-api-integration/assets/50041140/2bbad198-9dbe-47e2-8471-891b869b6c69)

# Step9: Successful payment Screen
![Screenshot 2023-06-23 180616](https://github.com/edwinnab/pesapal-api-integration/assets/50041140/798ad188-1d87-4bf6-b89c-97100b55b917)



