import nextcord
from nextcord.ext import commands
from config import settings


class UtilityCommandsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(
        name="ping",
        description="Check the bot's status and latency.",
        guild_ids=[settings.discord.guild_id],
    )
    async def slash_ping(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(
            "Pong! Current Discord API latency is "
            + str(round(interaction.client.latency * 1000))
            + " milliseconds.",
            ephemeral=True,
        )


def setup(bot):
    bot.add_cog(UtilityCommandsCog(bot))
