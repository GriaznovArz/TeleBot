import requests
import json

base = input("Enter the base currency: ")
sym = input("Enter the sym currency: ")

while True:
	try:
		amount = float(input("Enter the amount: "))
	except:
		print("The amount must be a numeric value!")
		continue

	if not amount > 0:
		print("The amount must be greater than 0")
		continue
	else:
		break

headers= {
  "apikey": "9NG6nzdJts1eyZA84IUGR8VuugvBy4Md"
}
response = requests.get(f"https://api.apilayer.com/fixer/convert?to={base}&from=\
{sym}&amount={str(amount)}",headers = headers)
# status_code = response.status_code
#
# if status_code != 200:
# 	print("Uh oh, there was a problem. Please try again later")
# 	quit()
result = json.loads(response.text)
print (round(result["result"],2))