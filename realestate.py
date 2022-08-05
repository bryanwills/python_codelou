import requests
import pandas as pd
import sqlalchemy
import openpyxl
import psycopg2

headers = {
    'authority': 'api2.realtor.ca',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,cs;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'visid_incap_2269415=DRpcY4I3SjKFMfalMxSftyaK6WIAAAAAQUIPAAAAAACvrLYGe+e3wDZmQZfgEaBA; nlbi_2269415=B6YSQ7YtUCMAjnPWn2FYxQAAAACYHLiQKXa5Yo8sEYT9lH/D; incap_ses_1291_2269415=SdugIV1PHwRJVXABPo7qESaK6WIAAAAA8vWAvOTCm3r54LL1BaCVtA==; incap_ses_116_2269415=FM63c0UCPQHIXBz0Kh6cASeK6WIAAAAA9WPFdt5xRRbegjs061rpqw==; reese84=3:W3xEMitJn4FeyQaF2XIXWQ==:p7Gd6DFbHB7lgs8ZiewNBgGqjQLo3wb7ZgLM5HEqdiD5sN4Mr44u810tBQhqV2vjU2U1jZhk1XUUaxH3SE6rRKOZt2IsJBaY91rEmL/BfA9TmyLmjn+zJzFmdGtmAiChQgjCUv8dENZu7G/vy9dAv2VS2qzg0HdfHvG9N6GpzCGi9tItYSFdAC8W6Hf1v7ru/vUdI9Gswb/t3vvtWsVgd0VwG0/MuhT3PJHUsJuK826Fry8SmmvyvBkYGWDIE/+2lgErv/802OoFzhg3SoNuJAU5wWhb00pBiZGi02wn5GRKByp4s/E2VoVX6arUlcELR5JUvMfIAehQsgzhbw4HOSKf5nJaZYKSYpYhSV/lyUoqp54LPEcLOcJiPaisJj2GJPoKHsQqa2LX7yNuFJCgwYL/h/luyeyPr/f5IKQnqGA=:/enhsFfOjcbixgt8+8usYgkzfKJI11l1g99of43Onuc=; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; ASP.NET_SessionId=4je5mml0zgqlvsnfaxs3egfb; visid_incap_2271082=B8sI/rNOS1O+7SuN27HKhkmK6WIAAAAAQUIPAAAAAADhnJ+CcKEEfvlCTsuuOLuJ; nlbi_2271082=shHQdkaMZgmv7s1ENo2IPAAAAAD0GfZzBej4n1ca1rAudqyl; incap_ses_116_2271082=fbUKUHhRXEGMgxz0Kh6cAUmK6WIAAAAAlXQi/sn9Rh1WHoAG/5A3fg==; nlbi_2269415_2147483392=u6DgadTQhS/ycA2tn2FYxQAAAABhO27gJcvY6w7tSWqOqotq',
    'dnt': '1',
    'origin': 'https://www.realtor.ca',
    'referer': 'https://www.realtor.ca/',
    'sec-ch-ua': '^\\^.Not/A)Brand^\\^;v=^\\^99^\\^, ^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

data = {
  'ZoomLevel': '10',
  'LatitudeMax': '45.61508',
  'LongitudeMax': '-75.15382',
  'LatitudeMin': '44.88320',
  'LongitudeMin': '-76.44608',
  'Sort': '6-D',
  'PropertyTypeGroupID': '1',
  'PropertySearchTypeId': '1',
  'TransactionTypeId': '2',
  'Currency': 'FXUSDCAD',
  'RecordsPerPage': '12',
  'ApplicationId': '1',
  'CultureId': '1',
  'Version': '7.0',
  'CurrentPage': '1'
}

response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)

#check status code from the request
print(response)
#should get back a 200 response
#create json object
result_json = response.json()

#output keys
result_json.keys()
#find the data we are looking for
#Address
#Bedrooms
#Bathrooms
#Agent Name
#Area Code
#Phone Number
#Price

#starting point for the data
result_items = result_json['Results']

len(result_items)
# should get back 12

