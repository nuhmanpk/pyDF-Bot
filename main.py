# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os 
from os import error
import logging
import pyrogram
import PyPDF2
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message

    
bughunter0 = Client(
    "Sticker-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)
START_STR = """
Hi **{}**, I'm PyDF Bot. I can Provide all Help regarding PDF file
"""
ABOUT = """
**BOT:** `PYDF BOT`
**AUTHOR :** [bughunter0](https://t.me/bughunter0)
**SERVER :** `Heroku`
**LIBRARY :** `Pyrogram`
**SOURCE :** [BugHunterBots](https://t.me/bughunterbots)
**LANGUAGE :** `Python 3.9`
"""
HELP = """
No one gonna Help You !!
"""

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/PyDF/")
TXT_LOCATION =  os.environ.get("TXT_LOCATION", "./DOWNLOADS/txt/")

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ABOUT',callback_data='cbabout'),
        InlineKeyboardButton('HELP',callback_data='cbhelp')
        ],
        [
        InlineKeyboardButton('↗ Join Here ↗', url='https://t.me/BughunterBots'),
        ]]
        
    )
CLOSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back',callback_data='cbclose'),
        ]]
    )

@bughunter0.on_callback_query()
async def cb_data(bot, update):  
    if update.data == "cbhelp":
        await update.message.edit_text(
            text=HELP,
            reply_markup=CLOSE_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "cbabout":
        await update.message.edit_text(
            text=ABOUT,
            reply_markup=CLOSE_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.edit_text(
            text=START_STR.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTON
        )

@bughunter0.on_message(filters.command(["start"]))
async def start(bot, update):
     await update.reply_text(
        text=START_STR.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )

@bughunter0.on_message(filters.command(["test"]))
async def pdf_to_text(bot, message):
     await message.reply_text("Validating Pdf ")
     pdf_path = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf"
     await message.reply_to_message.download(pdf_path)  
     pdf_reader = PyPDF2.PdfFileReader(pdf_path)
     num_of_pages = pdfReader.numPages()
     page_no = pdfReader.getPage(0)
     text_path = TXT_LOCATION + f"{message.chat.id}.txt"     
     for page in range (page_no,num_of_pages):
         text_path1 = open(TXT_LOCATION + f"{message.chat.id}.txt","a") 
         text_path1.write(f"{pageObj.extractText()}\n")
         
     text_path1.close()
     await update.reply_document(text_path,caption="©@BugHunterBots")
     await update.reply_document(text_path1,caption="©@BugHunterBots")
                                 
bughunter0.run()
