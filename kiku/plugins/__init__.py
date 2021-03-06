#    kiku - UserBot
#    Copyright (C) 2020 kiku

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon.tl.types import Channel

from kiku import *
from kiku import ALIVE_NAME, bot, lionver
from kiku.LionConfig import Config, Var

# stats
if Var.PRIVATE_GROUP_ID:
    log = "Enabled"
else:
    log = "Disabled"

if Config.TG_BOT_USER_NAME_BF_HER:
    bots = "Enabled"
else:
    bots = "Disabled"

if Var.LYDIA_API_KEY:
    lyd = "Enabled"
else:
    lyd = "Disabled"

if Config.SUDO_USERS:
    sudo = "Disabled"
else:
    sudo = "Enabled"

if Var.PMSECURITY.lower() == "off":
    pm = "Disabled"
else:
    pm = "Enabled"

KIKUUSER = str(ALIVE_NAME) if ALIVE_NAME else "@LionXsupport"

kiku = f"π»πΈπΎπ½ ππ΄πππΈπΎπ½: {kikuver}\n"
kiku += f"π»πΎπΆ πΆππΎππΏ: {log}\n"
kiku += f"πΌπ π°πππΈπππ°π½π π±πΎπ: {bots}\n"
kiku += f"π»ππ³πΈπ°: {lyd}\n"
kiku += f"πππ³πΎ πππ΄π: {sudo}\n"
kiku += f"πΏπΌ ππ΄π²πππΈππ: {pm}\n"
kiku += f"\nππΈππΈπ @teamkiku π΅πΎπ π°πππΈπππ°π½π.\n"
kikustats = f"{kiku}"

KIKU_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def lion_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            if entity.megagroup:
                if entity.creator or entity.admin_rights:
                    a.append(entity.id)
    return len(a), a
