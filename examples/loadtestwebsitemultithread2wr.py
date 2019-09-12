from seleniumbase import BaseCase
import time
from selenium.webdriver.common.action_chains import ActionChains
import datetime as dt
from parameterized import parameterized
import ctypes
import sys
import random

# C:\GitHub\TourTron
# pytest loadtestwebsitemultithread2wr.py -s -n 8

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
    ])
    def test_basic(self):
        for i in range(1):
            
            #ipdb.set_trace()
            
            self.open("https://raidtheroom.online")

            # Intro Page: Walk through tour
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))

            # Navigate to next page
            self.click("#next")
            time.sleep(random.randint(2,5))
            self.update_text("#name","ready")
            time.sleep(random.randint(2,5))
            self.click("#final")
            time.sleep(random.randint(2,5))
            
            # Puzzle 1: Walk through tour and then navigate to second puzzle.
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))


            # Interact with Right Turn Maze
            self.click("#Q1B")
            time.sleep(random.randint(2,5))
            self.click("#Q2A")
            time.sleep(random.randint(2,5))
            self.click("#Q3B")
            time.sleep(random.randint(2,5))

            self.click("#ccwturn")
            time.sleep(random.randint(2,5))
            self.click("#ccwturn")
            time.sleep(random.randint(2,5))
            self.click("#ccwturn")
            time.sleep(random.randint(2,5))
            self.click("#cwturn")
            time.sleep(random.randint(2,5))
            self.click("#cwturn")
            time.sleep(random.randint(2,5))
            self.click("#cwturn")
            time.sleep(random.randint(2,5))
            self.click("#cwturn")
            time.sleep(random.randint(2,5))

            self.click("#smallmaze")
            time.sleep(random.randint(2,5))

            self.click("#mazeimg")
            time.sleep(random.randint(2,5))

            self.click("#smallmaze")
            time.sleep(random.randint(2,5))

            self.click("#mazeimg")
            time.sleep(random.randint(2,5))

            # Navigate to next page
            self.click("#next")
            time.sleep(random.randint(2,5))
            self.update_text("#name","resources")
            time.sleep(random.randint(2,5))
            self.click("#final")
            time.sleep(random.randint(2,5))

            # Puzzle 2: Walk through tour and then navigate to third puzzle.
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))


            # Interact with Tic-Tac-Toe Page
            self.click("#Q1A")
            time.sleep(random.randint(2,5))
            self.click("#Q2B")
            time.sleep(random.randint(2,5))
            self.click("#Q3C")
            time.sleep(random.randint(2,5))
            self.click("#Q4C")
            time.sleep(random.randint(2,5))

            self.click("#C1Img")
            time.sleep(random.randint(2,5))
            self.click("#C1Img")
            time.sleep(random.randint(2,5))
            self.click("#C1Img")
            time.sleep(random.randint(2,5))
            self.click("#C2Img")
            time.sleep(random.randint(2,5))
            self.click("#C4Img")
            time.sleep(random.randint(2,5))
            self.click("#C6Img")
            time.sleep(random.randint(2,5))
            self.click("#C8Img")
            time.sleep(random.randint(2,5))
            self.click("#C9Img")
            time.sleep(random.randint(2,5))

            # Navigate to next page
            self.click("#next")
            time.sleep(random.randint(2,5))
            self.update_text("#name","future")
            time.sleep(random.randint(2,5))
            self.click("#final")
            time.sleep(random.randint(2,5))

            # Interact with iSpy Page
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))

            # Interact with iSpy Custom Content Questions
            self.click("#Q1A")
            time.sleep(random.randint(2,5))
            self.click("#Q2B")
            time.sleep(random.randint(2,5))
            self.click("#Q3C")
            time.sleep(random.randint(2,5))


            # Navigate to next page
            self.click("#next")
            time.sleep(random.randint(2,5))
            self.update_text("#name","consult")
            time.sleep(random.randint(2,5))
            self.click("#final")
            time.sleep(random.randint(2,5))


            # Interact with Magic Square
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))

            # Interact with  Magic Square Custom Content Questions
            self.click("#Q1T")
            time.sleep(random.randint(2,5))
            self.click("#Q2F")
            time.sleep(random.randint(2,5))
            self.click("#Q3T")
            time.sleep(random.randint(2,5))
            self.click("#Q4F")
            time.sleep(random.randint(2,5))
            self.click("#Q5T")
            time.sleep(random.randint(2,5))
            self.click("#Q6T")
            time.sleep(random.randint(2,5))
            self.click("#Q7T")
            time.sleep(random.randint(2,5))
            self.click("#Q8T")
            time.sleep(random.randint(2,5))


            # Navigate to next page
            self.click("#next")
            time.sleep(random.randint(2,5))
            self.update_text("#name","environment")
            time.sleep(random.randint(2,5))
            self.click("#final")
            time.sleep(random.randint(2,5))

            time.sleep(2)           
            # Interact with Codebreaker
            self.click('#tour1 > font:nth-child(2) > button')
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))
            self.click("button[class='hopscotch-nav-button next hopscotch-next']")
            time.sleep(random.randint(2,5))

            # Interact with  Codebreaker Custom Content Questions
            self.click("#Q1A")
            time.sleep(random.randint(2,5))
            self.click("#Q2B")
            time.sleep(random.randint(2,5))
            self.click("#Q3C")
            time.sleep(random.randint(2,5))