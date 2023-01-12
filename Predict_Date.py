import time
from datetime import datetime, timedelta
from collections import OrderedDict


def predict(form, buffer):
    ''' Returns Output data by adding the buffer days '''
    
    return form + timedelta(days=buffer)


def sub(check):
    ''' Returns ordinal indicator for respective numbers '''
    
    if int(check) >= 4 or int(check) <= 20 or \
            int(check) >= 24 or int(check) <= 30:
        return "th"
    elif int(check) % 10 == 1:
        return "st"
    elif int(check) % 10 == 2:
        return "nd"
    elif int(check) % 10 == 3:
        return "rd"
    else:
        pass


def num_to_month(temp):
    ''' Returns Month name in character form '''
    
    month_dict = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                  '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}

    for key, value in month_dict.items():
        if temp == key:
            return value


def process():
    '''Main functions which deals with all the logical plus formatting part '''
    
    try:
        print("Enter date with the format given below  [Year, Month, Day] :: \n ")
        
        year, month, day = list(map(int, input("Enter Here [For eg : 1997 01 12] : ").split()))
        date1 = datetime(year, month, day)
        
        inp = str(date1)
        input_form = inp.split(" ")[0].split("-")

        y = int(input("Enter days to get the final date \n"
                      "[For eg. date1 = 2022-01-12 and y = 10 so output = 2022-01-22] \n"
                      "** Please Enter  :::   "))

        p = predict(date1, y)
        res = str(p)
        output_form = res.split(" ")[0].split("-")

        initial = input_form[2] + sub(input_form[2]) + " " + num_to_month(input_form[1]) + " " + \
                  input_form[0]
        print("\nInput Date given by the User ::  {} \n".format(initial))
        
        time.sleep(5)
        
        print("Since your Buffer period is {} days".format(y))
        
        final = output_form[2] + sub(input_form[2]) + " " + num_to_month(output_form[1]) + " " + \
                output_form[0]
        time.sleep(3)
        
        print("So, Your Required Output Date will be  :::   {}".format(final))
        time.sleep(5)
        
        print("Enjoy your day ......")
        time.sleep(5)
        
    except ValueError:
        print("Please Input Correctly ....")


if __name__ == "__main__":
    process()
