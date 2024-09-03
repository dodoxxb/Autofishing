import cv2 as cv
import pyautogui
import time

if __name__ == '__main__':
    i = 0
    while(1):

        if i > 1e3:
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            break

        template = cv.imread('./1658573608832.png')      im = pyautogui.screenshot('./1.png', region=(2400, 320, 160, 150))
        # im = pyautogui.screenshot('./1.png', region=(2150, 350, 50, 50))
        # compare target img with screenshot
        target = cv.imread('./1.png')
        target = cv.cvtColor(target, cv.COLOR_RGB2GRAY)

        template = cv.cvtColor(template, cv.COLOR_RGB2GRAY)
        theight, twidth = template.shape[:2]
        result = cv.matchTemplate(target, template, cv.TM_SQDIFF_NORMED)
        cv.normalize(result, result, 0, 1, cv.NORM_MINMAX, -1)
        min_val0, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        template = cv.imread('./1658684431124.png')
        template = cv.cvtColor(template, cv.COLOR_RGB2GRAY)
        theight, twidth = template.shape[:2]
        result = cv.matchTemplate(target, template, cv.TM_SQDIFF_NORMED)
        cv.normalize(result, result, 0, 1, cv.NORM_MINMAX, -1)
        min_val00, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if (min_val0 > 0 and min_val0 < 5e-11) or (min_val00 > 0 and min_val00 < 5e-11):
            print("Waiting!", min_val0, min_val00)
            continue
  
        template = cv.imread('./2.png')
        template = cv.cvtColor(template, cv.COLOR_RGB2GRAY)
        theight, twidth = template.shape[:2]
        result = cv.matchTemplate(target, template, cv.TM_SQDIFF_NORMED)
        cv.normalize(result, result, 0, 1, cv.NORM_MINMAX, -1)
        min_val1, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        template = cv.imread('./22.png')
        template = cv.cvtColor(template, cv.COLOR_RGB2GRAY)
        theight, twidth = template.shape[:2]
        result = cv.matchTemplate(target, template, cv.TM_SQDIFF_NORMED)
        cv.normalize(result, result, 0, 1, cv.NORM_MINMAX, -1)
        min_val2, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # control mouse

        if (min_val1 > 0 and min_val1 < 5e-11) or (min_val2 > 0 and min_val2 < 5e-11):
            print("Fish!", min_val1, min_val2)

            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            time.sleep(1)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            time.sleep(2)
            # i += 1

