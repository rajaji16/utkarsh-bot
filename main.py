from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from logger import logging
import time
import asyncio
from pyrogram.types import User, Message
import sys
import re
import os
import random
import sys
import requests
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message
from pyrogram import Client, filters
from p_bar import progress_bar
from subprocess import getstatusoutput
from aiohttp import ClientSession
import helper
from logger import logging
import time
import asyncio
from pyrogram.types import User, Message
import sys
import os
import random
import re
import tempfile
from urllib.parse import urlparse, parse_qs
import datetime
import aiohttp
import asyncio
import random




bot = Client("bot",
             bot_token=os.environ.get("BOT_TOKEN"),
             api_id=int(os.environ.get("API_ID")),
             api_hash=os.environ.get("API_HASH"))



wner_id = 5128979564
# Extras
failed_links = []  # List to store failed links
fail_cap =f"**➜ This file Contain Failed Downloads while Downloding \n You Can Retry them one more time **"

# counter
global videocount, pdfcount  # Declare videocount and pdfcount as global variables

processing_request = False  # Variable to track if a request is being processed

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/DRAGON_ZONEE_OWNER_BOT",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🪄 Updates Channel",
                url="https://t.me/+YRvfgtd4q5A5ZDI1",
            ),

        ],
    ]
)



Busy = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="👨🏻‍💻 Devloper",
                url="https://t.me/DRAGON_ZONEE_OWNER_BOT",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✨Join our Channel ✨ ",
                url="https://t.me/+YRvfgtd4q5A5ZDI1",
            ),

        ],
    ]
)


# @bot.on_message(filters.command(["logs"]) )
# async def send_logs(bot: Client, m: Message):
#     try:

#         # Assuming `assist.txt` is located in the current directory
#          with open("Assist.txt", "rb") as file:
#             sent= await m.reply_text("**📤 Sending you ....**")
#             await m.reply_document(document=file)
#             await sent.delete(True)
#     except Exception as e:
#         await m.reply_text(f"Error sending logs: {e}")


# # List of image URLs
# image_urls = [
#     "https://graph.org/file/5f422748ce4847cd37ef2.jpg",
#     "https://graph.org/file/726869795f1e2d34774b9.jpg",
#     # Add more image URLs as needed
# ]

# @bot.on_message(filters.command("start"))
# async def start_command(bot, message):
#     start_message = await bot.send_message(
#         message.chat.id,
#         "**Welcome to the Uploader bot!**"
#     )

#     await asyncio.sleep(0.5)
#     await start_message.edit_text(
#         "Welcome to the Uploader bot!\n\n"
#         "Initializing Uploader bot... 🤖\n\n"
#         "Progress: [⬜⬜⬜⬜⬜⬜⬜⬜] 0%\n\n"
#     )

#     await asyncio.sleep(0.5)
#     await start_message.edit_text(
#         "Welcome to the Uploader bot!\n\n"
#         "Loading features... ⏳\n\n"
#         "Progress: [🟪🟪🟪⬜⬜⬜⬜⬜] 25%\n\n"
#     )

#     await asyncio.sleep(0.5)
#     await start_message.edit_text(
#         "Welcome to the Uploader bot!\n\n"
#         "This may take a moment, sit back and relax! 😊\n\n"
#         "Progress: [🟧🟧🟧🟧⬜⬜⬜⬜] 50%\n\n"
#     )

#     await asyncio.sleep(0.5)
#     await start_message.edit_text(
#         "Welcome to the Uploader bot!\n\n"
#         "Almost done... 🎉\n\n"
#         "Progress: [🟥🟥🟥🟥🟥⬜⬜] 75%\n\n"
#     )

#     await asyncio.sleep(0.5)
#     await start_message.edit_text(
#         "Welcome to the Uploader bot!\n\n"
#         "Completed! ✅\n\n"
#         "Progress: [🟫🟫🟫🟫🟫🟫🟫🟫🟫] 100%\n\n"
#     )
#     await asyncio.sleep(0.5)

#     await start_message.delete()
#     chat_id = message.chat.id
#     await send_random_photo(bot, chat_id)

