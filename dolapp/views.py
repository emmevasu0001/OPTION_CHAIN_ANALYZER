from http.client import HTTPResponse
from django.shortcuts import render
from urllib import request
import requests
import pandas as pd
import numpy
import json
import requests
from urllib import request
import requests
import pandas as pd
import numpy
import json

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
# from NSE_Option_Chain_Analyzer import *
import subprocess
def display(request):
    return render(request,'input_form.html')
def input_form(request):
    try:
        # Specify the path to your Python script
        script_path = 'dolapp/NSE_Option_Chain_Analyzer.py'  # Replace with the actual path to your script

        # Run the Python script using subprocess
        result = subprocess.run(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check if the script ran successfully
        if result.returncode == 0:
            # Script executed successfully, you can access the output
            output = result.stdout
            return HttpResponse(f'Script executed successfully.Please come back and run again if you want')
        else:
            # Script encountered an error, you can access the error message
            error_message = result.stderr
            return HttpResponse(f'Script encountered an error: {error_message}', status=500)
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}', status=500)

    nse=NSE()
    # if request.method == 'POST':
    #     nse_index = request.POST.get('nse_index')
    #     strikeprice = request.POST.get('strike_price')
    #     expiry_date = request.POST.get('expiry_date')
    #     option_type = request.POST.get('option_type')

    #     url = 'https://www.nseindia.com/api/option-chain-indices?symbol={0}'.format(nse_index)
    #     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'
    #                             'WebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    #                             'accept-language': 'en,gu;q=0.9,hi;q=0.8',
    #                             'accept-encoding': 'gzip, deflate, br'}
    #     session = request.Session()
    #     requests = session.get(url, headers=headers)
    #     cookies = dict(requests.cookies)
    #     requests = session.get(url, headers=headers,cookies=cookies)


    #     if requests.status_code == 200:
    #         try:
    #             # Extract the content from the response and parse it as JSON
    #             data=requests.text
    #             json_data = json.loads(data)
    #             # print(json.loads(requests))
    #             df = pd.DataFrame(json_data)
    #             df1 = pd.DataFrame(df['filtered']['data']).fillna(0)
    #         except json.JSONDecodeError as e:
    #             print("Error decoding JSON:", e)
    #     else:
    #         print("Request failed with status code:", requests.status_code)

        
    #     if df1:
    #         # data_dict=df1.to_dict(orient='records')
    #         data = []
    #         for i in range(0,len(df1)):
    #             calloi = callcoi = cltp = putoi = putcoi = pltp = 0
    #             stp = df1['strikePrice'][i]

    #             if(df1['CE'][i]==0):
    #                 calloi = callcoi = 0
    #             else:
    #                 calloi = df1['CE'][i]['openInterest']
    #                 callcoi = df1['CE'][i]['changeinOpenInterest']
    #                 cltp = df1['CE'][i]['lastPrice']
    #                 expdate = df1['CE'][i]["expiryDate"]
    #                 underlying = df1['CE'][i]["underlyingValue"]
    #                 diff = (stp - df1['CE'][i]["underlyingValue"])*(stp - df1['CE'][i]["underlyingValue"])
    #             if (df1['PE'][i] == 0):
    #                 putoi = putcoi = 0
    #             else:
    #                 putoi = df1['PE'][i]['openInterest']
    #                 putcoi = df1['PE'][i]['changeinOpenInterest']
    #                 pltp = df1['PE'][i]['lastPrice']

    #             opdata = {
    #                 'CALLOI' : calloi, 'CALLCOI' : callcoi, 'CALL LTP' : cltp, 'STRIKE PRICE' : stp,
    #                 'PUTOI': putoi, 'PUTCOI': putcoi, 'PUT LTP': pltp, 'EXP DATE' : expdate, 'UNDERLYING': underlying, 'diff': diff
    #             }
    #             data.append(opdata)
    #         optionchain = pd.DataFrame(data)
    #         data_dict=optionchain.to_dict(orient='records')
    #         return render(request, 'display_data.html', {'data': data_dict})
    #     # You can process the input data here
    #     # For example, you can save it to a database, perform calculations, etc.

    #     return HttpResponse(f"NSE Index: {nse_index}<br>Strike Price: {strike_price}<br>Expiry Date: {expiry_date}<br>Option Type: {option_type}")

    return render(request, 'input_form.html')