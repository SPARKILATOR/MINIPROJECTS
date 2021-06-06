'''On a form, users are asked to enter dates that come in as strings. Before 
storing them to the disk, they need to be converted to a standard date 
format. Write a function to convert the dates as described. 

Given a date string in the format Day Month Year, where: 

' Day a string in the farm "1 st", "2nd", "3rd '21 st", "22nd", "23rd", "31 st" and 
all others are the number + "th", e.g. "4th" or "12th". 
. Month is the first three letters of the English language months, like 'Jan" for 
January through "Dec" for December. 
. years 4 digits ranging from 1900 to 2100. 

Convert the date string "Day Month year" to the date string " yyyr-MM-DD" 
in the format "4 digit year - 2 digit month - digit day".  

Example 
. lst Mar 1974--. 197a-03-01 
. 22ndjan 2013-.2013-01-22 
. 7th Apr 1904-.1904-04-07 '''

#LETS GET STARTED..

import re
import calendar
l=[]
res = ''
res_1 = []
res_2 = ''
res_3 = ''
result = []
size = int(input())
input_list = []
for i in range(size):
    temp = input()
    input_list.append(temp)
for i in input_list:
    l=i.split()
    res_1 = re.findall(r"\d+", l[0])          #result date
    res = res_1[0]
    if len(res) == 1:
        res = '0' + res
    l[1] = l[1].lower()
    l[1] = l[1].capitalize()
    if (l[1] == 'Jan' or l[1] == 'Feb' or l[1] == 'Mar' or l[1] == 'Apr' or l[1] == 'May'\
           or l[1] == 'Jun' or l[1] == 'Jul' or l[1] == 'Aug' or l[1] == 'Sep'\
           or l[1] == 'Oct' or l[1] == 'Nov' or l[1] == 'Dec'):
        r = {month: index for index, month in enumerate(calendar.month_abbr) if month}
        for key,value in r.items():
            if key == l[1]:
                res_2 = str(r[key])
        if len(res_2) == 1:
            res_2 = '0' + res_2
    else:
        print("WRONG INPUT")
    res_3 = l[2]
    result.append(res_3+'-'+res_2+'-'+res)
    l.clear()
print(result)
    
