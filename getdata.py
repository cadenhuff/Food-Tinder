import requests
import json

def get_data_func(location,distance,price):
    url = 'https://api.yelp.com/v3/businesses/search'
    key = 'mgXw9dm-MPMu4K7s3wYm6boWR-ZYtWrl0a7vnb1yi1MftJtVg2OHuznV8B4sEZWH_JAUSsrO4B3iyh1EzH5MSt98pG7GB-CpCMJ4jj9aAzld9Usa--zNnFvdkg9KY3Yx'
    headers = {
        'Authorization': 'Bearer %s' % key
    }

    parameters = {'location': location,
                'term': 'Restaurant',
                'radius': distance,  
                'limit': 50,
                }

    response = requests.get(url, headers=headers, params=parameters)
    response

    response.json()


    import pandas as pd
    query = response.json()['businesses']

    results = {'Name': [], 'Rating': [], 'Pricing': []}
    for q in query:
        results['Name'].append(q['name'])
        results['Rating'].append(q['rating']) 
        try: 
            results['Pricing'].append(len(q['price']))
        except:
            results['Pricing'].append(None)
    
    return pd.DataFrame(results)


    

