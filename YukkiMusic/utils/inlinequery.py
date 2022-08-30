#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from YukkiMusic import app
from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent,
                            Message)
@app.on_message(filters.command("inlinehelp"))
async def help_message(bot, message):
    await message.reply_photo(
        photo="https://telegra.ph//file/e937426b58e31a881c25f.jpg",
        caption="""Hey how can i help You. The Basic Commands is /id & /info.
If you have any questions join support
Group and ask🤍❤️
Thank you for using Beta""")



answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="SEARCH ANY QUERY HERE🔍",
            input_message_content=InputTextMessageContent("/start"),
        ),
    ]
)
