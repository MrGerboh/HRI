import qi
import argparse
import sys
import time
import os

pdir = os.getenv('PEPPER_TOOLS_HOME')
sys.path.append(pdir+ '/cmd_server')

import pepper_cmd
from pepper_cmd import *

def think():
    jointNames = ["RShoulderPitch", "RElbowRoll", "RElbowYaw", "RWristYaw", "RHand", "HeadPitch"]
    angles = [-0.15, 1.0, 1.0, 0.8, 1.0, 0.5]
    times  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    for i in range(2):
        jointNames = ["RHand"]
        angles = [-1.0]
        times  = [0.8]
        isAbsolute = True
        motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

        angles = [1.0]
        motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    posture = "Stand"
    speed = 0.7
    rp_service.goToPosture(posture,speed)
    return

def cheer():
    jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "LShoulderPitch", "LShoulderRoll", "LElbowRoll", "HeadPitch"]
    angles = [-0.1, -0.5, 0.9, -0.1, 0.5, -0.9, -0.1]
    times  = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    for i in range(2):
        jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "LShoulderPitch", "LShoulderRoll", "LElbowRoll"]
        angles = [-1.0, 0.0, -0.1, -1.0,  0.0, 0.1]
        times  = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        isAbsolute = True
        motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

        jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "LShoulderPitch", "LShoulderRoll", "LElbowRoll"]
        angles = [-0.1, -0.5, 0.9, -0.1, 0.5, -0.9]
        times  = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
        isAbsolute = True
        motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    posture = "Stand"
    speed = 0.7
    rp_service.goToPosture(posture,speed)
    return

def hello():
    jointNames = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RWristYaw", "RHand", "HeadPitch"]
    angles = [-0.1, -0.5, 0.9, -0.8, 1.0, -0.1]
    times  = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
    isAbsolute = True
    motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    for i in range(2):
        jointNames = ["RElbowYaw", "HeadPitch"]
        angles = [2.0,  -0.1]
        times  = [0.8, 0.8]
        isAbsolute = True
        motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

        jointNames = ["RElbowYaw", "HeadPitch"]
        angles = [1.0, -0.1]
        times  = [0.8, 0.8]
        isAbsolute = True
        motion_service.angleInterpolation(jointNames, angles, times, isAbsolute)

    return

def greet(strsay):
    if strsay == "Hello!":
	sonarValues =  memory_service.getListData(sonarValueList)
    	motion_service.move(20, 0, 0)
	#time.sleep(3.5)
    	motion_service.stopMove()
    	posture = "Stand"
    	speed = 0.7
    	rp_service.goToPosture(posture,speed)

    print(strsay)
    tts_service.say(strsay, _async=True)
    hello()
    posture = "Stand"
    speed = 0.7
    rp_service.goToPosture(posture,speed)
    return

def search():
    joint = ["HeadYaw"]
    angle = [0.5]
    time = [2.0]
    isAbsolute = True
    motion_service.angleInterpolation(joint, angle, time, isAbsolute)

    angle = [-0.5]
    motion_service.angleInterpolation(joint, angle, time, isAbsolute)

    angle = [0.0]
    motion_service.angleInterpolation(joint, angle, time, isAbsolute)

    return

def behind(strsay):
    search()
    print(strsay)
    tts_service.say(strsay, _async=True)
    time.sleep(5.0)
    return

