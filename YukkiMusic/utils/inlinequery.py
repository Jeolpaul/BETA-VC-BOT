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
@app.on_message(
    filters.command("inlinehelp")
    & filters.group
    & filters.private
    & ~filters.edited
)
async def inlinehelp(client, message: Message, _):
    response = await message.reply_text(
        text="""YOU CAN SEARCH YOUTUBE IN TELEGRAM USING ME

Just Type ```@BETA_VC_BOT``` On Your Keyboard At Any Chat
Eg:- ```@BETA_VC_BOT How To Setup A Music Bot In Telegram | Telegram Bot | How to make a music bot in telegram```

LIKE THIS YOU CAN SEARCH anything ON YT""",
    )



answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="SEARCH ANY QUERY HERE🔍",
            input_message_content=InputTextMessageContent("/start"),
        ),
    ]
)
