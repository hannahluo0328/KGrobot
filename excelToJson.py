import xlrd
def openWorkbook():
    # 读取excel表的数据
    workbook = xlrd.open_workbook(r'data_new\treeMap.xlsx')
    # 选取需要读取数据的那一页
    sheet = workbook.sheet_by_index(0)
    # 获得行数和列数
    rows = sheet.nrows
    cols = sheet.ncols
    # 创建一个数组用来存储excel中的数据
    p = []
    for i in range(2, rows):
        d = {}
        for j in range(0, cols):
            q = '%s' % sheet.cell(0, j).value
            d[q] = sheet.cell(i, j).value
        ap = []
        for k, v in d.items():
            if isinstance(v, float):  # excel中的值默认是float,需要进行判断处理，通过'"%s":%d'，'"%s":"%s"'格式化数组
                ap.append('"%s":%d' % (k, v))
            else:
                ap.append('"%s":"%s"' % (k, v))
        s = '{%s}' % (','.join(ap))  # 继续格式化
        p.append(s)
    t = '[%s]' % (','.join(p))  # 格式化
    print(t)

    with open('treeMapOut.json', "w") as f:
        f.write(t)


openWorkbook()
