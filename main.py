import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)


@client.command()
async def Help(ctx):
	await ctx.send("DISCORD BOT COMMAND =\n coucou **-** Info **-** say **-** clear **-** rero.")

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('DDNet'))
	print("Ready !")

@client.command()
async def coucou(ctx):
	await ctx.send("Coucou !")

@client.command()
async def Info(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Flemme de la faire..."
	await ctx.send(message)

@client.command()
async def say(ctx, *text):
	await ctx.send(" ".join(text))

@client.command()
async def clear(ctx, nb : int):
	messages = await ctx.channel.history(limit = nb + 1).flatten()
	for message in messages:
		await message.delete()

@client.event
async def on_member_join(member):
    role2 = member.guild.get_role(774769580056117289)
    await member.add_roles(role2)

@client.command()
async def rero(ctx, *,role: discord.Role):
 if ctx.author.id == 442317943322312714:
   if role is None:
     await ctx.send('Please write *correct role name*')

   try:
     await role.delete()
     await ctx.send(f'I **yeeted** {role}!')

   except discord.Forbidden:
     await ctx.send('I do not have permission to delete this role')

client.run('Nzc0NzMyNTkwMjE2NzczNjUz.X6cD8w._0elLqTKIeznASXNUc7MxRkARds')