# async def send_random_photo(bot, chat_id):
#     width = random.randint(1100, 1250)
#     height = random.randint(600, 800)
#     await bot.send_photo(
#         chat_id=chat_id,
#         photo=f"https://picsum.photos/{width}/{height}.jpg",
#         caption=(
#             "**𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫 👋!**\n\n"
#             "**➠ 𝐈 AM DRM BOT 🕹️**\n"
#             "**➠ Can Extract Videos & Pdf Form Your Text File and Upload to Telegram**\n\n"
#             "**➠ 𝐔𝐬𝐞 /drm 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐅𝐫𝐨𝐦 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞**\n\n"
#             "**Meke Your 💾Txt File /txt**\n\n"
#             "**For Stop ⛔ working process ➡️ /stop or /restart Command**\n\n"
#             "**➠𝐌𝐚𝐝𝐞 𝐁𝐲: [🐲 𝗗𝗥𝗔𝗚𝗢𝗡 𝗭𝗢𝗡𝗘 🐲](https://t.me/DRAGON_ZONEE)**"
#         ),
#         reply_markup=InlineKeyboardMarkup(
#             [
#                 [InlineKeyboardButton("Contact Me", url="https://t.me/DRAGON_ZONEE_OWNER_BOT")]
#             ]
#         )
#     )


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):

        if failed_links:
         error_file_send = await m.reply_text("**📤 Sending you Failed Downloads List Before Stoping   **")
         with open("failed_downloads.txt", "w") as f:
          for link in failed_links:
            f.write(link + "\n")
    # After writing to the file, send it
         await m.reply_document(document="failed_downloads.txt", caption=fail_cap)
         await error_file_send.delete()
         os.remove(f'failed_downloads.txt')
         failed_links.clear()
         processing_request = False  # Reset the processing flag
         #await m.reply_text("**Note This Is BETA Stage May have Bugs  **")
         await m.reply_text("🚦**STOPPED**🚦", True)
         os.execl(sys.executable, sys.executable, *sys.argv)
        else:
         processing_request = False  # Reset the processing flag
         #await m.reply_text("**Note This Is BETA Stage May have Bugs  **")
         await m.reply_text("📍**STOPPED**📍", True)
         os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("**📍𝗥𝗘𝗦𝗧𝗔𝗥𝗧𝗘𝗗📍**", True)
    os.execl(sys.executable, sys.executable, *sys.argv)






@bot.on_message(filters.command(["txt"]))
async def account_login(bot: Client, m: Message):
    try:
        editable = await m.reply_text('𝗦𝗘𝗡𝗗 𝗠𝗘 𝗧𝗘𝗫𝗧 𝗧𝗢 𝗖𝗢𝗡𝗩𝗘𝗥𝗧 𝗜𝗡𝗧𝗢 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 🗃️')
        input_msg = await bot.listen(editable.chat.id)
        raw_text = input_msg.text
        await input_msg.delete(True)

        await editable.edit("𝗦𝗘𝗡𝗗 𝗠𝗘 𝗡𝗔𝗠𝗘 𝗧𝗢 𝗨𝗥 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 🤗")
        input_msg = await bot.listen(editable.chat.id)
        raw_text0 = input_msg.text
        await input_msg.delete(True)
        await editable.delete()

        path = f"./downloads/{m.chat.id}"

        file_name = f"{raw_text0}.txt"

        with open(file_name, "w") as file:
            file.write(raw_text)

        await bot.send_document(chat_id=m.chat.id, document=open(file_name, "rb"), caption=",")
        os.remove(file_name)
    except Exception as e:
        await m.reply_text('Failed: ' + str(e))

