"""
Author:Sunil Kumar
Date:28-July-2018
This Code is writen in Python3.6, using this script you can add data directly to GoogleSheet using GoogleSheet Api.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Defining Function 
def gsheet(sname,skey,rowdata,index):
    scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    cred=ServiceAccountCredentials.from_json_keyfile_name(skey,scope)
    client=gspread.authorize(cred)
    sheet=client.open(sname).sheet1
    sheet.insert_row(rowdata,index)
    return (print("Data Inserted Sucessfully"))

rowdata=[Column_1,Column_2,Column_3,Column_4]    #'The data should be in a list'.The no of element in list append automatically to different respectively.
sheetname='xxxxxxxxxx'                           #This is your googlesheet name in string form.
sheetkey='xxxxxx.json'                           #This is file path of your key downloded after creating credentials(In ".json" format).
Index=1                                          #This is index at which your data is added to the sheet.

gsheet(sheetname,sheetkey,rowdata,index)         #Calling Function
    
    
    
