import time
import pyautogui as pg
import keyboard



screenWidth, screenHeight = pg.size()
def perform_action():
    pg.moveTo(17, 305)
    pg.dragTo(1391, 630,0.3, button='left') 
    with pg.hold('ctrl'):
        pg.press(['c'])

    with pg.hold('ctrl'):
        pg.press(['t'])
    pg.press(['g'])
    pg.press(['enter'])
    time.sleep(0.2)
    with pg.hold('ctrl'):
        pg.press(['v'])
    pg.press(['enter'])
  

     


def detect_key_press():
    action_flag = False 

    while True:
        try:
            if keyboard.is_pressed(';'):
                if not action_flag:
                    perform_action()
                    action_flag = True
            else:
                action_flag = False
        except:
            break
                
        

# Start detecting key press
detect_key_press()



input()

   


#print(pg.position())
