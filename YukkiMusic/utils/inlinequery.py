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
            title="SEARCH YOUTUBE",
            description=f"SEARCH HERE ANYTHING TO GET YT LINKZ!.",
            thumb_url="https://graph.org/file/bb1ebd7c68d600dae4600.jpg",
            input_message_content=InputTextMessageContent("You Can Search Youtube On Inline Using Me, By Typing My Username on your Keyborad and search any query!!  \n\neg: ```@BETA_VC_BOT How To Make A Bot``` Like This You Can Search Any Query🙌🏻"),
        ),
    ]
)
