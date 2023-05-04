import pyautogui
import time

# List of templates
imgs = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']

def click(i):
    counter = 0
    for loc in pyautogui.locateAllOnScreen(imgs[i - 1], confidence=0.9, region=(596, 163, 620, 560)):
        center = pyautogui.center(loc)
        pyautogui.click(center)
        time.sleep(0.5)
        counter+= 1
        if counter== 3:
            break

def detect_imgs():
    num_list = [0] * len(imgs)
    for i, img in enumerate(imgs):
        for loc in pyautogui.locateAllOnScreen(img, confidence=0.9):
            num_list[i] += 1
    return num_list

# Set the fail-safe to prevent infinite loops
pyautogui.FAILSAFE = True

# Initialize the last position and wait time
wait_time = 0
last_pos = pyautogui.position()

# Main loop
while True:
    current_pos = pyautogui.position()
    if current_pos != last_pos:
        last_pos = current_pos
        wait_time = 0
    else:
        wait_time += 1
        if wait_time >= 5:
            pyautogui.click(997, 870)
            wait_time = 0
            continue
    
    # Detect the number of occurrences of each image
    num_list = detect_imgs()
    max_index, max_item = max(enumerate(num_list), key=lambda x: x[1])
    
    # Click on the image with the most occurrences
    click(max_index + 1)
