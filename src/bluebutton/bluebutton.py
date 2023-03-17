#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
picdir = os.path.join(os.getcwd(), '../../pic')

import sys
sys.path.append('../../')
import logging
from lib import epd5in65f
from PIL import Image,ImageDraw,ImageFont
import evdev
import subprocess
import time

logging.basicConfig(level=logging.DEBUG)

def doProcess(idx):
    try:
        if idx == 0:
            Page_1 = Image.open(os.path.join(picdir, '_page-1.jpg'))
            epd.display(epd.getbuffer(Page_1))
        if idx == 1:
            Page_2 = Image.open(os.path.join(picdir, '_page-2.jpg'))
            epd.display(epd.getbuffer(Page_2))
        if idx == 2:
            Page_3 = Image.open(os.path.join(picdir, '_page-3.jpg'))
            epd.display(epd.getbuffer(Page_3))
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd5in65f.epdconfig.module_exit()
        exit()

if __name__ == '__main__':
    # 初期化
    epd = epd5in65f.EPD()
    epd.init()
    epd.Clear()

    f_read = open('bluebutton-mode.txt', 'r')

    # 初回実行
    currentIndex = 0
    doProcess(currentIndex)

    f_read = open('bluebutton-mode.txt', 'r')
    prevModeStr = f_read.read()
    prevMode = prevModeStr.rstrip()
    f_read.close()

    while True:
      f_read = open('bluebutton-mode.txt', 'r')
      modeStr = f_read.read()
      mode = modeStr.rstrip()
      f_read.close()

      if mode != prevMode:

        if mode.rstrip() == 'incriment':
          
          print('incriment')
          
          # 参照するプロセスのIndexを更新
          if currentIndex < 2:
              currentIndex = currentIndex + 1
          else:
              currentIndex = 0
          # 新しいプロセスの取得
          doProcess(currentIndex)
          # 綺麗にする
          prevMode = 'none'
          f_write = open('bluebutton-mode.txt', 'w')
          f_write.write('none')
          f_write.close()
        elif mode.rstrip() == 'home':
          
          print('home')
          
          currentIndex = 0
          # 新しいプロセスの取得
          doProcess(currentIndex)
          # 綺麗にする
          prevMode = 'none'
          f_write = open('bluebutton-mode.txt', 'w')
          f_write.write('none')
          f_write.close()
        # sleep
        time.sleep(1) 
    