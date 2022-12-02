from asyncio import gather

from .aio import aiohttpsession as session

SOURCE = """[Github](https://github.com/Jeolpaul/BETA-VC-BOT) | [Updates](t.me/beta_botz)
```----------------
| Contributors |
----------------```
{dev} """


async def get(url: str, *args, **kwargs):
    async with session.get(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data
