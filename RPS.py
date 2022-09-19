# Author: Charlie Dewitt
# Date: 9/19/2022
#
# Description: Rock, Paper, Scissors program that keeps track of the win,loss,tie records of each user and the computer

import os
import random
import PySimpleGUI as pg

# File access locations, change if using a computer other than the author's
file_list = os.listdir('C:\\Users\\charl\\PycharmProjects\\PythonGUI\\Users')
path = 'C:\\Users\\charl\\PycharmProjects\\PythonGUI\\Users\\'
username = ''


class Computer:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0


class Profile:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.wins = 0
        self.losses = 0
        self.ties = 0


user = Profile()
cpu = Computer()


# Record access functions
def update_records():
    f = open(path + user.username + '.txt', "w+")
    f.write(user.username + '\n')
    f.write(user.password + '\n')
    f.write(str(user.wins) + '\n')
    f.write(str(user.losses) + '\n')
    f.write(str(user.ties) + '\n')
    f.close()

    g = open('C:\\Users\\charl\\PycharmProjects\\PythonGUI\\Computer', "w+")
    g.write(str(cpu.wins) + '\n')
    g.write(str(cpu.losses) + '\n')
    g.write(str(cpu.ties) + '\n')
    g.close()


def get_records():
    f = open(path + user.username + '.txt')
    user.username = f.readline().strip()
    user.password = f.readline().strip()
    user.wins = int(f.readline().strip())
    user.losses = int(f.readline().strip())
    user.ties = int(f.readline().strip())
    f.close()

    c = open('C:\\Users\\charl\\PycharmProjects\\PythonGUI\\Computer')
    cpu.wins = int(c.readline().strip())
    cpu.losses = int(c.readline().strip())
    cpu.ties = int(c.readline().strip())
    c.close()


# Game Engine
def login_success():
    win_flag = 0

    pg.theme('Topanga')
    output1 = pg.Text()
    output2 = pg.Text()
    win_lose1 = pg.Text()
    win_lose2 = pg.Text()
    user_record = pg.Text(str(user.wins) + '-' + str(user.losses) + '-' + str(user.ties), size=(10, 1),
                          justification='c')
    cpu_record = pg.Text(str(cpu.wins) + '-' + str(cpu.losses) + '-' + str(cpu.ties), size=(10, 1), justification='c')

    col1 = [[pg.Text('Record', size=(10, 1), justification='c')],
            [user_record],
            [output1],
            [win_lose1]]
    col2 = [[pg.Text('Record', size=(10, 1), justification='c')],
            [cpu_record],
            [output2],
            [win_lose2]]
    layout = [
        [pg.Frame('Player', col1, size=(150, 150), element_justification='c'),
         pg.Frame('Computer', col2, size=(150, 150), element_justification='c')],
        [pg.Button('Rock'), pg.Button('Paper'), pg.Button('Scissors')]
    ]

    window = pg.Window('Rock Paper Scissors', layout)

    while True:
        event, values = window.read()
        cpu_num = random.randrange(2)
        if event == pg.WIN_CLOSED:
            break
        if cpu_num == 0:
            cpu_move = 'Rock'
        elif cpu_num == 1:
            cpu_move = 'Paper'
        elif cpu_num == 2:
            cpu_move = 'Scissors'
        if event == 'Rock':
            output1.update('Rock')
            output2.update(cpu_move)
            if cpu_move == 'Rock':
                win_flag = 2
                win_lose1.update('Tie')
                win_lose2.update('Tie')
            elif cpu_move == 'Paper':
                win_flag = 0
                win_lose1.update('Lose')
                win_lose2.update('Win')
            elif cpu_move == 'Scissors':
                win_flag = 1
                win_lose1.update('Win')
                win_lose2.update('Lose')
        elif event == 'Paper':
            output1.update('Paper')
            output2.update(cpu_move)
            if cpu_move == 'Rock':
                win_flag = 1
                win_lose1.update('Win')
                win_lose2.update('Lose')
            elif cpu_move == 'Paper':
                win_flag = 2
                win_lose1.update('Tie')
                win_lose2.update('Tie')
            elif cpu_move == 'Scissors':
                win_flag = 0
                win_lose1.update('Lose')
                win_lose2.update('Win')
        elif event == 'Scissors':
            output1.update('Scissors')
            output2.update(cpu_move)
            if cpu_move == 'Rock':
                win_flag = 0
                win_lose1.update('Lose')
                win_lose2.update('Win')
            elif cpu_move == 'Paper':
                win_flag = 1
                win_lose1.update('Win')
                win_lose2.update('Lose')
            elif cpu_move == 'Scissors':
                win_flag = 2
                win_lose1.update('Tie')
                win_lose2.update('Tie')

        if win_flag == 1:
            user.wins += 1
            cpu.losses += 1

        elif win_flag == 0:
            user.losses += 1
            cpu.wins += 1

        elif win_flag == 2:
            user.ties += 1
            cpu.ties += 1

        update_records()

        cpu_record.update(str(cpu.wins) + '-' + str(cpu.losses) + '-' + str(cpu.ties))
        user_record.update(str(user.wins) + '-' + str(user.losses) + '-' + str(user.ties))

    window.close()


