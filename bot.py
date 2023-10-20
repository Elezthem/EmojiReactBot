import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot is ready as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '👋':
        await message.channel.send('👋 Hello!')

# Insert your bot token here
client.run('YOUR_BOT_TOKEN')
