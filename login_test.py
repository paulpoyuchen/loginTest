import requests

def loginTest(username, password):
    url = "https://api.shipt.com/auth/v2/oauth/token"

    querystring = {"bucket_number":"0"}

    payload = "username="+username+"&password="+password+"&grant_type=password&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'X-User-Type': "Customer",
        'cache-control': "no-cache",
        'Postman-Token': "a9202307-96ce-4510-8c7d-7b834e1e6847"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)
    return response.text
