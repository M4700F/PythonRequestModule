import requests # including the 'requests' module in python, it will give us the access 
                # to print the get and post request

url = 'https://www.example.com' # This is the url we are using 
response = requests.get(url) # This is a function call which invokes the get() function which sends a 
                             # a get request to the url

if response.status_code == 200:  # Check if the request was successful. 200 in HTTP represents a successful
                                 # request
    headers = response.headers # fetching the response header. Response header refer to the additional
                               # sent by the server along with requested data. It contains metadata 
                               # about the response itself like server type, content type, date and time
                               # of the response
    print("Response Headers:")
    for header in headers: # header variable holds each individual header of the headers dictionary
        print(f"{header}: {headers[header]}") # f string - formatter string {} is a placeholder
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
