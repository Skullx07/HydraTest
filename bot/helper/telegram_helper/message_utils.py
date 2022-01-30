from telegram import InlineKeyboardMarkup
from telegram.message import Message
from telegram.update import Update
from telegram import Bot
import time
import psutil
from bot import AUTO_DELETE_MESSAGE_DURATION, LOGGER, bot, \
    status_reply_dict, status_reply_dict_lock, download_dict, download_dict_lock, UPLOAD_LOG, UPLOAD_UNAME
from bot.helper.ext_utils.bot_utils import get_readable_message, get_readable_file_size, MirrorStatus
from telegram.error import TimedOut, BadRequest
from bot.helper.ext_utils.bot_utils import BotCommands

def sendMessage(text: str, bot, update: Update):
    try:
        return bot.send_message(update.message.chat_id,
                            reply_to_message_id=update.message.message_id,
                            text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def sendMarkup(text: str, bot, update: Update, reply_markup: InlineKeyboardMarkup):
    try:
        return bot.send_message(update.message.chat_id,
                             reply_to_message_id=update.message.message_id,
                             text=text, reply_markup=reply_markup, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))
        
        
def sendLog(text: str, bot, update: Update):
    try:
        return bot.send_message(f"{UPLOAD_LOG}",
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))
        
        
        def sendPrivate(text: str, bot, update: Update):
    bot_d = bot.get_me()
    b_uname = bot_d.username

    try:
        return bot.send_message(update.message.from_user.id,
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))
        if "Forbidden" in str(e):
            uname = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}</a>'
            botstart = f'<a href="http://t.me/{b_uname}?start=start">Start Me</a>'
            sendMessage(f"<b>Hey</b> {uname},\n\n<b>You didn't Started Me in Private Chat!</b>\n\n<i>Please {botstart} in PM(Private Chat) and Don't Miss Future Uploads. From Now On, I'll Give Links in Private Chat Only.</i>\n<i>For Now, Get Your Uploads From @{UPLOAD_UNAME}</i>", bot, update)
            return


def sendPvt(text: str, bot, update: Update):
    bot_d = bot.get_me()
    b_uname = bot_d.username

    try:
        return bot.send_message(update.message.from_user.id,
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))
        if "Forbidden" in str(e):
            uname = f'<a href="tg://user?id={update.message.from_user.id}">{update.message.from_user.first_name}</a>'
            sendMessage(f"<b>Hey</b> {uname}, <b>You didn't Started Me in Private Chat!</b>", bot, update)
            return


