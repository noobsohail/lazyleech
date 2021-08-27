# lazyleech - Telegram bot primarily to leech from torrents and upload to Telegram
# Copyright (c) 2021 lazyleech developers <theblankx protonmail com, meliodas_bot protonmail com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton
from pykeyboard import InlineKeyboard

@Client.on_message(filters.private & filters.command('start'))
async def start_cmd(client, message):

    msg = f"""
<b>Hi, I Am Alive.</b>
        """
    buttons = InlineKeyboard(row_width=2)
    buttons.add(
        InlineKeyboardButton(
            'Join Now', url='https://t.me/indianimein',
        ))
    await message.reply(msg, reply_markup=buttons)
