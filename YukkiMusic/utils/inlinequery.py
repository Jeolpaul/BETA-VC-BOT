#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
                title="JOIN OUR UPDATES CHANNEL",
                input_message_content=InputTextMessageContent(
                    "JOIN OUR UPDATES CHANNEL"
                ),
                thumb_url="https://telegra.ph/file/5b4d3482480f426ea5ede.jpg",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Open channel",
                            url="https://t.me/beta_botz"
                        )]
                    ]
                )
            ),
        ),
    ]
)
