# import pillow library (PIL)(using pip install pillow)
from PIL import ImageGrab

# take a screenshot from the whole screen
screenshot=ImageGrab.grab()

# or for customizing size you can do this
# screenshot=ImageGrab.grab(50,50,100,100)

# save it with default name.
take=screenshot.save("screenshot.png")

# close the screenshot
z=screenshot.close()