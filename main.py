import os
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InputTextMessageContent
from pyrogram.types import InlineQueryResultArticle


Bot = Client(
    "tgDonatebot",
    bot_token = os.environ["bot_token"],
    api_id = int(os.environ["api_id"]),
    api_hash = os.environ["api_hash"]
)


START_TEXT = """Hᴇʏ! {}
☞ Vᴇʀʏ Hᴀᴘᴘʏ ᴛᴏ Kɴᴏᴡ Tʜᴀᴛ Yᴏᴜ ᴀʀᴇ here to Find Movies channle .
Tʜᴀɴᴋꜱ Fᴏʀ Uꜱɪɴɢ [Oᴜʀ Bᴏᴛꜱ](https://t.me/Latest_hindi_hd_Movies_Hub).
Mᴀᴅᴇ Wɪᴛʜ Lᴏᴠᴇ Fᴏʀ [Yᴏᴜ](tg://settings)"""

DONATE_BUTTONS = [
    InlineKeyboardButton(
        text='📥📥 MOVIES CHANNLES List 📥📥 ',
        callback_data='donateme'
    )
]

DONATE_TEXT = """Hᴇʏ! {}
📥📥 Yᴏᴜ Cᴀɴ JOIN LATEST MOVIES CHANNLE.📥📥
 `@Latest_hindi_hd_Movies_Hub`
Oʀ Cᴏɴᴛᴀcᴛ Uꜱ :- [ツowner 🇮🇳](https://t.me/DeltaBotsOfficial). """

BUTTON_TEXT = """ 👇👇 Click the Below Buttons To 👇👇 JOIN MOVIES CHANNLES.👇👇 """

MOVIES_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back ", callback_data="back"),
            InlineKeyboardButton(" ⭕️MOVIES⭕️ ", url="https://t.me/Latest_hindi_hd_Movies_Hub")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

PAY_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('🎬𝗠𝗢𝗩𝗜𝗘𝗦🎬', url='https://t.me/joinchat/vii7DDEvKCZkNDVl'),
            InlineKeyboardButton('💢𝗧𝗩 𝗦𝗘𝗥𝗜𝗘𝗦💢', url='https://t.me/joinchat/Qea8OllY2QUzMDY1')
        ],
        [
            InlineKeyboardButton("⭕️ 𝗠𝗢𝗩𝗜𝗘𝗦 ⭕️ ", url="https://t.me/Latest_hindi_hd_Movies_Hub"),
            InlineKeyboardButton("Ⓜ️ 𝗠𝗢𝗩𝗜𝗘𝗦 𝗕𝗔𝗖𝗞𝗨𝗣 Ⓜ️ ", url="https://t.me/joinchat/fWTl8WXeWX5kN2Fl")
        ],
        [
            InlineKeyboardButton("⭐️ 𝐌𝐎𝐕𝐈𝐄𝐒 𝐆𝐑𝐎𝐔𝐏 1⭐️", url="https://t.me/joinchat/RSzvS3qax24wMmNl"),
            InlineKeyboardButton("⭐️ 𝐌𝐎𝐕𝐈𝐄𝐒 𝐆𝐑𝐎𝐔𝐏 2⭐️", url="https://t.me/joinchat/L_lCa57jPUBhNzU1")
        ],
        [
            InlineKeyboardButton(" ⚡️MOVIES ⚡️ ",url="https://t.me/Latest_hindi_hd_Movies_Hub"),
            InlineKeyboardButton('🙋🙋 𝗜𝗡𝗩𝗜𝗧𝗘 𝗬𝗢𝗨𝗥 𝗙𝗥𝗜𝗘𝗡𝗗𝗦 🙋🙋', url='https://telegram.me/share/url?url=https://t.me/Latest_hindi_hd_Movies_Hub')
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([DONATE_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, update):
    await bot.send_message(
        text="Click the Following Button to Donate Us.",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_message(filters.private & filters.command(["bots"]))
async def bots(bot, update):
    await bot.send_message(
        text="https://t.me/Latest_hindi_hd_Movies_Hub",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_inline_query()
async def answerX(bot, update):

    answer = list()
    answer.append(InlineQueryResultArticle(title="This is My Donation Or Payment Bot", description="You Can Donate Us Using Inline.",
    input_message_content=InputTextMessageContent(message_text="Please donate us any amount you like, to support the services."),
    reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("Dᴏɴᴀᴛᴇ 💳", url="") ] ] ),
    thumb_url="https://telegra.ph/file/330bd070950b8ef775ca9.jpg") )
    try:
        await update.answer(results=answer, cache_time=0)
    except Exception as e:
        print(f"🚸 ERROR : {e}")
    except QueryIdInvalid:
        pass

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "donateme":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "upidata":
        await update.message.edit_text(
            text=DONATE_TEXT.format(update.from_user.mention),
            reply_markup=UPI_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "back":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

Bot.run()