@bot.on_message(filters.command(["drm"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('**𝗦𝗘𝗡𝗗 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 🗂**')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))



    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("Invalid file input.")
           os.remove(x)
           return


    await editable.edit(f"𝗧𝗢𝗧𝗔𝗟 𝗟𝗜𝗡𝗞𝗦 𝗙𝗢𝗨𝗡𝗗 𝗜𝗡 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 𝗔𝗥𝗘 🫣 **{len(links)}**\n\n✍️ 𝗡𝗢𝗪 𝗦𝗘𝗡𝗗 𝗠𝗘 𝗙𝗥𝗢𝗠 𝗪𝗛𝗘𝗥𝗘 𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗜𝗡𝗜𝗧𝗜𝗔𝗟 𝗜𝗦 **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**𝗘𝗡𝗧𝗘𝗥 𝗖𝗢𝗨𝗥𝗦𝗘 𝗡𝗔𝗠𝗘 📝 𝗢𝗥 𝗦𝗘𝗡𝗗 𝗱 𝗧𝗢 𝗚𝗥𝗔𝗕 𝗙𝗥𝗢𝗠 𝗧𝗫𝗧 𝗙𝗜𝗟𝗘 📮.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0


    await editable.edit("**𝗘𝗡𝗧𝗘𝗥 𝗥𝗘𝗦𝗢𝗟𝗨𝗧𝗜𝗢𝗡 𝗙𝗢𝗥 𝗨𝗥 𝗟𝗘𝗖𝗧𝗨𝗥𝗘𝗦 🎬**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080"
        else:
            res = "UN"
    except Exception:
            res = "UN"



    await editable.edit("**𝗘𝗡𝗧𝗘𝗥 𝗨𝗥 𝗡𝗔𝗠𝗘 ✍️ 𝗔𝗦 𝗔 𝗛𝗜𝗚𝗛𝗟𝗜𝗚𝗛𝗧𝗘𝗥 💋 𝗧𝗢 𝗟𝗘𝗖𝗧𝗨𝗥𝗘𝗦 📇**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        MR = credit
    else:
        MR = raw_text3

    await editable.edit("𝗡𝗢𝗪 𝗦𝗘𝗡𝗗 𝗠𝗘 𝗧𝗛𝗘 🖼️ **𝗧𝗛𝗨𝗠𝗕𝗡𝗔𝗜𝗟 𝗨𝗥𝗟**\n\nEx : `https://graph.org/file/c9e4dcdd96af060ccc7c09b.jpg`\n\n𝗢𝗥 𝗦𝗘𝗡𝗗 `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V


            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Pragma': 'no-cache',
                    'Referer': 'http://www.visionias.in/',
                    'Sec-Fetch-Dest': 'iframe',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'cross-site',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'tencdn.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9'}).json()['url']

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9'}).json()['url']



            elif 'http://media-cdn-alisg.classplusapp.com' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9'}).json()['url']

            elif 'media-cdn.classplusapp.com' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9'}).json()['url']


            elif "edge.api.brightcove.com" in url: # Code made by Aditya
                url=url.split("bcov_auth=")[0]+"bcov_auth="+token
            elif 'tencdn' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': token, }).json()['url']

            elif 'tencdn' in url:
                id =  url.split("/")[-2]
                url =  "https://extractapi.vercel.app/classplus?link=https://tencdn.classplusapp.com/" + id + "/master.m3u8"

            elif "brightcove" in url:
                Master = url.split("?")
                src_url = Master[0].replace("/master.m3u8", "")
                src_auth = Master[1].split("=")[1]
                url = await master.generate_master_url(src_url, src_auth)

            elif 'testbook' in url:
                id =  url.split("/")[-2]
                url =  "https://extractapi.vercel.app/classplus?link=https://cpvod.testbook.com/" + id + "/playlist.m3u8"

            elif 'cpvod.testbook' in url:
                id =  url.split("/")[-2]
                url =  "https://extractapi.vercel.app/classplus?link=https://cpvod.testbook.com/" + id + "/playlist.m3u8"



            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "http://d.alphastudyofficial.live/v2/alpha/pw/download?v=https://d1d34p8vz63oiq.cloudfront.net/" + id + "/hls/" + raw_text2 + "/main.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "embed" in url:
                ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'

            elif "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:

                cc = f'**[ 🎥 ] Lᴇᴄ ɪᴅ. »** {str(count).zfill(3)}\n**Tɪᴛᴛʟᴇ »  ** `{name1} [{res}].mkv`\n\n**Bᴀᴛᴄʜ Nᴀᴍᴇ »** **{b_name}\n\n** **🌟 Dᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ » {MR}**\n'
                cc1 = f'**[ 📚 ] Pᴅғ ɪᴅ. »** {str(count).zfill(3)}\n**Tɪᴛᴛʟᴇ »  ** `{name1}.pdf` \n\n**Bᴀᴛᴄʜ Nᴀᴍᴇ »** **{b_name}\n\n** **🌟 Dᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ » {MR}**\n'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        #await copy.copy(chat_id = -1002008774612)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".mp3" in url:
                    try:
                        cmd = f'yt-dlp -x --audio-format mp3 -o "{name}.mp3" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        await bot.send_document(chat_id=m.chat.id,document=f'{name}.mp3', caption=cc2)
                        count += 1
                        os.remove(f'{name}.mp3')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**Dᴏᴡɴʟᴏᴀᴅɪɴɢ  ⏬**\n\n**Lᴇᴄ ɪᴅ. »** `{name}\n\nQᴜᴀʟɪᴛʏ. » {raw_text2}`\n\n**🌟**"
                    res_file = await helper.download_video(url, cmd, name)
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**⚠️ Downloading Failed**\n\n{str(e)}\n\n**Lᴇᴄ ɪᴅ.** » {name}\n\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("** 🌟 Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴏᴡɴʟᴏᴀᴅᴇᴅ Aʟʟ Lᴇᴄᴛᴜʀᴇs...! 🌟 **")


bot.run()

