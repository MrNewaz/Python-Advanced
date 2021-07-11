from pathlib import Path
from zipfile import ZipFile

# with ZipFile("files.zip", "w") as sip:
#     for path in Path("ecommerce").rglob("*.*"):
#         sip.write(path)

with ZipFile("files.zip") as sip:
    print(sip.namelist())
    # info = sip.getinfo("ecommerece/__init__.py")
    # print(info.file_size)
    # print(info.compress_size)
    sip.extractall("extract")
