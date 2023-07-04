import requests, json
#assest
import fractions, decimal


#url = "https://openexchangerates.org/api/convert/{}/{}/{}?app_id={}&prettyprint={}"
url = "https://openexchangerates.org/api/latest.json?app_id={}&base={}&symbols={}&prettyprint=false&show_alternative=false"
app_id = "50203a4f9f2f4ee18403984d42061d61"
headers = {"accept": "application/json"}
pretyprint = True
def revers_number(decimal_value):

    decimal_object = decimal.Decimal(decimal_value)
    fraction_object = fractions.Fraction.from_decimal(decimal_object)
    numerator, denominator = fraction_object.as_integer_ratio()
    decimal_value = denominator / numerator

    return decimal_value

class data:
    def __init__(self, value,from_cu,to_cu):
        self.value = value
        self.from_cu = from_cu
        self.to_cu = to_cu

class USD_caller:
    def __init__(self, format):
        self.format = format
        self.new_url = ""

    def exchange_with_api(self):
        # if self.format["from"] == "USD" and self.format["to"] != "USD":
        #     self.new_url = url.format(app_id, "USD", self.format["to"])
        #     response = requests.get(self.new_url, headers=headers)

        # elif self.format["from"] != "USD" and self.format["from"] == "USD":
        #     self.new_url = url.format(app_id, "USD", self.format["from"])
        #     response = requests.get(self.new_url, headers=headers)
        to = self.format["to"] if self.format["to"] != "USD" else self.format["from"]
        json_rate =self.format["to"] if self.format["to"] != "USD" else self.format["from"]
        #json_rate = self.format["to"] if self.format["to"] !="USD" els
        new_url = url.format(app_id, "USD", to)
        response = requests.get(new_url, headers=headers)

        #print(new_url)
        rate = json.loads(response.text)["rates"][f"{json_rate}"]
        if self.format["from"] == "USD":
            return  (self.format["value"] * rate)
        else: 
            return (self.format["value"] * revers_number(float(rate)))
        #else return baraks
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
        exchange_data = USD_caller(format=changed_format)
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