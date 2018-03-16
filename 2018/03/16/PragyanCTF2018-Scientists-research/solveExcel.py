from xlrd import open_workbook
from PIL import Image 

wb = open_workbook('observations.xlsx')
for sheet in wb.sheets():
	number_of_rows = sheet.nrows
	number_of_columns = sheet.ncols
	flagImage = Image.new('RGB', (number_of_columns,number_of_rows))
	for row in range(1, number_of_rows):
		for col in range(number_of_columns):
			value = str(hex(int(str(sheet.cell(row,col).value)[:-2]))[2:]).zfill(6)
			rgb = tuple(int(value[i:i+2], 16) for i in (0, 2 ,4))
			flagImage.putpixel((row,col),rgb)
flagImage.save("flag.png")
