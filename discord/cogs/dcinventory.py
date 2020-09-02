from discord.ext import commands
from discord import Embed
import discord
import requests
from csinventorypy import CSInventory

class dcInventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #self.url = "http://localhost:8080/api/inventory"

    @commands.cooldown(1, 60.0, commands.BucketType.user)
    @commands.command(name="inventory")
    async def _inventory(self, ctx, *, steamid):
        data = CSInventory(steamid).get_inventory()
        try:
            await ctx.send(", ".join(data))
        except:
            await ctx.send(f"http://localhost:3000/{steamid}")

def setup(bot):
    bot.add_cog(dcInventory(bot))