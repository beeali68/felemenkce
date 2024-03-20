import xlrd
import os
import pymongo
import sqlite3








workbook = xlrd.open_workbook(r"C:\Users\aliar\OneDrive\Belgeler\GitHub\flemenk\ff.xls")

sheet = workbook.sheet_by_name("Yeni Microsoft Excel Çalışma Sa")
#getting the first sheet
print(1)
sheet_1 = workbook.sheet_by_index(0)

for sh in workbook.sheets():
    print(sh.name)

print(2)

for i in range(10000):
    header = sheet.row_values(i, start_colx=0, end_colx=None)
    print(header)


    with sqlite3.connect("mysite/flemenkce_kelime_cumle.db") as vt:
        cursor = vt.cursor()

    cursor.execute(
        "INSERT INTO tablo_1 (kelime_tr, kelime_nl, cumle_tr, cumle_nl, grup, grup_2) VALUES ('{}','{}','{}','{}','{}','{}')".format(header[0],header[1],header[2],header[3], header[4], header[5]))
    vt.commit()