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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply
from pyrogram.types import User, Message, Document 

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

@bughunter0.on_message(filters.document | (filters.document & filters.forwarded)) 
async def document(bot, message):
  message_id=int(message.message_id)
  await message.reply_text(text=" ◆ /pdf2txt - Extract text to Txt file \n ◆ /info to Get PDF information",reply_markup=ForceReply(True),reply_to_message_id=message_id)
  
@bughunter0.on_message(filters.command(["pdf2txt"])) # PdfToText 
async def pdf_to_text(bot, message):
      try :
           if message.reply_to_message:
                pdf_path = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" #pdfFileObject
                txt = await message.reply_text("Downloading.....")     
                await message.reply_to_message.download(pdf_path)  
                await txt.edit("Downloaded File")
                pdf = open(pdf_path,'rb')
                pdf_reader = PyPDF2.PdfFileReader(pdf) #pdfReaderObject
                await txt.edit("Getting Number of Pages....")
                num_of_pages = pdf_reader.getNumPages()
                await txt.edit(f"Found {num_of_pages} Page")
                page_no = pdf_reader.getPage(0) # pageObject
                await txt.edit("Extracting Text from PDF...")
                page_content = """ """ # EmptyString   
                with open(f'{message.chat.id}.txt', 'a+') as text_path:   
                  for page in range (1,num_of_pages+1):
                      file_write = open(f'{message.chat.id}.txt','a+') 
                      page_no = pdf_reader.getPage(page) # Iteration of page number
                      page_content = page_no.extractText()
                      file_write.write(f"\n page number - {page} \n")
                      file_write.write(f" {page_content} ")   
                      file_write.write(f"\n © BugHunterBots \n ")
                   #  await message.reply_text(f"**Page Number  :  {page}  **\n\n  ` {page_content} `\n     @BugHunterBots\n\n") # Use this Line of code to get Pdf Text as Messages
                        
                with open(f'{message.chat.id}.txt', 'a+') as text_path:  
                      await message.reply_document(f"{message.chat.id}.txt",caption="©@BugHunterBots")      
         
                os.remove(pdf_path)
                os.remove(f"{message.chat.id}.txt")  
           else :
                await message.reply("Please Reply to PDF file")
      except Exception as error :
           await txt.delete()
           await message.reply_text(f"{error}")
           os.remove(pdf_path)
           os.remove(f"{message.chat.id}.txt")      
           
@bughunter0.on_message(filters.command(["info"]))
async def info(bot, message):
     try:
         if message.reply_to_message:
              txt = await message.reply_text("Validating Pdf ")  
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
         else:
             await message.reply_text("Please Reply to a Pdf File")
     except Exception as error :
         await message.reply_text(f"Oops , {error}")

@bughunter0.on_message(filters.command(["merge"])) # Under Maintenance
async def merge(bot, message):
      try:
         txt = await message.reply_text("Validating Pdf ")  
         pdf_path = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" #pdfFileObject
         pdf2 = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" # Second pdf
         output = DOWNLOAD_LOCATION + f"{message.chat.id}.pdf" # Output file
         await txt.edit("Downloading.....")
         await message.reply_to_message.download(pdf_path)  
         await txt.edit("Downloaded File")
         pdf = open(pdf_path,'rb')
         pdf_reader = PyPDF2.PdfFileReader(pdf) #pdfReaderObject
         await message.reply_text("Send me the File to merge")
         @bughunter0.on_message((filters.private | filters.forwarded | filters.reply) & filters.document)
         async def read(bot, message):
          try:
             txt = await message.reply_text("Downloading...")
             await message.download(pdf2)  
             pdf2open = open(pdf2,'rb')
             pdfMerger = PyPDF2.PdfFileMerger() # pdf Merger Object
             pdfs = [pdf_path,pdf2]
             for pdf in pdfs:
                 pdfMerger.append(pdf)
             with open(output, 'wb') as f:
                 pdfMerger.write(f)
             await message.reply_text("Uploading...")
             await message.reply_document(document=output ,caption="@BugHunterBots")
             return
          except Exception as error:
             await message.reply_text(f"{error}")
             print(error)
      except Exception as error:
              await message.reply_text(f"{error}")
              print(error)
bughunter0.run()
