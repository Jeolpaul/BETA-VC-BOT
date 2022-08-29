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
            title="GITHUB REPO",
            description=f"GET THE REPO OF MEH!",
            thumb_url="https://graph.org/file/bb1ebd7c68d600dae4600.jpg",
            input_message_content=InputTextMessageContent(
                    "CLICK THE BELOW BUTTON TO GET MY REPO"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "GIT REPO💡",
                            url="https://github.com/Jeolpaul/BETA-MUSIC-OFFICIAL-"
                        )]
                    ]
                )
            ),
        ),
    ]
)
