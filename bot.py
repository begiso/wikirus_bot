import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1943689877:AAHtvGAt0WTYpeYHC2J7b95AGijMvpph-4A'
wikipedia.set_lang('ru')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Добро пожаловать в Википедию.\nНапишите, что вы хотите найти ?")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Соответствий запросу не найдено')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)