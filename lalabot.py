from glob import glob
from nextcord.ext import commands
from pathlib import Path
from config import settings
from click import echo, style
import nextcord

description = """A bot to help FFXIV Free Companies manage various things."""

intents = nextcord.Intents.all()

bot = commands.Bot(
    command_prefix=settings.discord.bot.command_prefix,
    description=description,
    intents=intents,
)


@bot.event
async def on_ready():
    echo(
        style("[ OK ]\n", fg="bright_green")
        + "Logged in as {} (ID: {}).".format(
            style(bot.user, fg="bright_cyan"),
            style(bot.user.id, fg="cyan"),
        ),
    )

    for cog_file in glob("./cogs/*.py"):
        cog_name = Path(cog_file).stem
        echo(
            style("Loading ", fg="bright_yellow")
            + style(cog_name, fg="bright_cyan")
            + style(" extension... ", fg="bright_yellow"),
            nl=False,
        )

        try:
            bot.load_extension(f"cogs.{cog_name}")
        except commands.errors.ExtensionFailed as exc:
            echo(style("[FAIL]", fg="bright_red"))
            echo(style("Exception data: ", fg="yellow") + str(exc))
        else:
            echo(style("[ OK ]", fg="bright_green"))

    echo(style("Done loading extensions.", fg="bright_yellow"))


echo(
    style("Attempting to connect to Discord API... ", fg="bright_yellow"),
    nl=False,
)

bot.run(settings.discord.bot.api_token)
