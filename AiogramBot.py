from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import bot_token 
import BotApiworker
import re

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

switchTypeDict = {
    "clicky": "1",
    "linear": "2",
    "tactile": "3",
}


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    """React on command /start"""

    await message.bot.send_message(message.from_user.id, "Hello!\nInsert some command.")


@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    """React on command /help"""

    await message.bot.send_message(message.from_user.id, "There is the example of my commands:\n\n`/getall`\n\n`/getbyid id:1`\n\n`/delete id:10`\n\n`/insert name:gateron price:65 color:red type:linear`\n\n`/update id:14 name:gateron price:65 color:red type:linear`\n\nYou can simply click on the command and it will copy to your clipboard.", parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(content_types=["text"])
async def commander(message: types.Message):
    """React on all another commands"""

    if "/getbyid" in message.text:
        switchId = "".join(re.findall(r"id:([0-9]+)", message.text))
        if switchId != "":
            await message.reply(BotApiworker.GetById(switchId))
        else:
            await message.reply("You forgot to specify your text!\nExample: `/getbyid id:1`", parse_mode=types.ParseMode.MARKDOWN)

    if "/getall" in message.text:
        await message.reply(BotApiworker.GetAll())

    if "/delete" in message.text:
        switchId = "".join(re.findall(r"id:([0-9]+)", message.text))
        if switchId != "":
            await message.reply(BotApiworker.DeleteById(switchId))
        else:
            await message.reply("You forgot to specify your text!\nExample: `/delete id:10`", parse_mode=types.ParseMode.MARKDOWN)
    if "/photo" in message.text:
        await bot.send_photo(message.from_user.id, photo=open("maxresdefault.jpg", "rb"))

    if "/insert" in message.text:
        switchName = "".join(re.findall(r"name:([\w]+)", message.text))
        switchPrice = "".join(re.findall(r"price:([0-9]+)", message.text))
        switchColor = "".join(re.findall(r"color:([\w]+)", message.text))
        switchType = "".join(re.findall(r"type:([\w]+)", message.text))
        if switchName != "" and switchPrice != "" and switchColor != "":
            if switchType in switchTypeDict:
                switchTypeId = int(switchTypeDict[switchType])
                await message.reply(BotApiworker.InsertOne(switchName, switchPrice, switchColor, switchTypeId))
            else:
                await message.reply("I dont know this switch type!\nHere is mine: `clicky`, `linear`, `tactile`\nExample: `/insert name:gateron price:65 color:red type:linear`", parse_mode=types.ParseMode.MARKDOWN)
        else:
            await message.reply("You forgot to specify your text!\nExample: `/insert name:gateron price:65 color:red type:linear`", parse_mode=types.ParseMode.MARKDOWN)

    if "/update" in message.text:
        switchId = "".join(re.findall(r"id:([0-9]+)", message.text))
        switchName = "".join(re.findall(r"name:([\w]+)", message.text))
        switchPrice = "".join(re.findall(r"price:([0-9]+)", message.text))
        switchColor = "".join(re.findall(r"color:([\w]+)", message.text))
        switchType = "".join(re.findall(r"type:([\w]+)", message.text))
        if switchName != "" and switchPrice != "" and switchColor != "":
            if switchType in switchTypeDict:

                switchTypeId = int(switchTypeDict[switchType])
                await message.reply(BotApiworker.UpdateById(switchId, switchName, switchPrice, switchColor, switchTypeId))
            else:
                await message.reply("I dont know this switch type!\nHere is mine: `clicky`, `linear`, `tactile`\nExample: `/update id:14 name:gateron price:65 color:red type:linear`", parse_mode=types.ParseMode.MARKDOWN)
        else:
            await message.reply("You forgot to specify your text!\nExample: `/update id:14 name:gateron price:65 color:red type:linear`", parse_mode=types.ParseMode.MARKDOWN)


if __name__ == "__main__":
    executor.start_polling(dp)
