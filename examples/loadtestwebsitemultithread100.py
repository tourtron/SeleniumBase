from seleniumbase import BaseCase
import time
from selenium.webdriver.common.action_chains import ActionChains
import datetime as dt
from parameterized import parameterized
import ctypes
import sys

# E:\Dropbox\Raid the Room\Automation\2019-09-03
# pytest loadtestwebsitemultithread100.py -s -n 100

# pytest loadtestwebsitemultithread100.py -s -n 100 --headless

class MyTestClass(BaseCase):

    @parameterized.expand([

        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],

    ])
    def test_basic(self):
        for i in range(1):
            waitVar = 0.5 # Set wait timer between actions
            
            #ipdb.set_trace()
            
            self.open("https://raidtheroom.online")

            # Intro Page: Walk through tour
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)

            # Navigate to next page
            self.click("#next")
            time.sleep(waitVar)
            self.update_text("#name","ready")
            time.sleep(waitVar)
            self.click("#final")
            time.sleep(waitVar)
            
            # Puzzle 1: Walk through tour and then navigate to second puzzle.
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)


            # Interact with Right Turn Maze
            self.click("#Q1B")
            time.sleep(waitVar)
            self.click("#Q2A")
            time.sleep(waitVar)
            self.click("#Q3B")
            time.sleep(waitVar)

            self.click("#ccwturn")
            time.sleep(waitVar)
            self.click("#ccwturn")
            time.sleep(waitVar)
            self.click("#ccwturn")
            time.sleep(waitVar)
            self.click("#cwturn")
            time.sleep(waitVar)
            self.click("#cwturn")
            time.sleep(waitVar)
            self.click("#cwturn")
            time.sleep(waitVar)
            self.click("#cwturn")
            time.sleep(waitVar)

            self.click("#smallmaze")
            time.sleep(waitVar)

            self.click("#mazeimg")
            time.sleep(waitVar)

            self.click("#smallmaze")
            time.sleep(waitVar)

            self.click("#mazeimg")
            time.sleep(waitVar)

            # Navigate to next page
            self.click("#next")
            time.sleep(waitVar)
            self.update_text("#name","resources")
            time.sleep(waitVar)
            self.click("#final")
            time.sleep(waitVar)

            # Puzzle 2: Walk through tour and then navigate to third puzzle.
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)


            # Interact with Tic-Tac-Toe Page
            self.click("#Q1A")
            time.sleep(waitVar)
            self.click("#Q2B")
            time.sleep(waitVar)
            self.click("#Q3C")
            time.sleep(waitVar)
            self.click("#Q4C")
            time.sleep(waitVar)

            self.click("#C1Img")
            time.sleep(waitVar)
            self.click("#C1Img")
            time.sleep(waitVar)
            self.click("#C1Img")
            time.sleep(waitVar)
            self.click("#C2Img")
            time.sleep(waitVar)
            self.click("#C4Img")
            time.sleep(waitVar)
            self.click("#C6Img")
            time.sleep(waitVar)
            self.click("#C8Img")
            time.sleep(waitVar)
            self.click("#C9Img")
            time.sleep(waitVar)

            # Navigate to next page
            self.click("#next")
            time.sleep(waitVar)
            self.update_text("#name","future")
            time.sleep(waitVar)
            self.click("#final")
            time.sleep(waitVar)

            # Interact with iSpy Page
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)

            # Interact with iSpy Custom Content Questions
            self.click("#Q1A")
            time.sleep(waitVar)
            self.click("#Q2B")
            time.sleep(waitVar)
            self.click("#Q3C")
            time.sleep(waitVar)


            # Navigate to next page
            self.click("#next")
            time.sleep(waitVar)
            self.update_text("#name","consult")
            time.sleep(waitVar)
            self.click("#final")
            time.sleep(waitVar)


            # Interact with Magic Square
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)

            # Interact with  Magic Square Custom Content Questions
            self.click("#Q1T")
            time.sleep(waitVar)
            self.click("#Q2F")
            time.sleep(waitVar)
            self.click("#Q3T")
            time.sleep(waitVar)
            self.click("#Q4F")
            time.sleep(waitVar)
            self.click("#Q5T")
            time.sleep(waitVar)
            self.click("#Q6T")
            time.sleep(waitVar)
            self.click("#Q7T")
            time.sleep(waitVar)
            self.click("#Q8T")
            time.sleep(waitVar)


            # Navigate to next page
            self.click("#next")
            time.sleep(waitVar)
            self.update_text("#name","environment")
            time.sleep(waitVar)
            self.click("#final")
            time.sleep(waitVar)

            time.sleep(2)           
            # Interact with Codebreaker
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(waitVar)

            # Interact with  Codebreaker Custom Content Questions
            self.click("#Q1A")
            time.sleep(waitVar)
            self.click("#Q2B")
            time.sleep(waitVar)
            self.click("#Q3C")
            time.sleep(waitVar)