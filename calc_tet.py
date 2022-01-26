import json
import datetime

with open('trong_am_co_duong.json') as json_file:
    data = json.load(json_file)


def normalize(dmy):
    a = datetime.datetime.strptime(dmy, '%d/%m/%Y')
    return a.strftime('%b %d, %Y %H:%M:%S')


def up_to_down(day, month, year):
    cur_year = data[str(year)]
    cur_month = cur_year[str(month)]
    cur_day = cur_month[day-1].split(' ')[1].split('/')
    down_day = cur_day[0]
    down_month = cur_day[1]
    return down_day, down_month


def get_data():
    json_date = {}
    for year in data:
        yearss = {}
        for month in data[str(year)]:
            monthsss = []
            for day in data[str(year)][str(month)]:
                down = ' '.join(day.split(' ')[1].split('/'))
                monthsss.append(down)
            yearss[month] = monthsss
        json_date[year] = yearss
    return json_date


def calc_tet():
    tet_each_year = {}
    cur_year = datetime.datetime.now().year
    for year in data:
        for month in data[str(year)]:
            for day in data[str(year)][str(month)]:
                d = day.split(' ')[0]
                d_m = day.split(' ')[1].split('/')
                if d_m[0] == '1' and d_m[1] == '1':
                    tet_each_year[year] = f'{d}/{month}'
    tet = datetime.datetime.strptime(
        tet_each_year[str(cur_year)] + '/' + str(cur_year), '%d/%m/%Y')
    if datetime.datetime.now() > tet:
        cur_year += 1
    return normalize(tet_each_year[str(cur_year)] + '/' + str(cur_year))
