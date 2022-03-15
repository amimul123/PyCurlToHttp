# PyCurlToHttp
Convert curl request to HTTP (API) request in Python

# curl request & response (Token)
Request:<br/>
curl -u "username:password" "https://example.com/api/token" <br/>
Response:
```json
{
    "project": "project id",
    "token": "your token",
    "version": "version number"
}
```

# curl request & response (Rating)
Request:<br/>
curl -u "username:password" "https://example.com/api/myrating?end_date={END_DATE}&start_date={START_DATE}"<br/>
Response:
```json
response:
{
    "data": [
        {
            "created_at": "2022-02-01T23:59:59.999 00:00",
            "count": 200,
            "value": 111,
            "rating": 8
        },
        {
            "created_at": "2022-02-02T23:59:59.999 00:00",
            "count": 100,
            "value": 11,
            "rating": 10
        },
    ]
}

```
