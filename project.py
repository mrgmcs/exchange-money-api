import requests, json
#assest
#url = "https://openexchangerates.org/api/convert/{}/{}/{}?app_id={}&prettyprint={}"
url = "https://openexchangerates.org/api/latest.json?app_id={}&base={}&symbols={}&prettyprint=false&show_alternative=false"
app_id = "50203a4f9f2f4ee18403984d42061d61"
headers = {"accept": "application/json"}

pretyprint = True
class data:
    def __init__(self, value,from_cu,to_cu):
        self.value = value
        self.from_cu = from_cu
        self.to_cu = to_cu

class api_call:
    def __init__(self, format):
        self.format = format
    def exchange_with_api(self):
        new_url = url.format(app_id, self.format["from"], self.format["to"])
        response = requests.get(new_url, headers=headers)
        rate = json.loads(response.text)["rates"][f"{self.format['to']}"]
        return  (self.format["value"] * rate)
class Adapter:
    def __init__(self, data):
        pass
        self.data=data
    def exchange(self):
        #call new class
        changed_format = {
            "value": self.data.value,
            "from": self.data.from_cu,
            "to": self.data.to_cu
        }
        #call new class to exchange
        exchange_data = api_call(format=changed_format)
        return exchange_data.exchange_with_api()

#get data from user
def get_user_data():
    value = int(input("Enter the value: "))
    from_cu = input("From currency(must be 3 letters) : ")
    to_cu = input("To currency(must be 3 letters) : ")
    user_data_ret = {
        "value": value,
        "from": from_cu.upper(),
        "to": to_cu.upper()
    }
    return user_data_ret
user_data = get_user_data()
#we have dict for data

human_readble_data = data(user_data["value"],user_data["from"], user_data["to"])
adapter_exchange = Adapter(human_readble_data)
eq = adapter_exchange.exchange()
print(f"{user_data['value']} {user_data['from']} is equivalent to {eq} {user_data['to']}")