def sendLog(text: str, bot, update: Update):
    try:
        return bot.send_message(f"{UPLOAD_LOG}",
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def sendPrivate(text: str, bot, update: Update):
    bot_d = bot.get_me()
    b_uname = bot_d.username

    try:
        return bot.send_message(update.message.from_user.id,
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def sendLog(text: str, bot, update: Update):
    try:
        return bot.send_message(f"{UPLOAD_LOG}",
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def sendPrivate(text: str, bot, update: Update):
    bot_d = bot.get_me()
    b_uname = bot_d.username

    try:
        return bot.send_message(update.message.from_user.id,
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def sendLog(text: str, bot, update: Update):
    try:
        return bot.send_message(f"{UPLOAD_LOG}",
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def sendPrivate(text: str, bot, update: Update):
    bot_d = bot.get_me()
    b_uname = bot_d.username

    try:
        return bot.send_message(update.message.from_user.id,
                             reply_to_message_id=update.message.message_id,
                             text=text, disable_web_page_preview=True, allow_sending_without_reply=True, parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def editMessage(text: str, message: Message, reply_markup=None):
    try:
        bot.edit_message_text(text=text, message_id=message.message_id,
                              chat_id=message.chat.id,reply_markup=reply_markup,
                              parse_mode='HTMl')
    except Exception as e:
        LOGGER.error(str(e))


def deleteMessage(bot, message: Message):
    try:
        bot.delete_message(chat_id=message.chat.id,
                           message_id=message.message_id)
    except Exception as e:
        LOGGER.error(str(e))


def sendLogFile(bot, update: Update):
    with open('log.txt', 'rb') as f:
        bot.send_document(document=f, filename=f.name,
                          reply_to_message_id=update.message.message_id,
                          chat_id=update.message.chat_id)


def auto_delete_message(bot, cmd_message: Message, bot_message: Message):
    if AUTO_DELETE_MESSAGE_DURATION != -1:
        time.sleep(AUTO_DELETE_MESSAGE_DURATION)
        try:
            # Skip if None is passed meaning we don't want to delete bot xor cmd message
            deleteMessage(bot, cmd_message)
            deleteMessage(bot, bot_message)
        except AttributeError:
            pass


def delete_all_messages():
    with status_reply_dict_lock:
        for message in list(status_reply_dict.values()):
            try:
                deleteMessage(bot, message)
                del status_reply_dict[message.chat.id]
            except Exception as e:
                LOGGER.error(str(e))


def update_all_messages():
    msg = get_readable_message()
    msg += f"<b>🖥️CPU:</b> {psutil.cpu_percent()}%" \
           f" <b>📀DISK:</b> {psutil.disk_usage('/').percent}%" \
           f" <b>📝RAM:</b> {psutil.virtual_memory().percent}%"
    with download_dict_lock:
        dlspeed_bytes = 0
        uldl_bytes = 0
        for download in list(download_dict.values()):
            speedy = download.speed()
            if download.status() == MirrorStatus.STATUS_DOWNLOADING:
                if 'KiB/s' in speedy:
                    dlspeed_bytes += float(speedy.split('K')[0]) * 1024
                elif 'MiB/s' in speedy:
                    dlspeed_bytes += float(speedy.split('M')[0]) * 1048576 
            if download.status() == MirrorStatus.STATUS_UPLOADING:
                if 'KB/s' in speedy:
            	    uldl_bytes += float(speedy.split('K')[0]) * 1024
                elif 'MB/s' in speedy:
                    uldl_bytes += float(speedy.split('M')[0]) * 1048576
        dlspeed = get_readable_file_size(dlspeed_bytes)
        ulspeed = get_readable_file_size(uldl_bytes)
        msg += f"\n<b>DOWN: </b>{dlspeed}ps ⏬| <b>UP: </b>{ulspeed}ps ⏫\n"
    with status_reply_dict_lock:
        for chat_id in list(status_reply_dict.keys()):
            if status_reply_dict[chat_id] and msg != status_reply_dict[chat_id].text:
                if len(msg) == 0:
                    msg = "Starting DL"
                try:
                    editMessage(msg, status_reply_dict[chat_id])
                except Exception as e:
                    LOGGER.error(str(e))
                status_reply_dict[chat_id].text = msg


def sendStatusMessage(msg, bot):
    progress = get_readable_message()
    progress += f"<b>💻CPU:</b> {psutil.cpu_percent()}%" \
           f" <b>💽DISK:</b> {psutil.disk_usage('/').percent}%" \
           f" <b>📝RAM:</b> {psutil.virtual_memory().percent}%"
    with download_dict_lock:
        dlspeed_bytes = 0
        uldl_bytes = 0
        for download in list(download_dict.values()):
            speedy = download.speed()
            if download.status() == MirrorStatus.STATUS_DOWNLOADING:
                if 'KiB/s' in speedy:
                    dlspeed_bytes += float(speedy.split('K')[0]) * 1024
                elif 'MiB/s' in speedy:
                    dlspeed_bytes += float(speedy.split('M')[0]) * 1048576 
            if download.status() == MirrorStatus.STATUS_UPLOADING:
                if 'KB/s' in speedy:
            	    uldl_bytes += float(speedy.split('K')[0]) * 1024
                elif 'MB/s' in speedy:
                    uldl_bytes += float(speedy.split('M')[0]) * 1048576
        dlspeed = get_readable_file_size(dlspeed_bytes)
        ulspeed = get_readable_file_size(uldl_bytes)
        progress += f"\n<b>DOWN: </b>{dlspeed}ps 🔻| <b>UP: </b>{ulspeed}ps 🔺\n"
    with status_reply_dict_lock:
        if msg.message.chat.id in list(status_reply_dict.keys()):
            try:
                message = status_reply_dict[msg.message.chat.id]
                deleteMessage(bot, message)
                del status_reply_dict[msg.message.chat.id]
            except Exception as e:
                LOGGER.error(str(e))
                del status_reply_dict[msg.message.chat.id]
                pass
        if len(progress) == 0:
            progress = "Starting DL"
        message = sendMessage(progress, bot, msg)
        status_reply_dict[msg.message.chat.id] = message

def sendAddedMessage(update: Update, is_watch_command=False):
    if is_watch_command:
        update.effective_message.reply_html(
            f"{update.effective_user.mention_html()}, <b>Your Requested YT-DL Link Has Been Added To</b> /{BotCommands.StatusCommand}"
        )
    else:
        update.effective_message.reply_html(
            f"{update.effective_user.mention_html()}, <b>Your Requested Task Has Been Added To</b> /{BotCommands.StatusCommand}"
        )
