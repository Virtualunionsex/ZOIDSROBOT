from telethon.errors.rpcerrorlist import YouBlockedUserError
from KynanRobot import telethn as tbot
from KynanRobot.events import register
from KynanRobot import ubot2 as ubot
from asyncio.exceptions import TimeoutError


@register(pattern="^/sg ?(.*)")
@register(pattern="^/check_name ?(.*)")
async def lastname(steal):
    steal.pattern_match.group(1)
    puki = await steal.reply("```Mengambil Informasi Pengguna!```")
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await puki.edit("```Mohon Balas Ke Pesan Pengguna!```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMata_beta_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await puki.edit("```Balas Pesan Pengguna Asli!```")
        return
    await puki.edit("```Mohon tunggu!```")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```Kesalahan, laporkan ke @ZennXSupport```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await puki.edit(f"`{r.message}`")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                ) 
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await puki.edit("```Saya Tidak Dapat Menemukan Informasi Pengguna Ini, Pengguna Ini Belum Pernah Mengubah Namanya Sebelumnya.```")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await puki.edit(f"```{response.message}```")
            await ubot.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await puki.edit("`Saya Tidak Bisa, Maap..`")


__help__ = """
 ──「 ꜱᴀɴɢᴍᴀᴛᴀ 」──

➣ *Perintah yang tersedia:*
ᐉ /sg *:* Untuk Mengambil Informasi.
"""
__mod_name__ = "ꜱᴀɴɢᴍᴀᴛᴀ"
