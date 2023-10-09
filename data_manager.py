from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/49b70b056cff7fa65a4b7400a8725ad1/cheapFlight/sheet1"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers={"Authorization": "Basic aDpo"})
        data = response.json()
        # print(data
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
