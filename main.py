#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.getcwd(), 'pic')
libdir = os.path.join(os.getcwd(), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from lib import epd5in65f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

def main():
    try:
        logging.info(picdir)
        
        epd = epd5in65f.EPD()

        epd.init()
        epd.Clear()

        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
        font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)

        # Himage = Image.new('RGB', (epd.width, epd.height), 0xffffff)  # 255: clear the frame
        # draw = ImageDraw.Draw(Himage)
        # draw.text((10, 160), u'minako-ph', font = font30, fill = epd.BLACK)
        # draw.text((10, 200), u'minako-ph', font = font30, fill = epd.ORANGE)
        # draw.text((10, 240), u'minako-ph', font = font30, fill = epd.GREEN)
        # draw.text((10, 280), u'minako-ph', font = font30, fill = epd.BLUE)
        # draw.text((10, 320), u'minako-ph', font = font30, fill = epd.RED)
        # draw.text((10, 360), u'minako-ph', font = font30, fill = epd.YELLOW)
        # draw.line((20, 50, 70, 100), fill = 0)
        # draw.line((70, 50, 20, 100), fill = 0)
        # draw.rectangle((20, 50, 70, 100), outline = 0)
        # draw.line((165, 50, 165, 100), fill = 0)
        # draw.line((140, 75, 190, 75), fill = 0)
        # draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
        # draw.rectangle((80, 50, 130, 100), fill = 0)
        # draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
        # epd.display(epd.getbuffer(Himage))
        # time.sleep(3)

        Himage = Image.open(os.path.join(picdir, 'mock-2.jpg'))
        epd.display(epd.getbuffer(Himage))
        time.sleep(5)
        
        # epd.Clear()
        # epd.sleep()
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd5in65f.epdconfig.module_exit()
        exit()

def clear():
    epd = epd5in65f.EPD()
    epd.init()
    epd.Clear()
    epd.sleep()

# main()
clear()