# address of first result using the index of '0'
result_items[0]['Property']['Address']['AddressText']
# targeting the 'Property' key to get the address since it is within the property key.
# Going further to get the specific data I am looking for, I keep going down the 'keys' until I have just the street address I need.
# Get bedroom information
result_items[0]['Building']['Bedrooms']
# Get bathrooms information
result_items[0]['Building']['BathroomTotal']
# Get the Agent Name. Since the Agent is part of a list, need to use an index to extract the information.
result_items[0]['Individual'][0]['Name']
# Get the area code, using index 0 since there is a fax number as well
result_items[0]['Individual'][0]['Phones'][0]['AreaCode']
# Get the phone number
result_items[0]['Individual'][0]['Phones'][0]['PhoneNumber']

#put everything together in a loop to iterate the data needed, putting information into a list
# Create empty lists, these are the data points I want to extract from the webpage
address = []
bedrooms = []
bathrooms = []
agent_name = []
area_code = []
phone_number = []
price = []

# iterate over each item on the page
for result in result_items:

    # address
    try:
        address.append(result['Property']['Address']['AddressText'])
    except:
        address.append('')

    # bedrooms
    try:
        bedrooms.append(result['Building']['Bedrooms'])
    except:
        bedrooms.append('')

    # bathrooms
    try:
        bathrooms.append(result['Building']['BathroomTotal'])
    except:
        bathrooms.append('')

    # Agent Name
    try:
        agent_name.append(result['Individual'][0]['Name'])
    except:
        agent_name.append('')

    # area code
    try:
        area_code.append(result['Individual'][0]['Phones'][0]['AreaCode'])
    except:
        area_code.append('')

    # phone number
    try:
        phone_number.append(result['Individual'][0]['Phones'][0]['PhoneNumber'])
    except:
        phone_number.append('')

    # price
    try:
        price.append(result['Property']['Price'])
    except:
        price.append('')

#print out the 12 addresses from the first page of search results
print(address)

#Pandas Dataframe
# Take all the data from the for loop above and put it into a Pandas Dataframe, each list should return a column
df_realtor = pd.DataFrame({'Address': address, 'Bedrooms': bedrooms, 'Bathrooms': bathrooms, 'Agent Name': agent_name, 'Area Code': area_code, 'Telephone': phone_number, 'Price': price})

# Display the data frame, will show all 12 addresses and related information for each listing on the page.
print(df_realtor)

#put everything together in a loop to iterate through all 50 pages of search results
# Create empty lists, these are the data points I want to extract from the webpage
address = []
bedrooms = []
bathrooms = []
agent_name = []
area_code = []
phone_number = []
price = []

