

import asyncio

from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    xx = f"HERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n\n`{ss}`\n\nGENERATED BY BETA"
    ok = await i.send_message("me", xx)
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n") 
    print("\nGENERATED BY BETA \n")


asyncio.run(main())