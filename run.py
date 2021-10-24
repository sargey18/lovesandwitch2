import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from the user 
    """
    print("please enter sales data from the last market. ")    # instruct the user to provide the sales data
    print("Data should be six numbers, seperated by commas. ") # also the data we need and how 
    print("Example: 10, 20, 30, 40, 50, 60\n") #example
    
    data_str = input("Enter your data here: ")  # where the user inputs the data 
    print(f"The data provided is {data_str} . ")
    
get_sales_data()