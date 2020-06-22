import xlrd

loc = '../vgsales.xlsx'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

def ngames_by_publisher(publisher):
    publisher = publisher.lower()
    ret = []

    for i in range(sheet.nrows):
        p = sheet.cell_value(i, 5).lower()
        if p == publisher:
            ret.append(sheet.cell_value(i, 1))
        i += 1

    return ret


def ngames_by_publisher_1():
    ret = dict()

    for i in range(1, sheet.nrows):
        p = sheet.cell_value(i, 4)
        if p in ret.keys():
            ret[p] = int(ret.get(p)) + 1
        else:
            ret[p] = 1

    keys = list(ret.keys())
    for i in range(len(keys)):
        if ret[keys[i]] < 0:
            ret.pop(keys[i])
            i -= 1

    return ret


def ngames_by_year(platform):
    ret = list()
    years = published_years()

    for i in range(0, len(years)):
        ret.append(0)
        for k in range(1, sheet.nrows):
            p = sheet.cell_value(i, 2)
            if p == platform:
                y = sheet.cell_value(k, 3)
                if y == years[i]:
                    ret[i] += 1

    return ret


def published_years():
    ret = list()

    for i in range(1, sheet.nrows):
        y = sheet.cell_value(i, 3)
        if y not in ret and y != 'N/A':
            ret.append(int(y))

    ret.sort()

    return ret

def ngames_by_platform_and_year():
    ret = dict()

    ret['Year'] = published_years()

    for p in platforms():
        ret[p] = ngames_by_year(p)

    return ret

def platforms():
    ret = list()

    for i in range(1, sheet.nrows):
        y = sheet.cell_value(i, 2)
        if y not in ret and y != 'N/A':
            ret.append(y)

    return ret

