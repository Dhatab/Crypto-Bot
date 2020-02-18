import logging
from uuid import uuid4
from coinAPI import coinSearch
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown


#Command handlers
#Sends message when /start is used
def start(update, context):
    update.message.reply_text('Hello!')

#Sends message when /search is used
def help(update, context):
    update.message.reply_text('Help!')

#Sends message when @botname is used
def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query

    if not query:
        results = [
            InlineQueryResultArticle(
                id=uuid4(),
                title="Caps",
                input_message_content=InputTextMessageContent(
                    query.upper())),
            InlineQueryResultArticle(
                id=uuid4(),
                title="Bold",
                input_message_content=InputTextMessageContent(
                    "*{}*".format(escape_markdown(query)),
                    parse_mode=ParseMode.MARKDOWN)),
            InlineQueryResultArticle(
                id=uuid4(),
                title="Italic",
                input_message_content=InputTextMessageContent(
                    "_{}_".format(escape_markdown(query)),
                    parse_mode=ParseMode.MARKDOWN))]
    else:
        _coinSearch = coinSearch()
        _coinSearch.main(query.lower())
        results =[
            InlineQueryResultArticle(
                id = uuid4(),
                title = _coinSearch.name,
                input_message_content = InputTextMessageContent("{} is at $: {}".format(_coinSearch.name, _coinSearch.price_usd) 
                )
            ),

            InlineQueryResultArticle(
                id = uuid4(),
                title = _coinSearch.symbol,
                input_message_content = InputTextMessageContent("{} is at $: {}".format(_coinSearch.name, _coinSearch.price_usd) 
                )
            ),

            InlineQueryResultArticle(
                id = uuid4(),
                title = _coinSearch.rank,
                input_message_content = InputTextMessageContent("{} is at $: {}".format(_coinSearch.name, _coinSearch.price_usd) 
                )
            ),

            InlineQueryResultArticle(
                id = uuid4(),
                title = _coinSearch.price_usd,
                input_message_content = InputTextMessageContent("{} is at $: {}".format(_coinSearch.name, _coinSearch.price_usd) 
                )
            ),
        ]
        
    
    update.inline_query.answer(results)

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater("BOT TOKEN HERE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # # log all errors
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()