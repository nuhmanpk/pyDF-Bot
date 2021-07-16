# © BugHunterCodeLabs ™
# © bughunter0
# 2021
# Copyright - https://en.m.wikipedia.org/wiki/Fair_use

import os 
from os import error, system, name
import logging
import pyrogram
import PyPDF2
import time
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
# TXT_LOCATION =  os.environ.get("TXT_LOCATION", "./DOWNLOADS/txt/")
path = './DOWNLOADS/txt/bughunter0.txt'

  

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

@bughunter0.on_callback_query() # callbackQuery()
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

@bughunter0.on_message(filters.command(["start"])) # StartCommand
async def start(bot, update):
     await update.reply_text(
        text=START_STR.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )

@bughunter0.on_message(filters.command(["test"])) # PdfToText NoT Working!!
async def pdf_to_text(bot, message):
   #  try :
          txt =await message.reply_text("Validating Pdf ")
          pdf_path = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" #pdfFileObject
          await txt.edit("Downloading.....")
          await message.reply_to_message.download(pdf_path)  
          await txt.edit("Downloaded File")
          pdf = open(pdf_path,'rb')
          pdf_reader = PyPDF2.PdfFileReader(pdf) #pdfReaderObject
          await txt.edit("Getting Number of Pages....")
          num_of_pages = pdf_reader.getNumPages()
          await txt.edit(f"Found {num_of_pages} Page")
          page_no = pdf_reader.getPage(0) # pageObject
        # text_path = TXT_LOCATION + f"txt{message.chat.id}.txt"     
          await txt.edit("Extracting Text from PDF...")
          print(page_no.extractText())
          time.sleep(10)
          page_content = f"""{page_no.extractText()}""" # EmptyString
          text_path = path
      #    await txt.edit(f"This is what i found\n{page_content}")
          with open('bughunter0.txt', 'w') as fp:   
                for page in range (0,num_of_pages):
                    os.open('bughunter0.txt',os.O_RDWR & os.O_APPEND)
                    page_content = page_no.extractText()
                    print (page_content)
                    time.sleep(10)
                    await message.reply_text(f"{page_content} This is what i Found")
                    os.write('bughunter0.txt',page_content)
                    os.close('bughunter0.txt')
       
          await message.reply_document(text_path,caption="©@BugHunterBots")
        # await message.reply_document(text_path1,caption="©@BugHunterBots")
          pdf_path.close ()             # pdfFileObject Closed  
          os.remove(pdf_path)
          os.remove(text_path)    
   #  except ValueError as error :
          await txt.delete()
          os.remove(pdf_path)
          os.remove(text_path)    
          tx = await message.reply_text("Oops !!! Something Wrong occurred")
@bughunter0.on_message(filters.command(["info"]))
async def clear(bot, message):
   #  try:
         txt =await message.reply_text("Validating Pdf ")  
         pdf_path = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" #pdfFileObject
         await txt.edit("Downloading.....")
         await message.reply_to_message.download(pdf_path)  
         await txt.edit("Downloaded File")
         pdf = open(pdf_path,'rb')
         pdf_reader = PyPDF2.PdfFileReader(pdf) #pdfReaderObject
         await txt.edit("Getting Number of Pages....")
         num_of_pages = pdf_reader.getNumPages()
         await txt.edit(f"Found {num_of_pages} Page")
         await txt.edit("Getting PDF info..")
         info = pdf_reader.getDocumentInfo()
         await txt.edit(f"""
**author :** {info.author}
**creator :** {info.creator}
**producer :** {info.producer}
**subject :** {info.subject}
**title :** {info.title}
**Pages :** {num_of_pages}""")

         os.remove(pdf_path)
  #   except Exception as error :
    #     await message.reply_text("Oops , error")


bughunter0.run()
