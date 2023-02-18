import matplotlib.pyplot as plt
import random
import time
import pandas as pd
import csv
from csv import writer
import logging
logging.basicConfig(filename='log_file.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class GuessIt:
    def __init__(self,n,name,id):
        self.n = n
        self.name = name
        self.id = id
        self.result = []
        self.game = []
        self.num = 5
        self.com = {}
        self.user = {}

    def banner(self):
        print('\n')
        print(f"!!!!!!!! Welcome to the the Guess Game - {self.name} !!!!!!")
        time.sleep(2)
        print(f"{self.name}, since you have opted for {self.n} game(s) so we will configure your game accordingly")
        time.sleep(1)
        print(f"Meanwhile Here are the Rules of the Game :: ")
        print('\n')
        time.sleep(2)
        print(f"Each game consist of 5 guess, you have to guess a number between 1 and 5. \
              At the same time computer will also guess a number if your guess and computer guess is same then you win \
              and each correct guess will give you 1 point and there is no negative point for wrong guess")
        print("For example if in Game 1, you guessed 3 out of 5 numbers right than your score will become 60%")
        print("Finally one bar graph will be saved in the local, So as to know how you performed...")
        time.sleep(10)
        print("We are done with Configuring your game environment, Lets Jump into that ")
        print('\n')
        time.sleep(2)


    def logic(self):
        self.banner()
        for i in range(1,self.n+1):
            print(f"Welcome to Game {i}")
            win = 0
            for j in range(0,self.num):
                com_input = random.randint(1,5)
                
                user_input = int(input(f"[**Game {i} ]Enter Any Number (Chance {j+1} of {self.num}): "))

                if com_input == user_input:
                    win = win + 1

                print("Please Wait .....")
                #time.sleep(2)

            temp = win*100 // self.num
            self.result.append(temp)
            print('\n')
            if i != self.n:
                print(f"---------------Loading Game {i+1} -------------------")
            else:
                print("Thanks for Playing the game ....")
                print("You will get the Bar chart from the organiser .....")
            print('\n')
            time.sleep(2)

        for i in range(1,self.n+1):
            self.game.append(f"Game {str(i)}")

        logging.warning(f"Success - {self.id}")
        return self.plot()

    def plot(self):

        plt.bar(self.game, self.result)
        plt.xlabel('No. of Games Played')
        plt.ylabel('Win Percantage')
        plt.title(label=f'Guess Game Results - {self.id}', 
          fontweight=10, 
          pad='2.0')
        #plt.savefig(f"output_{self.id}.jpg")
        plt.ylim(0, 100)
        plt.savefig(f"output_{self.id}.jpg", facecolor='y', bbox_inches="tight",
            pad_inches=0.3, transparent=True)



if __name__ == "__main__":
    
    no_of_games = int(input("Enter no. of Games you want to play : "))
    player_name = input("Enter Player Name : ")
    id = random.randint(100000,110000)
    player_id = player_name + "_" + str(id)
    with open('test.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow([player_id])
        f_object.close()

    with open('test.csv', newline='') as in_file:
        with open('db_data_final.csv', 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if row:
                    writer.writerow(row)

    g = GuessIt(no_of_games, player_name, player_id)
    g.logic()