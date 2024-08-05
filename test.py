# https://github.com/ultrafunkamsterdam/undetected-chromedriver/discussions/1798

import nodriver as uc 
import pyautogui
import os
import sys
async def main():
    address = sys.argv[1]
    fullPathScreenshot = sys.argv[2]
    driver = await uc.start()

    tab = await driver.get("https://dexscreener.com/ethereum/{address}".format(address=address))
 
    print("finding checkbox")
    location = pyautogui.locateOnScreen("{fullPathScreenshot}".format(fullPathScreenshot=fullPathScreenshot), confidence=0.8, grayscale=True, minSearchTime=10)  # 
    if location:
        center = pyautogui.center(location)
        pyautogui.click(center)
    else:
        print("Can't find location")

    print("finding the website link")
    await tab.wait_for(" div.chakra-stack.custom-18cqgg9 > a.chakra-link.chakra-button.custom-1xt6654")
    website = await tab.query_selector_all(" div.chakra-stack.custom-18cqgg9 > a.chakra-link.chakra-button.custom-1xt6654") 
    for element in website:
        print(element.attributes)
if __name__ == "__main__":
    # Running the main function
    uc.loop().run_until_complete(main())


