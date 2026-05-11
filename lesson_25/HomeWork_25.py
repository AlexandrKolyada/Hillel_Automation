from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

BASE_URL_AUTH = "https://guest:welcome2qauto@qauto2.forstudy.space/"

browser = WebDriver()
browser.implicitly_wait(5)

try:
    browser.get(BASE_URL_AUTH)
    print(f"Page title: {browser.title}\n")

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

    # XPATH
    xpath_locators = {
        "1. button 'Sign up'": "//button[contains(text(), 'Sign up')]",
        "2. button 'Sign In' in header": "//button[text()='Sign In']",
        "3. logog in header (class)": "//a[@class='header_logo']",
        "4. link 'Home'": "//a[contains(text(), 'Home')]",
        "5. button 'About'": "//button[@class='btn header-link' and text()='About']",
        "6. button 'Contacts'": "//button[@class='btn header-link' and text()='Contacts']",
        "7. Title H1": "//div[@class='hero-descriptor']//h1",
        "8. description H1": "//div[contains(@class, 'hero-descriptor')]//p",
        "9. Logo from parent header": "//header//a[contains(@class, 'header_logo')]",
        "10. Link  Facebook in footer": "//a[contains(@href, 'facebook')]",
        "11. Link Telegram in footer": "//a[contains(@href, 't.me') or contains(@href, 'telegram')]",
        "12. Link Youtube in footer": "//a[contains(@href, 'youtube')]",
        "13. Link Instagram in footer": "//a[contains(@href, 'instagram')]",
        "14. Link LinkedIn in footer": "//a[contains(@href, 'linkedin')]",
        "15. Link Hillel about href": "//a[contains(@href, 'ithillel.ua')]",
        "16. Link Hillel about text": "//a[contains(text(), 'ithillel.ua')]",
        "17. Email support (mailto)": "//footer//a[contains(@href, 'mailto')]",
        "18. Email developers about text": "//a[contains(text(), 'developer')]",
        "19. Email developers about href": "//a[contains(@href, 'mailto:developer')]",
        "20. Navi in header (navi)": "//nav[contains(@class, 'header_nav')]",
        "21. First section (Hero)": "//section[contains(@class, 'section hero')]",
        "22. Section title 'About'": "//h2[contains(text(), 'About') or text()='About']",
        "23. Section title 'Contacts'": "//h2[contains(text(), 'Contacts') or text()='Contacts']",
        "24. Button first part header (language)": "//div[contains(@class, 'header_right')]//button",
        "25. Copyright in the footer (any paragraf)": "//footer//p"
    }

    # CSS SELECTOR
    css_locators = {
        "1. Button 'Sign up'": "button.hero-descriptor_btn",
        "2. Button 'Sign In'": "button.btn-outline-white",
        "3. Logo in header": "a.header_logo",
        "4. Activ link in header": "a.header-link",
        "5. Button 'About'": "button[appscrollto='aboutSection']",
        "6. Button 'Contacts'": "button[appscrollto='contactsSection']",
        "7. Main title H1": "div.hero-descriptor > h1",
        "8. Paragraf description H1": "div.hero-descriptor p",
        "9. Logo via header": "header .header_logo",
        "10. Facebook in footer": "a[href*='facebook']",
        "11. Telegram in footer": "a[href*='t.me'], a[href*='telegram']",
        "12. Youtube in footer": "a[href*='youtube']",
        "13. Instagram in footer": "a[href*='instagram']",
        "14. LinkedIn in footer": "a[href*='linkedin']",
        "15. Link in Hillel attribute": "a[href*='ithillel.ua']",
        "16. Email developer about attribute": "a[href*='mailto:developer']",
        "17. Email for main mailto": "footer a[href^='mailto']",
        "18. Navigation container": "nav.header_nav",
        "19. Footer container": "footer",
        "20. Social icons (general class)": "a.socials_link",
        "21. First icon (Facebook) via class": "a.socials_link:nth-of-type(1)",
        "22. Language selection button (first button in header)": "header button.btn",
        "23. Section title 'About'": "h2",
        "24. section 'Contacts' (class or tag)": "div.contacts-section, section",
        "25. Copyright in the footer (any paragraf)": "footer p"
    }

    print("=== test 25 XPATH  ===")
    for name, xpath in xpath_locators.items():
        try:
            element = browser.find_element(By.XPATH, xpath)
            print(f"✅ {name}: FOUND")
        except Exception:
            print(f"❌ {name}: NOT FOUND")

    print("\n=== test 25 CSS locator ===")
    for name, css in css_locators.items():
        try:
            element = browser.find_element(By.CSS_SELECTOR, css)
            print(f"✅ {name}: FOUND")
        except Exception:
            print(f"❌ {name}: NOT FOUND")

finally:
    print("\nTest completed")
    browser.quit()