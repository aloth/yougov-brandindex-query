# Python functions to query the YouGov BrandIndex API.
# Tested with Python 3.7.3
#
# https://github.com/aloth/yougov-brandindex-query

import requests
import urllib.parse

def querySingleBrandTimeline(filename, apiParameters):
    # apiParameters:
    # region - the region to which the brand belongs.
    # sector - the sector to which the brand belongs.
    # brand_id - the ID of the brand from which to retrieve datapoints from.
    # start_date - the starting date from when to retrieve datapoints, in the format YYYY-MM-DD.
    # end_date - the ending date until when to retrieve datapoints, in the format YYYY-MM-DD.
    # scoring - the scoring option to use, within "total" (includes all respondents, including unaware respondents), "aware" (excludes unaware respondents) and "opinion" (excludes both unaware respondents and respondents who don't have a positive or negative opinion of the brand).
    # moving_average - (optional) the timeline moving average, in days, that will be applied to the scores, as an integer. Defaults to 1.
    # filters - (optional) filters in the format [:demo_filters][:metric_filters].
    # metrics - (optional) specific metrics, if you don't want all of them. If you want more than one, just separate them by a forward slash (/).
    
    with requests.Session() as session:

        response = session.post('https://api.brandindex.com/v0/login', {'email': email, 'password': password})
        print(response.text)
        
        baseUrl = 'https://api.brandindex.com/v0/timeline/file.csv?'
        url = baseUrl + urllib.parse.urlencode(apiParameters)
        print(url)

        download = session.get(url)
        decoded_content = download.content.decode('utf-8')

        with open(filename, 'wb') as f:  
            f.write(download.content)

def queryMultiBrandTimeline(filename, apiParameters):
    # apiParameters:
    # brand - a parameter in the format region:sector_id:brand_id[:demo_filters][:metric_filters][:metrics]. Can be provided multiple times - if so, multiple brands will be listed in the response data.
    # sector - a parameter in the format region:sector_id[:demo_filters][:metric_filters][:metrics]. Can be provided multiple times - if so, multiple sectors will be listed in the response data.
    # custom_sector - a parameter in the format region:custom_sector_id[:demo_filters][:metric_filters][:metrics]. Can be provided multiple times - if so, multiple custom sectors will be listed in the response data.
    # start_date - the starting date from when to retrieve datapoints, in the format YYYY-MM-DD.
    # end_date - the ending date until when to retrieve datapoints, in the format YYYY-MM-DD.
    # scoring - the scoring option to use, within "total" (includes all respondents, including unaware respondents), "aware" (excludes unaware respondents) and "opinion" (excludes both unaware respondents and respondents who don't have a positive or negative opinion of the brand).
    # moving_average - (optional) the timeline moving average, in days, that will be applied to the scores, as an integer. Defaults to 1.
    # period_type - (optional) the type of period, if rolling up the datapoints. Can be "day", "week", "month" or "year". Defaults to "day".
    # period_size - (optional) the integer size of each period - e.g., 2 for rolling up "every 2 weeks". Defaults to 1.
    
    with requests.Session() as session:

        response = session.post('https://api.brandindex.com/v0/login', {'email': email, 'password': password})
        print(response.text)
        
        baseUrl = 'https://api.brandindex.com/v0/timeline/multi-brand-file.csv?'
        url = baseUrl + urllib.parse.urlencode(apiParameters)
        print(url)

        download = session.get(url)
        decoded_content = download.content.decode('utf-8')

        with open(filename, 'wb') as f:  
            f.write(download.content)
            
# Your YouGov API credentials:
email = 'xxx'
password = '123'

# Example to query a single-brand timeline:
querySingleBrandTimeline('db.csv', {'region':'de', 'sector':'135', 'brand_id':'135003', 'scoring':'opinion', 'start_date':'2015-01-01', 'end_date':'2019-05-15', 'moving_average':'28'})

# Example to query a multi-brand timeline:
queryMultiBrandTimeline('db-multi.csv', {'brand':'de:135:135003', 'brand':'de:135:601569', 'brand':'de:135:601570', 'scoring':'opinion', 'start_date':'2019-01-01', 'end_date':'2019-05-15', 'moving_average':'28'})
