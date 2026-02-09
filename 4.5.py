from zipfile import ZipFile
from functools import reduce

# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()

# res = [(i.filename, i.file_size) for i in info if i.is_dir()]
# print(res)


# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()

# # res = [(i.file_size, i.compress_size) for i in info]
# res = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]),
#              [(i.file_size, i.compress_size) for i in info])

# print(f'Объем исходных файлов: {res[0]} байт(а)', f'Объем сжатых файлов: {res[1]} байт(а)', sep='\n')


with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

# res = [(i.file_size, i.compress_size) for i in info]
res = max(info, key=lambda x: x.compress_size /
          x.file_size if not x.is_dir() else 0)

print((res.filename).split('/')[-1])
