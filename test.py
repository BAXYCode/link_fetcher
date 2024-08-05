# https://github.com/ultrafunkamsterdam/undetected-chromedriver/discussions/1798

import nodriver as uc 
import pyautogui
import os
async def main():
    driver = await uc.start()

    tab = await driver.get("https://dexscreener.com/ethereum/0x3885fbe4cd8aed7b7e9625923927fa1ce30662a3")
 
    print("finding checkbox")
    location = pyautogui.locateOnScreen("/home/benjaminlaine/git/venv/checkbox_dark.png", confidence=0.8, grayscale=True, minSearchTime=10)  # 
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


