from selenium import webdriver
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
def main():
    try:
        # 初期化
        chrome_option = webdriver.ChromeOptions()
        chrome_option.binary_location = '/usr/bin/chromium-browser'
        chrome_option.add_argument('--headless')
        chrome_option.add_argument("--remote-debugging-port=9222")
        # ドライバの機動
        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_option) 
        # waitオブジェクト
        wait = WebDriverWait(driver, 30)
        driver.set_page_load_timeout(30)
        driver.set_script_timeout(30)

        driver.get("https://www.notion.so/login")
        try:
            # 既にログイン済みの場合
            wait.until(expected_conditions.invisibility_of_element_located((By.ID, "notion-app")))
            driver.save_screenshot('../../pic/notion-login-1.png')
        except Exception:
            googleBtn = driver.find_element(By.XPATH, "//div[contains(text(), 'Google')]")
            googleBtn.click()
            driver.save_screenshot('../../pic/notion-login-2.png')

        # スクリーンショットを取る
        wait.until(expected_conditions.title_contains("ダッシュボード"))
        driver.get("https://www.notion.so/minakoph/db687f05bc83414796ba44d61dcdb9c1")
        driver.save_screenshot('../../pic/page-1.png')
        wait.until(expected_conditions.title_contains("タスク一覧・予定一覧"))
        driver.get("https://www.notion.so/minakoph/7a7ceb2723cb439c9f08391e61563826")
        driver.save_screenshot('../../pic/page-2.png')
        wait.until(expected_conditions.title_contains("ガントチャート・目標一覧"))
        driver.get("https://www.notion.so/minakoph/fc28b51cd2e745e9a72d58c4c4f6dc81")
        driver.save_screenshot('../../pic/page-3.png')
        # ドライバの終了
        driver.quit()
    except:
        print(traceback.format_exc()) 
        driver.quit()

if __name__ == '__main__':
    main()