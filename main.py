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
    "PyDF-BOT",
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
       #   text_path = TXT_LOCATION + f"txt{message.chat.id}.txt"     
          await txt.edit("Extracting Text from PDF...")
       #   print(page_no.extractText())
       #   time.sleep(10)
          page_content = """ """ # EmptyString
          
       #   await txt.edit(f"This is what i found \n {page_content}")
          with open('bughunter0.txt', 'w') as text_path:   
                for page in range (0,num_of_pages):
                    file_write = open('bughunter0.txt','a+')
                  # try: 
                    page_no = pdf_reader.getPage(page) # Iteration of page number
                    page_content = page_no.extractText()
                    file_write.write(f"Page Number{page}   \n {page_content} BugHunterBots")   
                #   except Exception as error:
                #   await message.reply_text(f"Oops!! Error occurred while Extracting page number {page}")
                #   await message.reply_text(f"**Page Number : {page}**\n\n`{page_content} `\n @BugHunterBots")
                #   os.write(file_write,page_content)
                #   os.close(file_write)
       
          await message.reply_document(text_path,caption="©@BugHunterBots")
        # await message.reply_document(text_path1,caption="©@BugHunterBots")
    #      pdf_path.close ()             # pdfFileObject Closed  
          os.remove(pdf_path)
          os.remove(text_path)  
          os.remove('bughunter0.txt')  
   #  except ValueError as error :
     #     await txt.delete()
     #     os.remove(pdf_path)
    #      os.remove(text_path)    
    #      tx = await message.reply_text("Oops !!! Something Wrong occurred")

@bughunter0.on_message(filters.command(["info"]))
async def info(bot, message):
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
**Author :** `{info.author}`
**Creator :** `{info.creator}`
**Producer :** `{info.producer}`
**Subject :** `{info.subject}`
**Title :** `{info.title}`
**Pages :** `{num_of_pages}`""")

         os.remove(pdf_path)
  #   except Exception as error :
    #     await message.reply_text("Oops , error")


bughunter0.run()
