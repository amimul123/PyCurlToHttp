#!/usr/bin/env python
# coding: utf-8

import requests
import json
from datetime import datetime, timedelta

username = 'your username'
password = 'your password'
credential = (username,password)

# token information
tokenUrl= "https://example.com/api/token"
tokeRes = requests.get(tokenUrl, auth= credential)

jsonToken = json.loads(tokeRes.text)
print(jsonToken)

# Ratings and Stars
params = (
    ('end_date', '2022-02-02'),
    ('start_date', '2022-02-01'),
)
rating_url = 'https://example.com/api/myrating'
ratingRes = requests.get(rating_url, params=params, auth=credential)
jsonRating =  json.loads(ratingRes.text)
#jsonRating


ratings = jsonRating.get('data', [])
for rating in ratings:
    created_at = datetime.fromisoformat(rating.get('created_at')).strftime('%Y-%m-%d %H:%M:%S')
    count = rating.get('count',0)
    value = rating.get('value',0.00)
    rating = rating.get('rating',0)
    print(created_at, count, value, rating)




