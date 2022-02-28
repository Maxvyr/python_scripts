import tabula


file_name = input("Filename : ")

tabula.convert_into(file_name, "output.csv", output_format="csv", pages='all')