# iterate over the pages 1 to 51 using the CurrentPage key value as the variable in the for loop to get data from all the pages available.
for i in range(1,51):

    headers = {
        'authority': 'api2.realtor.ca',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,cs;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'visid_incap_2269415=DRpcY4I3SjKFMfalMxSftyaK6WIAAAAAQUIPAAAAAACvrLYGe+e3wDZmQZfgEaBA; nlbi_2269415=B6YSQ7YtUCMAjnPWn2FYxQAAAACYHLiQKXa5Yo8sEYT9lH/D; incap_ses_1291_2269415=SdugIV1PHwRJVXABPo7qESaK6WIAAAAA8vWAvOTCm3r54LL1BaCVtA==; incap_ses_116_2269415=FM63c0UCPQHIXBz0Kh6cASeK6WIAAAAA9WPFdt5xRRbegjs061rpqw==; reese84=3:W3xEMitJn4FeyQaF2XIXWQ==:p7Gd6DFbHB7lgs8ZiewNBgGqjQLo3wb7ZgLM5HEqdiD5sN4Mr44u810tBQhqV2vjU2U1jZhk1XUUaxH3SE6rRKOZt2IsJBaY91rEmL/BfA9TmyLmjn+zJzFmdGtmAiChQgjCUv8dENZu7G/vy9dAv2VS2qzg0HdfHvG9N6GpzCGi9tItYSFdAC8W6Hf1v7ru/vUdI9Gswb/t3vvtWsVgd0VwG0/MuhT3PJHUsJuK826Fry8SmmvyvBkYGWDIE/+2lgErv/802OoFzhg3SoNuJAU5wWhb00pBiZGi02wn5GRKByp4s/E2VoVX6arUlcELR5JUvMfIAehQsgzhbw4HOSKf5nJaZYKSYpYhSV/lyUoqp54LPEcLOcJiPaisJj2GJPoKHsQqa2LX7yNuFJCgwYL/h/luyeyPr/f5IKQnqGA=:/enhsFfOjcbixgt8+8usYgkzfKJI11l1g99of43Onuc=; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; ASP.NET_SessionId=4je5mml0zgqlvsnfaxs3egfb; visid_incap_2271082=B8sI/rNOS1O+7SuN27HKhkmK6WIAAAAAQUIPAAAAAADhnJ+CcKEEfvlCTsuuOLuJ; nlbi_2271082=shHQdkaMZgmv7s1ENo2IPAAAAAD0GfZzBej4n1ca1rAudqyl; incap_ses_116_2271082=fbUKUHhRXEGMgxz0Kh6cAUmK6WIAAAAAlXQi/sn9Rh1WHoAG/5A3fg==; nlbi_2269415_2147483392=u6DgadTQhS/ycA2tn2FYxQAAAABhO27gJcvY6w7tSWqOqotq',
        'dnt': '1',
        'origin': 'https://www.realtor.ca',
        'referer': 'https://www.realtor.ca/',
        'sec-ch-ua': '^\\^.Not/A)Brand^\\^;v=^\\^99^\\^, ^\\^Google',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    data = {
    'ZoomLevel': '10',
    'LatitudeMax': '45.61508',
    'LongitudeMax': '-75.15382',
    'LatitudeMin': '44.88320',
    'LongitudeMin': '-76.44608',
    'Sort': '6-D',
    'PropertyTypeGroupID': '1',
    'PropertySearchTypeId': '1',
    'TransactionTypeId': '2',
    'Currency': 'FXUSDCAD',
    'RecordsPerPage': '12',
    'ApplicationId': '1',
    'CultureId': '1',
    'Version': '7.0',
    'CurrentPage': str(i),
    }

    # response
    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)

    # create json object
    result_json = response.json()

    # result items
    result_items = result_json['Results']

    for result in result_items:

        # address
        try:
            address.append(result['Property']['Address']['AddressText'])
        except:
            address.append('')

        # bedrooms
        try:
            bedrooms.append(result['Building']['Bedrooms'])
        except:
            bedrooms.append('')

        # bathrooms
        try:
            bathrooms.append(result['Building']['BathroomTotal'])
        except:
            bathrooms.append('')

        # Agent Name
        try:
            agent_name.append(result['Individual'][0]['Name'])
        except:
            agent_name.append('')

        # area code
        try:
            area_code.append(result['Individual'][0]['Phones'][0]['AreaCode'])
        except:
            area_code.append('')

        # phone number
        try:
            phone_number.append(result['Individual'][0]['Phones'][0]['PhoneNumber'])
        except:
            phone_number.append('')

        # price
        try:
            price.append(result['Property']['Price'])
        except:
            price.append('')

# Take all the data from the for loop above and put it into a Pandas Dataframe, each list should return a column. Re-use the data frame we already created, taking to account the iteration of all the page results.
df_realtor = pd.DataFrame({'Address': address, 'Bedrooms': bedrooms, 'Bathrooms': bathrooms, 'Agent Name': agent_name, 'Area Code': area_code, 'Telephone': phone_number, 'Price': price})

# output the data frame to show all results. Running this cell generates 600 rows of real estate listings
print(df_realtor)

#Store it into Excel
df_realtor.to_excel('realtor_multiple_pages.xlsx', index=False)

#Store information into postgres
# create an sqlalchmey engine using the postgres username and password, port 5432 (db port)
engine = sqlalchemy.create_engine('postgresql://postgres:12345@localhost:5432')
# send dataframe to sql using the name real_estate as the table name and passing in the engine parameter
df_realtor.to_sql('real_estate_new', engine)