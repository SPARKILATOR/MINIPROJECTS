'''
Script which will predict what team will be against whom in the Round of 16
of the Champions League
Other data like the group details and the Pot details are present in the Json
which is present in the main folder.
'''
import logging
import json
import random
import time
logging.basicConfig(filename=r'log.txt', filemode='w', format='%(asctime)s.%(msecs)03d %(name)s - %(levelname)s - %(message)s')

logging.warning('Champions League Round of 16 Draw Starting .....')

if __name__ == "__main__":
    draw_list = []
    # extracting relevant details from the Json.
    with open(r"details.json") as json_file:
        data = json.load(json_file)
    with open(r"group.json") as json_file_group:
        data_group = json.load(json_file_group)
    # Logging the POT1 and POT2 teams of the league.
    logging.warning("CHAMPIONS LEAGUE POT 1 : %r" %(data['Pot1']))
    logging.warning("CHAMPIONS LEAGUE POT 2 : %r" % (data['Pot2']))
    # Main logic to predict the teams
    for club1, country1 in data['Pot1'].items():
        while True:
            count = 0
            a = random.choice(list(data['Pot2'].items()))
            if (club1 in draw_list) or (a[0] in draw_list):
                continue
            if str(country1) != str(a[1]):
                for i in range(1, 9):
                    if (club1 in data_group['GROUP_' + str(i)]) and (a[0] in data_group['GROUP_' + str(i)]):
                        count = 1
                        break
                if count == 0:
                    draw_list.append(club1)
                    draw_list.append(a[0])
                    break
    logging.warning("PLEASE WAIT .....")
    time.sleep(2)
    logging.warning("\n")
    logging.warning("----> CHAMPIONS LEAGUE DRAW LOADING .....")
    time.sleep(2)
    for i in range(0,len(draw_list),2):
        logging.warning("DRAW %r --> %r [%r] VS %r [%r]" %((i+2)//2,draw_list[i],data['Pot1'][draw_list[i]],draw_list[i+1],data['Pot2'][draw_list[i+1]]))
        time.sleep(2)
