#  Copyright (c) 2021 thanosuser

import logging
import re

from pyrogram import Client
from pyrogram.errors import (
    FloodWait,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from telethon import Button, TelegramClient, events
from telethon.errors.rpcerrorlist import FloodWaitError as fwe
from telethon.errors.rpcerrorlist import PasswordHashInvalidError as phi
from telethon.errors.rpcerrorlist import PhoneCodeExpiredError as pce
from telethon.errors.rpcerrorlist import PhoneCodeInvalidError as pci
from telethon.errors.rpcerrorlist import SessionPasswordNeededError as spn
from telethon.sessions import StringSession

from strings import *
from var import Var

logging.basicConfig(level=logging.INFO)


bot = TelegramClient(None, Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)


async def makeSession(type, api_id: int, api_hash: str):
    if "pyro" in type:
        return Client(":memory:", api_id=int(api_id), api_hash=str(api_hash))
    return TelegramClient(StringSession(), api_id=int(api_id), api_hash=str(api_hash))


@bot.on(events.NewMessage(pattern="/start", incoming=True, func=lambda e: e.is_private))
async def begin(e):
    if e.fwd_from:
        return
    await e.reply(
        "This is THANOS PRO Session Generator [Bot](https://telegra.ph/file/c8fe5de96a7968636edc4.mp4) Choose Options Below)",
        buttons=[
            [Button.inline("Telethon Session", data="tele")],
            [Button.inline("Pyrogram Session", data="pyro")],
            [Button.inline("Thanos Session", data="tele")],
        ],
    )


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("tele")))
async def tl(e):
    await e.delete()
    async with bot.conversation(e.chat_id) as conv:
        await conv.send_message(GIVE_API)
        response = conv.wait_event(events.NewMessage(chats=e.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await conv.send_message(ABORT)
        api_id = res.message.message
        await conv.send_message(GIVE_HASH)
        response = conv.wait_event(events.NewMessage(chats=e.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await conv.send_message(ABORT)
        api_hash = res.message.message
        try:
            newbot = await makeSession("tele", api_id=int(api_id), api_hash=api_hash)
            await newbot.connect()
        except BaseException:
            newbot = await makeSession("tele", api_id=Var.API_ID, api_hash=Var.API_HASH)
            await newbot.connect()
        await conv.send_message(PHONE)
        response = conv.wait_event(events.NewMessage(chats=e.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await conv.send_message(ABORT)
        phone = res.message.message.replace(" ", "")
        try:
            await newbot.send_code_request(phone)
        except fwe:
            return await conv.send_message(FLOOD.format(fwe.seconds))
        except BaseException:
            await conv.send_message(PHONE_AGAIN)
            response = conv.wait_event(events.NewMessage(chats=e.chat_id))
            res = await response
            if "/cancel" in res.message.message:
                return await conv.send_message(ABORT)
            phone = res.message.message.replace(" ", "")
            try:
                await newbot.send_code_request(phone)
            except BaseException:
                return await conv.send_message(PHONE_WRONG)
        await conv.send_message(CODE)
        response = conv.wait_event(events.NewMessage(chats=e.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await conv.send_message(ABORT)
        code = res.message.message.replace(" ", "")
        try:
            await newbot.sign_in(phone=phone, code=code, password=None)
        except pce:
            return await conv.send_message(EXPIRED)
        except pci:
            await conv.send_message(CODE_AGAIN)
            response = conv.wait_event(events.NewMessage(chats=e.chat_id))
            res = await response
            if "/cancel" in res.message.message:
                return await conv.send_message(ABORT)
            code = res.message.message.replace(" ", "")
            try:
                await newbot.sign_in(phone=phone, code=code, password=None)
            except pci:
                return await conv.send_message(CODE_WRONG)
        except spn:
            await conv.send_message(PASS)
            response = conv.wait_event(events.NewMessage(chats=e.chat_id))
            res = await response
            if "/cancel" in res.message.message:
                return await conv.send_message(ABORT)
            password = res.message.message
            try:
                await newbot.sign_in(password=password)
            except phi:
                await conv.send_message(PASS_AGAIN)
                response = conv.wait_event(events.NewMessage(chats=e.chat_id))
                res = await response
                if "/cancel" in res.message.message:
                    return await conv.send_message(ABORT)
                password = res.message.message
                try:
                    await newbot.sign_in(password=password)
                except BaseException:
                    return conv.send_message(PASS_WRONG)
        except BaseException:
            return conv.send_message(WRONG)
        sess = newbot.session.save()
        await conv.send_message(SESSION.format(sess))
        await newbot.disconnect()
        return


@bot.on(events.callbackquery.CallbackQuery(data=re.compile("pyro")))
async def _(e):
    await e.delete()
    async with bot.conversation(e.chat_id) as conv:
        await conv.send_message(GIVE_API)
        response = conv.wait_event(events.NewMessage(chats=e.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await conv.send_message(ABORT)
        api_id = res.message.message
        await conv.send_message(GIVE_HASH)
        response = conv.wait_event(events.NewMessage(chats=e.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await conv.send_message(ABORT)
        api_hash = res.message.message
        try:
            newbot = await makeSession("pyro", api_id=int(api_id), api_hash=api_hash)
            await newbot.connect()
        except ConnectionError:
            await newbot.disconnect()
            await newbot.connect()
        except BaseException:
            newbot = await makeSession("pyro", api_id=Var.API_ID, api_hash=Var.API_HASH)
            await newbot.connect()
        await conv.send_message(PHONE)
        response = conv.wait_event(events.NewMessage(chats=e.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await conv.send_message(ABORT)
        phone = res.message.message.replace(" ", "")
        try:
            code = await newbot.send_code(phone)
        except PhoneNumberInvalid:
            await conv.send_message(PHONE_AGAIN)
            response = conv.wait_event(events.NewMessage(chats=e.chat_id))
            res = await response
            if "/cancel" in res.message.message:
                return await conv.send_message(ABORT)
            phone = res.message.message.replace(" ", "")
            try:
                code = await newbot.send_code(phone)
            except BaseException:
                return await conv.send_message(PHONE_WRONG)
        except FloodWait as f:
            return await conv.send_message(FLOOD.format(f))
        except BaseException:
            return await conv.send_message(WRONG)
        await conv.send_message(CODE)
        response = conv.wait_event(events.NewMessage(chats=e.chat_id))
        res = await response
        if "/cancel" in res.message.message:
            return await conv.send_message(ABORT)
        otp = res.message.message.replace(" ", "")
        try:
            await newbot.sign_in(phone, code.phone_code_hash, phone_code=otp)
        except PhoneCodeInvalid:
            await conv.send_message(CODE_AGAIN)
            response = conv.wait_event(events.NewMessage(chats=e.chat_id))
            res = await response
            if "/cancel" in res.message.message:
                return await conv.send_message(ABORT)
            otp = res.message.message.replace(" ", "")
            try:
                await newbot.sign_in(phone, code.phone_code_hash, phone_code=otp)
            except PhoneCodeInvalid:
                return await conv.send_message(CODE_WRONG)
        except PhoneCodeExpired:
            return await conv.send_message(EXPIRED)
        except SessionPasswordNeeded:
            await conv.send_message(PASS)
            response = conv.wait_event(events.NewMessage(chats=e.chat_id))
            res = await response
            if "/cancel" in res.message.message:
                return await conv.send_message(ABORT)
            password = res.message.message
            try:
                await newbot.check_password(password)
            except BaseException:
                await conv.send_message(PASS_AGAIN)
                response = conv.wait_event(events.NewMessage(chats=e.chat_id))
                res = await response
                if "/cancel" in res.message.message:
                    return await conv.send_message(ABORT)
                password = res.message.message
                try:
                    await newbot.check_password(password)
                except BaseException:
                    return await conv.send_message(PASS_WRONG)
        except Exception as er:
            print(er)
            return await conv.send_message(WRONG)
        sess = await newbot.export_session_string()
        await conv.send_message(PYSESSION.format(sess))
        await newbot.disconnect()
        return


print("Bot Started")

bot.run_until_disconnected()
