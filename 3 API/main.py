# Damian Eggert s19766

import imdb
import requests


# Create connection to IMDB API
ia = imdb.IMDb()


def search(term):
    arg = {"q": term}
    return ia.make_request('/find', arg)


# test search movie
def test_simple_search():
    srch = search("diuna")
    x = srch['data']['results'][0]['list'][0]
    print(x)
    assert x['title'] == 'Diuna'
    assert x['tconst'] == 'tt1160419'


# test GET request
url = "https://imdb8.p.rapidapi.com/actors/list-most-popular-celebs"

querystring = {"homeCountry":"US","currentCountry":"US","purchaseCountry":"US"}

headers = {
    'x-rapidapi-key': "dda7be91a8mshaca6900105dfee1p1b762djsn986c366962e5",  # personal account key
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)

# check response status
assert response.status_code == 200

# check response with error status
url2 = "https://imdb8.p.rapidapi.com/actors/wrongwrong"
response2 = requests.request("GET", url2)
# print(response2.status_code)
assert response2.status_code == 401
