#!/usr/bin/python
# -*- coding: utf-8 -*-
"файл для работы с csv"
import xlwt


def data_to_excel(json_data):
    "каждый словарь распихиваем список"
    data_list = []
    for i in range(len(json_data)):
        list_ = []
        for _, value in json_data[i].items():
            list_.append(value)
        data_list.append(list_)
    return data_list


def to_excel(excel_data):
    "запись в csv"
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('appstore_test')
    for i in range(len(excel_data)):
        for j in range(len(excel_data[i])):
            worksheet.write(i, j, str(excel_data[i][j]))
    workbook.save('appstore.csv')
