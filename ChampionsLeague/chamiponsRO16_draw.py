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

logging.basicConfig(filename=r'log.txt', filemode='w', format='%(asctime)s.%(msecs)03d %(levelname)s - %(message)s')

logging.warning('Champions League Round of 16 Draw Starting .....')


def draw_time(t1, t2):
    # Performance check for the logic
    return t2 - t1


class ChampionsLeague:
    def __init__(self, data, data_group):
        self.data = data
        self.data_group = data_group
        self.draw_list = []
        self.t = 0

    def log(self):
        # Logging the POT1 and POT2 teams also the group details of the league.
        logging.warning("CHAMPIONS LEAGUE POT 1 : %r" % self.data['Pot1'])
        logging.warning("CHAMPIONS LEAGUE POT 2 : %r" % self.data['Pot2'])
        logging.warning("GROUP DETAILS  ::: %r" % self.data_group)

    def draw(self):
        t1 = time.time()
        # Main logic to predict the teams
        for club1, country1 in self.data['Pot1'].items():
            while True:
                count = 0
                # Pick any team from the Pot2
                a = random.choice(list(self.data['Pot2'].items()))
                # To handle duplication
                if (club1 in self.draw_list) or (a[0] in self.draw_list):
                    continue
                # Applied Conditions like 2 Teams should not be from same national league
                # and not from the same group
                if str(country1) != str(a[1]):
                    for i in range(1, len(self.data_group) + 1):
                        if (club1 in self.data_group['GROUP_' + str(i)]) and (
                                a[0] in self.data_group['GROUP_' + str(i)]):
                            count = 1
                            break
                    if count == 0:
                        self.draw_list.append(club1)
                        self.draw_list.append(a[0])
                        break
        logging.warning("PLEASE WAIT .....")
        time.sleep(2)
        logging.warning("\n")
        logging.warning("----> CHAMPIONS LEAGUE DRAW LOADING .....")
        time.sleep(2)
        for i in range(0, len(self.draw_list), 2):
            logging.warning("DRAW %r --> %r [%r] VS %r [%r]" % (
                (i + 2) // 2, self.draw_list[i].upper(), self.data['Pot1'][self.draw_list[i]],
                self.draw_list[i + 1].upper(),
                self.data['Pot2'][self.draw_list[i + 1]]))
            time.sleep(2)
        logging.warning('\n')
        t2 = time.time()
        self.t = round(draw_time(t1, t2), 2)
        logging.warning("This prediction took  %r seconds " % self.t)
        logging.warning("----> THANK YOU FOR STAYING WITH US, AND WILL MEET SOON TILL THEN ENJOY RESPONSIBLY .....")


if __name__ == "__main__":
    # extracting relevant details from the Json.
    with open(r"details.json") as json_file:
        data_pot = json.load(json_file)
    with open(r"group.json") as json_file_group:
        data_group_detail = json.load(json_file_group)
    championsRO16_draw = ChampionsLeague(data_pot, data_group_detail)
    # if u want details of the group and pot, then do this championsRO16_draw.log()
    championsRO16_draw.draw()
