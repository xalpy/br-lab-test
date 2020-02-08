import requests
import json
from to_csv import to_excel, data_to_excel
import argparse


def get_json_data(url: str, headers: dict, collected_data = []) -> list:
	# запрос по апи в appstore и получение джсона
	json_req = requests.get(url, headers = headers).json()
	# каждый комментарий запихиваем в список для дальнейшей записи в csv
	for i in range(len(json_req)):
		json_data = json_req['data'][i]['attributes']
		collected_data.append(json_data)
	return collected_data


def parse(offset_count: int) -> None:
	# основная функция на вход получает аргумент переданный в командной строке как аргумент
	offset = range(0, offset_count, 2)
	bearer = 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldlYlBsYXlLaWQifQ.eyJpc3MiOiJBTVBXZWJQbGF5IiwiaWF0IjoxNTc5NjM3MzI0LCJleHAiOjE1OTUxODkzMjR9.SCgFvMtDJmpfGBYGjJ9ss9aloYssX7HYq0eI-xyQssNruaVLI_wXLWPDUtigBXDQrwVCPariPfcvOLvEn067lg'
	user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36'
	headers = {'authorization': bearer, 'user-agent': user_agent}
	for off in offset:
		url = f'https://amp-api.apps.apple.com/v1/catalog/ru/apps/1065803457/reviews?l=ru&offset={off}&platform=web&additionalPlatforms=appletv%2Cipad%2Ciphone%2Cmac'
		json_data = get_json_data(url, headers)

	excel_data = data_to_excel(json_data)
	to_excel(excel_data)



if __name__ == "__main__":

	parser=argparse.ArgumentParser(prefix_chars='-#+')
	parser.add_argument(
	    '--parse',
	    type=int,
	    default=2,
	    help='provide an integer (default: 2)'
	)

	my_namespace = parser.parse_args()
	offset_int = my_namespace.parse
	parse(offset_int)