# Helper functions for login()
def login_fail_password():
    pg.theme("Topanga")
    layout = [
        [pg.Text("Incorrect password, please try again", justification='c')],
        [pg.Button("Log-In"), pg.Button("Cancel")]
    ]

    window = pg.Window("Log In Failed", layout)

    while True:
        event, values = window.read()
        if event == "Log-In" or event == pg.WIN_CLOSED:
            login()
        elif event == "Cancel":
            break

    window.close()


def login_fail_username():
    pg.theme("Topanga")
    layout = [
        [pg.Text("Username not found, please try again", justification='c')],
        [pg.Button("Log-In"), pg.Button("Cancel")]
    ]

    window = pg.Window("Log In Failed", layout)

    while True:
        event, values = window.read()
        if event == "Log-In" or event == pg.WIN_CLOSED:
            login()
        elif event == "Cancel":
            break
    window.close()


def check_password(passw):  # helper function for login() to check the matching of passwords
    if user.password == passw:
        return True
    else:
        return False  #


# Main windows
def login():  # login function, accessed from Log-in button, used for current accounts
    pg.theme('DarkGreen1')
    layout = [[pg.Text("Log In", size=(15, 1), font=40, justification='l')],
              [pg.Text("Enter Username:", size=(15, 1), font=16), pg.InputText(key='-usern-', font=16)],
              [pg.Text("Enter Password:", size=(15, 1), font=16),
               pg.InputText(key='-passw-', font=16, password_char='*')],
              [pg.Button("Submit"), pg.Button("Cancel")]]

    window = pg.Window("Log In", layout)

    while True:
        event, values = window.read()
        if event == 'Cancel' or event == pg.WIN_CLOSED:
            break
        else:
            if event == 'Submit':
                user.username = values['-usern-']
                if user.username + '.txt' in file_list:
                    get_records()
                    if check_password(values['-passw-']) is True:
                        login_success()
                    else:
                        window.close()
                        login_fail_password()
                        break
                else:
                    window.close()
                    login_fail_username()
            break
    window.close()  ##


def create_profile():  # create profile window, sign up
    global username

    pg.theme('DarkGreen1')
    layout = [[pg.Text("Sign Up", size=(15, 1), font=40, justification='l')],
              [pg.Text("Create Username", size=(15, 1), font=16), pg.InputText(key='-usern-', font=16)],
              [pg.Text("Create Password", size=(15, 1), font=16),
               pg.InputText(key='-passw-', font=16, password_char='*')],
              [pg.Button("Submit"), pg.Button("Cancel"), pg.Button("Log-In")]]

    window = pg.Window("Sign Up", layout)

    while True:
        event, values = window.read()
        if event == 'Cancel' or event == pg.WIN_CLOSED:
            break
        elif event == "Log-In":
            window.close()
            login()
            break
        else:
            if event == 'Submit':
                username = values['-usern-']
                f = open(path + values['-usern-'] + '.txt', "x")
                f.write(values['-usern-'] + '\n')
                f.write(values['-passw-'] + '\n')
                f.write(str(0) + '\n')
                f.write(str(0) + '\n')
                f.write(str(0) + '\n')
                f.close()
                break
    window.close()


create_profile()  # start of program
