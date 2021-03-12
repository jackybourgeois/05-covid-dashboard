# Import relevant functions from the module 'covid'
from covid import download_summary, download_confirmed_per_country
# Import the object Flask and request from flask module
from flask import Flask

# Import and setup logging
import logging
log_format = "[%(levelname)s] - %(asctime)s : %(message)s in %(module)s:%(lineno)d"
logging.basicConfig(filename='covid.log', format=log_format, level=logging.INFO)

# Import the json module to manipulate JSON from a file
import json

# Create a webserver object called 'COVID Dashboard' and keep track of it in the variable server
server = Flask('COVID Dashboard')

# Define an HTTP route / to serve the dashboard home web page
@server.route('/')
# Define the function 'index()' and connect it to the route /
def index():
  # Return the static file 'index.html'
  return server.send_static_file('index.html')

# Define an HTTP route /summary to serve the summary chart
@server.route('/summary')
# Define the function 'serve_summary()' and connect it to the route /summary
def serve_summary():
  """
  Download the summary from the COVID19 API, extract the 'Countries' values (skip 'Globals'). The chart description is returned with template and data.
  """
  # Load json template from summary.json
  json_template = json.load(open("templates/summary.json"))
  # Download summary from the COVID API
  json_data = download_summary()
  # Add the data to the template
  json_template["data"]["values"] = json_data["Countries"]
  # Send the chart description to the client
  return json_template

# Define an HTTP route /new to serve the new count worldwide chart
@server.route('/new')
# Define the function 'serve_summary_new()' and connect it to the route /new
def serve_summary_new():
  """
  Download the summary from the COVID19 API, extract the 'new' values (skip totals) and format the data. The chart description is returned with template and data.
  """
  # Load json template from new.json
  json_template = json.load(open("templates/new.json"))
  # Download summary from the COVID API
  json_data = download_summary()
  # Create an empty list of value to receive filtered and formated data
  values = []
  # For all data in the "Global" structure
  for key in json_data["Global"]:
    # Keep the 'New' entries (skip overall totals)
    if key.startswith("New"):
      # Create a dictionary with 'category' and 'value'
      value = {"category": key, "value": json_data["Global"][key]}
      # Add the dictionary to the list of values
      values.append(value)
  # Add the data to the template
  json_template["data"]["values"] = values
  # Send the chart description to the client
  return json_template

# Define an HTTP route /netherlands to serve the chart of the netherlands
@server.route('/netherlands')
# Define the function 'serve_netherlands_history()' and connect it to the route /netherlands
def serve_netherlands_history():
  """
  Download the confirmed cases of the netherlands from the COVID API. The chart description is returned with template and data.
  """
  # Load json template from history.json
  json_template = json.load(open("templates/history.json"))
  # Download the confirmed cases of the netherlands from the COVID API
  json_data = download_confirmed_per_country("netherlands")
  # Add the data to the template
  json_template["data"]["values"] = json_data["data"]
  # Send the chart description to the client
  return json_template

# Start the web server
server.run('0.0.0.0')