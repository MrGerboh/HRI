import sys
import time
import os
import random

try:
    sys.path.insert(0, os.getenv('MODIM_HOME')+'/src/GUI')
except Exception as e:
    print "Please set MODIM_HOME environment variable to MODIM folder."
    sys.exit(1)

# Set MODIM_IP to connnect to remote MODIM server

import ws_client
from ws_client import *


def i1():

    im.init()

    im.ask('welcome', timeout = 999)  # wait for button

    q = 'home'
    a = im.ask(q, timeout = 999)

    while (a != 'exit'):
        if a == 'fact':
            #Show fun fact
            while a != 'back':
                #q = 'fact_' + str(random.choice(['1', '2', '3']))
                q = 'fact_2'
                a = im.ask(q, timeout = 999)
            a = im.ask('home', timeout = 999)
        elif a == 'forecast':
            #Show forecast
            while a != 'back':
                #q = str(random.choice(['sunny', 'cloudy', 'rainy']))
                q = 'sunny'
                a = im.ask(q, timeout = 999)
            a = im.ask('home', timeout = 999)
        elif a == 'test':
            retry = True
            #Choose category
            while retry == True:
                score = 0
                a = im.ask('test', timeout = 999)
                if a == 'back':
                    a = im.ask('home', timeout = 999)
                #Play test
                elif a == 'pop':
                    a = im.ask('pop_1', timeout = 20)
                    if a == 'correct':
                        score += 1
                    a = im.ask('pop_2', timeout = 20)
                    if a == 'correct':
                        score += 1
                    a = im.ask('pop_3', timeout = 20)
                    if a == 'correct':
                        score += 1
                    if score >= 2:
                        a = im.execute('correct')
                        retry = False
                    else:
                        a = im.ask('wrong', timeout = 999)
                        if a == 'try':
                            retry = True
                        else:
                            retry = False
                elif a == 'science':
                    a = im.ask('science_1', timeout = 20)
                    if a == 'correct':
                        score += 1
                    a = im.ask('science_2', timeout = 20)
                    if a == 'correct':
                        score += 1
                    a = im.ask('science_3', timeout = 20)
                    if a == 'correct':
                        score += 1
                    if score >= 2:
                        a = im.execute('correct')
                        retry = False
                    else:
                        a = im.ask('wrong', timeout = 999)
                        if a == 'try':
                            retry = True
                        else:
                            retry = False
                elif a == 'art':
                    a = im.ask('art_1', timeout = 20)
                    if a == 'correct':
                        score += 1
                    a = im.ask('art_2', timeout = 20)
                    if a == 'correct':
                        score += 1
                    a = im.ask('art_3', timeout = 20)
                    if a == 'correct':
                        score += 1
                    if score >= 2:
                        a = im.execute('correct')
                        retry = False
                    else:
                        a = im.ask('wrong', timeout = 999)
                        if a == 'try':
                            retry = True
                        else:
                            retry = False
            a = im.ask('home', timeout = 999)

    #im.execute('welcome')
    im.execute('goodbye')

    im.init()


if __name__ == "__main__":

    mws = ModimWSClient()

    # local execution
    mws.setDemoPathAuto(__file__)
    # remote execution
    # mws.setDemoPath('<ABSOLUTE_DEMO_PATH_ON_REMOTE_SERVER>')

    mws.run_interaction(i1)