def study(subject, level):
    if subject == "math":
        if level == "beginner":
            questions = random.sample(math_beginner.items(), 5)
        if level == "intermediate":
            questions = random.sample(math_intermediate.items(), 5)
        if level == "advanced":
            questions = random.sample(math_advanced.items(), 5)
    else:
        if level == "beginner":
            questions = random.sample(english_beginner.items(), 5)
        if level == "intermediate":
            questions = random.sample(english_intermediate.items(), 5)
        if level == "advanced":
            questions = random.sample(english_advanced.items(), 5)
    strsay = "I will ask you 5 questions. When you're ready to answer, touch my right or left hand."
    print(strsay)
    tts_service.say(strsay, _async=True)
    points = 0
    for i in range(len(questions)):
        strsay = questions[i][0]
        print(strsay)
        tts_service.say(strsay, _async=True)
        sonarValues =  memory_service.getListData(sonarValueList)
        start_time = time.time()
        while sonarValues[3] == 0.0 and sonarValues[4] == 0.0:
            sonarValues =  memory_service.getListData(sonarValueList)
            if time.time() - start_time >= 20.0:
                start_time = time.time()
                strsay = random.choice(encouragements)
                tts_service.say(strsay, _async=True)
            continue
        strsay = "Alright! What is your answer?"
        tts_service.say(strsay, _async=True)
        value = raw_input(strsay + " ")
        if value.lower() == questions[i][1]:
            points += 1
            strsay = "Yay! You're right! Good job!"
            print(strsay)
            tts_service.say(strsay, _async=True)
        else:
            strsay = "Oh no! That is not right! Don't worry, you'll get it right the next time!"
            print(strsay)
            tts_service.say(strsay, _async=True)
    strsay = "Alright, we finished this test. Let me see how it went..."
    print(strsay)
    tts_service.say(strsay, _async=True)
    think()
    time.sleep(2.0)
    if points >= 3:
        strsay = "Nice job! You passed the test!"
        print(strsay)
        tts_service.say(strsay, _async=True)
        cheer()
        if points == 5 and dataset[current_person.lower()][subject] != "advanced":
            strsay = "You answered correctly to all the questions. Do you want me to increase your level of proficiency in " + subject + "?"
            tts_service.say(strsay, _async=True)
            value = raw_input(strsay + " ")
            if value.lower() == "yes":
                if dataset[current_person.lower()][subject] == "beginner":
                    dataset[current_person.lower()][subject] = "intermediate"
                elif dataset[current_person.lower()][subject] == "intermediate":
                    dataset[current_person.lower()][subject] = "advanced"
                strsay = "Alright, I increased your " + subject + " level to " + dataset[current_person.lower()][subject] + "!"
                print(strsay)
                tts_service.say(strsay, _async=True)
            else:
                strsay = "Alright, I'll keep the level you are now"
                print(strsay)
                tts_service.say(strsay, _async=True)
    else:
        strsay = "Mmmhh... There's still some room for improvement. But don't worry, I'm sure you'll do better next time"
        print(strsay)
        tts_service.say(strsay, _async=True)   
        if points == 0 and dataset[current_person.lower()][subject] != "beginner":
            strsay = "Hey... the test didn't go very well. Do you want me to decrease your level of proficiency in " + subject + "?"
            tts_service.say(strsay, _async=True)
            value = raw_input(strsay + " ")    
            if value.lower() == "yes":
                if dataset[current_person.lower()][subject] == "intermediate":
                    dataset[current_person.lower()][subject] = "beginner"
                elif dataset[current_person.lower()][subject] == "advanced":
                    dataset[current_person.lower()][subject] = "intermediate"
                strsay = "Okay, I decreased your " + subject + " level to " + dataset[current_person.lower()][subject] + "!"
                print(strsay)
                tts_service.say(strsay, _async=True)
            else:
                strsay = "Alright, I'll keep the level you are now"
                print(strsay)
                tts_service.say(strsay, _async=True)
    return

