import undetected_chromedriver as uc
import traceback

def main():
    try:
        # 初期化
        driver = uc.Chrome(user_data_dir='/home/pi/.config/chromium/Profile 2')

        # test
        driver.get("https://www.google.co.jp/")
        driver.save_screenshot('../../pic/google.png')
        driver.get("chrome://version")
        driver.save_screenshot('../../pic/chrome-version.png')
        
    except:
        print(traceback.format_exc()) 

if __name__ == '__main__':
    main()

