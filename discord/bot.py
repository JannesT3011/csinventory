from discord.ext import commands
import discord

#async def run():
#    bot = CSInventoryDiscord()
#    try:
#        await bot.start("")
#    except Exception as err:
#        print(err)

class CSInventoryDiscord(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."),
            description="discord bot",
        )
        self.creator = "Bmbus#8446"
        self.github_url = "https://github.com/Bmbus/csinventory"
        #self.db = Database()

        self.load_extension("cogs.dcinventory")
    
    async def on_ready(self):
        print("##########\n"f"{self.user.name}\n"f"{self.user.id}\n""##########")
        print(discord.utils.oauth_url(self.user.id))
    
    async def on_message(self, message):
        if message.guild:
            return
        await self.process_commands(message)

if __name__ == "__main__":
    CSInventoryDiscord().run("")