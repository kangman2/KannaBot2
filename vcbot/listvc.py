# KannaBot - UserBot
# All Rights @TeamUltroid < https://github.com/TeamUltroid/Ultroid/ >
# 
# Editado por @fnixdev

from . import *


@asst.on_message(
    filters.command(["listvc", f"listvc@{vcusername}"])
    & filters.user(VC_AUTHS())
    & ~filters.edited
)
async def list_handler(_, message):
    OUT = ""
    if len(list(CallsClient.active_calls.keys())) == 0:
        return await eor(message, "No Active Group Calls Running..")
    OUT += "**• List of All Active Calls •**\n\n"
    for ke in CallsClient.active_calls.keys():
        stat = CallsClient.active_calls[ke]
        OUT += f"• `{ke}` : `{stat}`\n"
    await eor(message, OUT)


@Client.on_message(
    filters.outgoing & filters.command("listvc", HNDLR) & ~filters.edited
)
async def llhnf(_, message):
    await list_handler(_, message)
