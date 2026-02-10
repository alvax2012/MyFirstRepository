from zipfile import ZipFile
from functools import reduce
from datetime import datetime
import json

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


# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()

# # res = [(i.file_size, i.compress_size) for i in info]
# res = max(info, key=lambda x: x.file_size /
#           x.compress_size if not x.is_dir() else 0)

# print((res.filename).split('/')[-1])

# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()


# res = [i.filename.split('/')[-1]
#        for i in info if i.date_time > (2021, 11, 30, 14, 22, 0) and not i.is_dir()]

# # print((res.filename).split('/')[-1])
# # datetime.strptime(file_info, "(%Y, %m, %d, %H, %M, %S)")    datetime(*i.date_time)
# res.sort()
# print(*res, sep='\n')


# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()

# res = [(i.filename.split('/')[-1], datetime(*i.date_time), i.file_size, i.compress_size)
#        for i in info if not i.is_dir()]
# # print(res)
# res.sort(key=lambda x: x[0])
# for i in res:
#     # print(i[0])
#     # print(f'  Дата модификации файла: {i[1]}')
#     # print(f'  Объем исходного файла: {i[2]} байт(а)')
#     # print(f'  Объем сжатого файла: {i[3]} байт(а)')

#     print(f'''{i[0]}
# 	Дата модификации файла: {i[1]}
# 	Объем исходного файла: {i[2]} байт(а)
# 	Объем сжатого файла: {i[3]} байт(а)
#     ''')

def f1(*args):
    print(type(args))
    # if args:
    #     print(type(args))
    # else:
    #     print("None")


f1([1, 2])


# l = []
# with ZipFile('data.zip') as zip_file:
#     info = zip_file.infolist()

#     for i in info:
#         if i.is_dir():
#             continue
#         # print(i.filename)
#         m = i.filename.split('/')[-1]
#         with zip_file.open(i) as file:
#             try:
#                 dt = json.load(file)
#                 if dt['team'] == 'Arsenal':
#                     # print(dt['first_name'], dt['last_name'])
#                     l.append((dt['first_name'], dt['last_name']))
#             except ValueError:
#                 pass
# l.sort(key=lambda x: (x[0], x[1]))
# for i in l:
#     print(i[0], i[1])

with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()


for i in info:
    print(i.filename)
