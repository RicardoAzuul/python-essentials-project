import gspread
from google.oauth2.service_account import Credentials

# Constant variables, written in all caps

# IAM configuration
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# credentials
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True:
        print("Please enter sales data form the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10, 20, 30, 40, 50, 60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")        

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Inside the try, converts all strings into integers.
    Raises ValueError if strings cannot be converted into int, 
    or if there aren't exactly 6 values.
    """
    try:
        # for each in value in values do method int on value
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:  # e is Python standard shorthand for error
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True
        


get_sales_data()