class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pip", type=str, default=os.environ['PEPPER_IP'],
                        help="Robot IP address.  On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--pport", type=int, default=9559,
                        help="Naoqi port number")
    
    args = parser.parse_args()
    pip = args.pip
    pport = args.pport

    #Starting application
    try:
        connection_url = "tcp://" + pip + ":" + str(pport)
        app = qi.Application(["Say", "--qi-url=" + connection_url ])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + pip + "\" on port " + str(pport) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    app.start()
    session = app.session

    global memory_service
    global motion_service
    global tts_service
    global rp_service
    global audio_service
    global sonarValueList
    global sonarValues
    global dataset

    #Starting services
    memory_service=app.session.service("ALMemory")
    motion_service = session.service("ALMotion")
    tts_service = session.service("ALTextToSpeech")    
    rp_service = session.service("ALRobotPosture")
    audio_service = session.service("ALAudioPlayer")

    tts_service.setLanguage("English")
    tts_service.setVolume(1.0)
    tts_service.setParameter("speed", 1.0)

    sonarValueList = ["Device/SubDeviceList/Platform/Front/Sonar/Sensor/Value",
              	            "Device/SubDeviceList/Platform/Back/Sonar/Sensor/Value",
                                  "Device/SubDeviceList/Head/Touch/Middle/Sensor/Value",
                                  "Device/SubDeviceList/LHand/Touch/Back/Sensor/Value",
                                  "Device/SubDeviceList/RHand/Touch/Back/Sensor/Value",
                                   ]
    #######################################
    memory_service.insertData(sonarValueList[0], 2.0)
    memory_service.insertData(sonarValueList[1], 2.0)
    #######################################
    sonarValues =  memory_service.getListData(sonarValueList)

    dataset = {"mario" : {"math" : "advanced", "english" : "intermediate"}}

    global math_beginner
    global math_intermediate
    global math_advanced
    global english_beginner
    global english_intermediate
    global english_advanced
    global encouragements

    math_beginner = {"8 + 5 = " : "13",
                                  "15 - 7 = " : "8",
                                  "4 x 3 = " : "12",
                                  "18 / 3 = " : "6",
                                  "25 + 14 = " : "39",
                                  "30 - 12 = " : "18",
                                  "6 x 5 = " : "30",
                                  "45 / 5 = " : "9",
                                  "9 + 7 = " : "16",
                                  "22 - 10 = " : "12"
                                  }

    math_intermediate = {"1/2 + 1/3 = " : "5/6",
                                         "3/4 - 1/2 = " : "1/4",
                                         "20% of 50 is " : "10",
                                         "2/3 = 8/x. What is the value of x? " : "12",
                                         "2x + 5 = 13. What is the value of x? " : "4",
                                         "What is the area of a rectangle with length 4 and width 5?" : "20",
                                         "What is the mean of 4, 6, 8?" : "6",
                                         "What is the value of the hypotenuse of a triangle sides of length 3 and 4?" : "5",
                                         "3x - 7 > 5. What is the value of x? " : "x > 4"
                                         }

    math_advanced = {"x^2 - 5x + 6 = 0. What are the values of x? " : "2,3",
                                    "log2 (8) = " : "3",
                                    "sin(30) = " : "0.5",
                                    "What is the derivative of x^2?" : "2x",
                                    "(x+1)^3 = " : "x^3 + 3x^2 + 3x + 1"
                                    }

    english_beginner = {"The cat chased the ___. \nA) dog \nB) ball \nC) moon" : "b",
                                      "She loves to read ___. \nA) books \nB) clouds \nC) rocks" : "a",
                                      "We went swimming in the ___. \nA) park \nB) lake \nC) mountain" : "b",
                                      "My favorite color is ___. \nA) banana \nB) yellow \nC) elephant" : "b",
                                      "He rode his ___ to school. \nA) spaceship \nB) horse \nC) tree" : "b",
                                      "The sun is shining ___. \nA) brightly \nB) loudly \nC) quickly" : "a",
                                      "The ___ fell from the tree. \nA) moon \nB) apple \nC) cloud" : "b",
                                      "I have three ___. \nA) fingers \nB) chairs \nC) glasses" : "c",
                                      "The ___ was delicious. \nA) bed \nB) sandwich \nC) table" : "b",
                                      "We play games at ___. \nA) school \nB) ocean \nC) mountain" : "a"
                                      }

    english_intermediate = {"She plays the piano ___. \nA) sun \nB) fast \nC) perfectly" : "c",
                                            "The teacher explained the ___ clearly. \nA) air \nB) mathematics \nC) phone" : "b",
                                            "He went to the store to buy some ___. \nA) groceries \nB) sun \nC) rain" : "a",
                                            "They visited the ___ over the weekend. \nA) beach \nB) tree \nC) sky" : "a",
                                            "The ___ is full of stars. \nA) rain \nB) sun \nC) sky" : "c",
                                            "The dog barked ___. \nA) fast \nB) loudly \nC) tree" : "b",
                                            "We need to finish our ___. \nA) homework \nB) car \nC) cloud" : "a",
                                            "She likes to ride her ___. \nA) book \nB) moon \nC) bicycle" : "c",
                                            "He enjoys playing ___. \nA) apple \nB) football \nC) rain" : "b",
                                            "They visited the ___. \nA) museum \nB) sun \nC) bed" : "a"
                                         }

    english_advanced = {"She studied hard for the ___. \nA) exam \nB) banana \nC) star" : "a",
                                       "The novel was set in ___ times. \nA) rain \nB) ancient \nC) book" : "b",
                                       "They discussed the ___. \nA) home \nB) rain \nC) weather" : "c",
                                       "The scientist made a ___ discovery. \nA) important \nB) home \nC) rock" : "a",
                                       "He received a ___ from his boss. \nA) sand \nB) promotion \nC) apple" : "b",
                                       "She played the ___ beautifully. \nA) sun \nB) rock \nC) piano" : "c",
                                       "The painting hung on the ___. \nA) museum \nB) wall \nC) tree" : "b",
                                       "The movie was ___. \nA) exciting \nB) tree \nC) apple" : "a",
                                       "They enjoyed their ___. \nA) star \nB) vacation \nC) sun" : "b",
                                       "He wrote a ___ to his friend. \nA) rain \nB) apple \nC) letter" : "c"
                                       }

    encouragements = [ "I know you can do it!",
                                      "I believe in you!",
                                      "You got this!"
                                    ]

    global current_person
    global subject

    greeted = False
    current_person = ""

    while not greeted:
        sonarValues =  memory_service.getListData(sonarValueList)
        #print(sonarValues) # front, back
        closest = min(sonarValues[0], sonarValues[1])
        behind_sentences = ["Hey! Who's behind me? Come in front of me so I can see you!",
                                           "I can't see behind me, come in front of me so I can see you!"
                                            ]
        behind_sentence = random.choice(behind_sentences)
        if sonarValues[2] > 0:
            #behind(behind_sentence)
            behind("Hey! Who's behind me? Come in front of me so I can see you!")
            continue
        if closest < 2.0:
            if closest == sonarValues[1]:
                behind("I can't see behind me, come in front of me so I can see you!")
                #behind(behind_sentence)
                continue
            greeted = True
            greet("Hello!")
            strsay = "I'm Pepper. What's your name?"
            tts_service.say(strsay, _async=True)
            value = raw_input(strsay + " ")
            current_person = value
            if value == "stop":
                greet("Bye, see you next time!\n")
                return
            if value.lower() not in dataset:
                dataset[value.lower()] = {"math" : "none", "english" : "none"}
                strsay = "Hi " + current_person + "! Nice to meet you!"
                print(strsay)
                tts_service.say(strsay, _async=True)
            else:
                strsay = "Welcome back, " + current_person + "!"
                print(strsay)
                tts_service.say(strsay, _async=True)
            

    stop_flag = False
    identified = False

    while not stop_flag:
        try:
            strsay = "How can I help you?"
            tts_service.say(strsay, _async=True)
            value = raw_input(strsay + " ")

        except KeyboardInterrupt:
            greet("Bye, see you next time!\n")
            return

        if value == "stop":
            greet("Bye, see you next time!\n")
            return
        elif "tablet" in value:
            with cd("modim_demo/scripts"):
                os.system("python demo.py")
        elif "study" in value:
            got_it = False
            while not got_it:
                strsay = "Alright! What do you want to study, English or Math?" 
                tts_service.say(strsay, _async=True)
                value = raw_input(strsay + " ")
                if value.lower() != "math" and value.lower() != "english":
                    strsay = "I did not understand. Can you repeat?"
                    print(strsay)
                    tts_service.say(strsay, _async=True)
                    continue
                subject = value.lower()
                got_it = True
            level = dataset[current_person.lower()][subject]
            if level == "none":
                got_it = False
                while not got_it:
                    strsay = "I see you have never studied " + subject + " with me. What level would you say you are? Beginner, Intermediate or Advanced?"
                    tts_service.say(strsay, _async=True)
                    value = raw_input(strsay + " ")
                    if value.lower() != "beginner" and value.lower() != "intermediate" and value.lower() != "advanced":
                        strsay = "I did not understand. Can you repeat?"
                        print(strsay)
                        tts_service.say(strsay, _async=True)
                        continue
                    dataset[current_person.lower()][subject] = value.lower()
                    level = dataset[current_person.lower()][subject]
                    got_it = True
            strsay = "I see your level is " + level + ". Let's start!"
            print(strsay)
            tts_service.say(strsay, _async=True)
            study(subject, level)


if __name__ == "__main__":
    main()
