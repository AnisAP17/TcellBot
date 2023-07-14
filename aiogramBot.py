from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = "5870105739:AAEkQVYMG6AINTxmagdROkvfjsnaWT2J56U"
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_bot(message: types.Message):
    await message.answer(message.text)

print("new branch")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)