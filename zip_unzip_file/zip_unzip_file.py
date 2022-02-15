import shutil

# file_zip = zipfile.ZipFile("zip_CA.zip", "w", zipfile.ZIP_DEFLATED) #last param help to reduce size file
# file_zip.write("10_oct.xlsx")
# file_zip.write("11_nov.xlsx")
# file_zip.write("12_dec.xlsx")

# zip good version
shutil.make_archive("file_result", "zip", "file_group")


#unzip
# shutil.unpxack_archive("file_result_zip.zip", "extract_zip_file d")