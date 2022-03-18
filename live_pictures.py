import pyautogui, os, time, sys
from PIL import Image, ImageOps

os.system('cls')
start = time.time()
topPosition = pyautogui.locateCenterOnScreen('top_left.png')
bottomPosition = pyautogui.locateCenterOnScreen('bottom.png')
print(topPosition)
print(bottomPosition)
try:
   #topPosition[0] += (-35, -58)
   topX = topPosition[0] - 16
   topY = topPosition[1] + 58
   bottomX = bottomPosition[0] + 15
   bottomY = bottomPosition[1] - 13
#Take a screenshot  (converts it to greyscale)          top is the topleft start, the width/length is the bottom - the top
   screenshot = ImageOps.grayscale(pyautogui.screenshot(region=(topX, topY, (bottomX-topX), (bottomY-topY))))
   screenshot.save('image.png')
except:
   print('didn\'t find it')

end = time.time()
print("Time it took: " + str(end - start))