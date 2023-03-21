from selenium import webdriver
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
import time


def main():
    try:
        # 初期化
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/chromium-browser'
        options.add_argument('--headless')
        options.add_argument("--remote-debugging-port=9292")
        options.add_argument("--user-data-dir=/home/pi/.config/chromium")
        options.add_argument("--profile-directory=Profile 3")

        # ドライバの機動
        service = Service(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options) 

        # waitオブジェクト
        wait = WebDriverWait(driver, 30)
        driver.set_page_load_timeout(30)
        driver.set_script_timeout(30)

        # test
        driver.get("https://www.google.com/")
        driver.save_screenshot('../../pic/google.png')
        driver.get("chrome://version")
        driver.save_screenshot('../../pic/chrome-version.png')
        
        # Notionのログインページに移動する
        driver.get("https://www.notion.so/login")

        try:
            # 既にログイン済みの場合
            wait.until(expected_conditions.invisibility_of_element_located((By.ID, "notion-app")))
            driver.save_screenshot('../../pic/notion-loggedin.png')
        except Exception:
            googleBtn = driver.find_element(By.XPATH, "//div[contains(text(), 'Google')]")
            googleBtn.click()
            driver.switch_to.window(driver.window_handles[-1])
            driver.save_screenshot('../../pic/notion-not-loggedin.png')

        # １ページ目
        driver.get("https://www.notion.so/minakoph/db687f05bc83414796ba44d61dcdb9c1")
        try:
            wait.until(expected_conditions.title_contains("ダッシュボード"))
            driver.save_screenshot('../../pic/page-1.png')
        except Exception:
            driver.save_screenshot('../../pic/page-1-timeout.png')
        # 2ページ目
        driver.get("https://www.notion.so/minakoph/7a7ceb2723cb439c9f08391e61563826")
        try:
            wait.until(expected_conditions.title_contains("タスク一覧・予定一覧"))
            driver.save_screenshot('../../pic/page-2.png')
        except Exception:
            driver.save_screenshot('../../pic/page-2-timeout.png')
        # 3ページ目
        driver.get("https://www.notion.so/minakoph/fc28b51cd2e745e9a72d58c4c4f6dc81")
        try:
            wait.until(expected_conditions.title_contains("ガントチャート・目標一覧"))
            driver.save_screenshot('../../pic/page-3.png')
        except Exception:
            driver.save_screenshot('../../pic/page-3-timeout.png')
        # ドライバの終了
        driver.quit()
    except:
        print(traceback.format_exc()) 
        driver.quit()

if __name__ == '__main__':
    main()