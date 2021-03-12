"""
Access to Coronavirus COVID19 API: https://covid19api.com
Postman: https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""

# Import get function from requests to send HTTP requests
from requests import get
# Import the logging module to log errors
# from logging import error
import logging

# Create a constant 'URL_API' with the url of the api
URL_API = "http://api.covid19api.com"


def download_summary():
    """
  Send HTTP request to API /summary and return the response in JSON format.
  
  API details: https://documenter.getpostman.com/view/10808728/SzS8rjbc#00030720-fae3-4c72-8aea-ad01ba17adf8
  
  """
    # Send the HTTP request
    response = get(f'{URL_API}/summary')
    # Check for the HTTP response status 200 (OK)
    if response.status_code == 200:
        # Return the response as JSON
        return response.json()
    # Otherwise, something went wrong
    else:
        # Log the error message
        logging.error(f'An error has occurred: HTTP status {response.status_code}')
        # Return an empty result
        return {}


def download_confirmed_per_country(country):
    """
  Send HTTP request to API /country/<country>/status/confirmed to receive the daily number of confirmed cases for the requested country. Return the response in JSON format.
  
  API details: https://documenter.getpostman.com/view/10808728/SzS8rjbc#b07f97ba-24f4-4ebe-ad71-97fa35f3b683
  
  country -- the name of the requested 
  """
    # Send the HTTP request
    response = get(f'{URL_API}/country/{country}/status/confirmed')
    # Check for the HTTP response status 200 (OK)
    if response.status_code == 200:
        # Return the response as JSON
        logging.info('Serve Dutch Data')
        return { "data" : response.json() }
    # Otherwise, something went wrong
    else:
        # Log the error message
        logging.error(f'An error has occurred: HTTP status {response.status_code}')
        # Return an empty result
        return {}
