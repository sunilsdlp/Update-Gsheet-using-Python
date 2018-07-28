# Update-Gsheet-using-Python
This Code is writen in Python3.6, using this code you can add data directly to GoogleSheet using GoogleSheet Api.


Package Required:
  1.gspread
  2.oauth2client
	3.PyOpenSSL

SetUp:
  Sign in to your google Account.
  Head to Google Developers Console and create a new project (or select the one you have.)
  Under "API & auth", in the API enable "Drive API".
  Enabled APIs
  Go to "Credentials" and choose "New Credentials > Service Account Key".
  Google Developers Console
  You will automatically download a JSON file with this data.
  Download Credentials JSON from Developers Console
  This is how this file may look like:
  {
      "private_key_id": "2cd … ba4",
      "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
      "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
      "client_id": "473 … hd.apps.googleusercontent.com",
      "type": "service_account"
  }
  In the next step you'll need the value of client_email from the file.
  Go to your spreadsheet and share it with a client_email from the step above. Otherwise you'll get a SpreadsheetNotFound exception when     trying to access this spreadsheet with gspread.
  Now you can read this file, and use the data when constructing your credentials:
