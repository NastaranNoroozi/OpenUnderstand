from pprint import pprint

try:
    import understand as und
except ImportError:
    print("Can not import understand")

db = und.open("D:\Dev\JavaSample\JavaSample1.udb")

pprint(db.relative_file_name("D:\Dev\JavaSample\src\Admin.java"))
