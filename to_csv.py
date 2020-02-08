import xlwt


def data_to_excel(json_data):
	# каждый словарь распихиваем список
	data_list = []
	for i in range(len(json_data)):
		list_ = []
		for k, v in json_data[i].items():
			list_.append(v)
		data_list.append(list_)
	return data_list


def to_excel(excel_data):
	# запись в csv
	wb = xlwt.Workbook() 
	ws = wb.add_sheet('appstore_test') 
	for i in range(len(excel_data)): 
		for j in range(len(excel_data[i])): 
			ws.write(i, j, str(excel_data[i][j]))
	wb.save('appstore.csv')