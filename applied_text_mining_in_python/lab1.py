# this version does not use pandas
import regex as re
import calendar
import datetime
import operator

#convert month name into numbers
def convert_month(month_name):
    if len(month_name[0]) > 3:
        datetime_object = datetime.datetime.strptime(month_name[0], "%B")
    else:
        datetime_object = datetime.datetime.strptime(month_name[0], "%b")
    return datetime_object.month
        
with open('dates.txt') as f:
    count = 0
    line_num = 1
    # create month abbreviations list
    month_abbr_list = []
    for i in range(1,13):
        month_abbr_list.append(calendar.month_abbr[i])
    
    #can be simplified    
    pattern = '\d{1,2}\/\d{1,2}\/\d{2,4}|\d{1,2}-\d{1,2}-\d{2,4}|\d{1,2}\s[a-zA-Z]{3}\s\d{4}|' + '[\.,]?\s\d{4}|'.join(calendar.month_name[1:]) + '[\.,]?\s\d{4}|' +'[\.,]?\s\d{1,2}[\.,]?\s\d{4}|'.join(calendar.month_name[1:]) + '[\.,]?\s\d{1,2}[\.,]?\s\d{4}|' + '[\.,]?\s\d{4}|'.join(month_abbr_list) +'[\.,]?\s\d{4}|' + '[\.,]?\s\d{1,2}[\.,]?\s\d{4}|'.join(month_abbr_list) +'[\.,]?\s\d{1,2}[\.,]?\s\d{4}' + '|\d{1,2}\s[a-zA-Z]+\s\d{4}|\d{1,2}\/\d{4}|19\d\d|20\d\d'
    
    result_date = []
    for line in f:
        result = re.findall(pattern, line)
        result_date.append(result[0])

    date_table = []
    original_index = 0
    # create a table to store the dates
    for i in range(len(result_date)):
        #standardize dates format as numbers only and seperated by / only
        new_date = re.sub(r'[ -]', '/', result_date[i])
        new_date = re.sub(r'[,.]', '', new_date)
        month_name = re.findall(r'[a-zA-Z]+',new_date)
        if month_name != []:
            month_num = str(convert_month(month_name))
            new_date = re.sub(month_name[0], month_num, new_date)

        #standardize dates by adding lost month or date so that it conforms to the format: xx/xx/xxxx
        if new_date.count('/') == 0:
            new_date = '01/01/' + new_date
        elif new_date.count('/') == 1:
            new_date = re.sub('/', '/01/', new_date)
        
        #standardize to mm/dd/yyyy
        new_date_list = new_date.split('/')
        if int(new_date_list[0]) > 12:
            d = new_date_list[0]
            new_date_list[0] = new_date_list[1]
            new_date_list[1] = d
        if len(new_date_list[2]) == 2:
            new_date_list[2] = '19' + new_date_list[2]
        if len(new_date_list[0]) == 1:
            new_date_list[0] = '0' + new_date_list[0]
        if len(new_date_list[1]) == 1:
            new_date_list[1] = '0' + new_date_list[1]
        
        #convert to integer for comparison
        new_date_list = [int(new_date_list[2] + new_date_list[0] + new_date_list[1])]
        
        #adding original index for comparison later
        new_date_list.insert(0, original_index)
        original_index += 1
        date_table.append(new_date_list)
    
    sorted_date = sorted(date_table, key=operator.itemgetter(1))
    sorted_index = []
    for item in sorted_date:
        sorted_index.append(item[0])
    print(sorted_index)