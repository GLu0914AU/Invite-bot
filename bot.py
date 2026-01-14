"""
Where Winds Meet Guild Auto Invite Bot
A Discord bot that automatically generates and manages guild invites
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID', 0))
INVITE_CHANNEL_ID = int(os.getenv('INVITE_CHANNEL_ID', 0))

# Bot setup with intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """Event handler for when the bot is ready"""
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guild(s)')
    
    # Display guild information
    for guild in bot.guilds:
        print(f'- {guild.name} (id: {guild.id})')


@bot.event
async def on_member_join(member):
    """Event handler for when a new member joins the guild"""
    guild = member.guild
    if guild.id == GUILD_ID:
        channel = guild.get_channel(INVITE_CHANNEL_ID)
        if channel:
            embed = discord.Embed(
                title="Welcome to Where Winds Meet Guild!",
                description=f"Welcome {member.mention}! We're glad to have you here.",
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
            embed.add_field(name="Member Count", value=f"{guild.member_count}", inline=True)
            await channel.send(embed=embed)


@bot.command(name='createinvite', help='Creates a new invite link for the guild')
@commands.has_permissions(manage_guild=True)
async def create_invite(ctx, max_age: int = 0, max_uses: int = 0):
    """
    Creates a new invite link with optional parameters
    
    Args:
        max_age: Time in seconds until the invite expires (0 = never)
        max_uses: Maximum number of uses (0 = unlimited)
    """
    try:
        # Create invite for the channel where command was used
        invite = await ctx.channel.create_invite(
            max_age=max_age,
            max_uses=max_uses,
            reason=f"Invite created by {ctx.author}"
        )
        
        embed = discord.Embed(
            title="🎫 New Invite Created!",
            description=f"Invite link: {invite.url}",
            color=discord.Color.blue()
        )
        
        if max_age > 0:
            embed.add_field(name="Expires in", value=f"{max_age} seconds", inline=True)
        else:
            embed.add_field(name="Expires", value="Never", inline=True)
            
        if max_uses > 0:
            embed.add_field(name="Max uses", value=f"{max_uses}", inline=True)
        else:
            embed.add_field(name="Max uses", value="Unlimited", inline=True)
        
        await ctx.send(embed=embed)
        
    except discord.Forbidden:
        await ctx.send("❌ I don't have permission to create invites in this channel!")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {str(e)}")


@bot.command(name='inviteinfo', help='Shows information about active invites')
@commands.has_permissions(manage_guild=True)
async def invite_info(ctx):
    """Shows all active invites for the guild"""
    try:
        invites = await ctx.guild.invites()
        
        if not invites:
            await ctx.send("No active invites found!")
            return
        
        embed = discord.Embed(
            title=f"📋 Active Invites for {ctx.guild.name}",
            color=discord.Color.purple()
        )
        
        for invite in invites[:10]:  # Limit to 10 invites
            invite_info = f"**Code:** {invite.code}\n"
            invite_info += f"**Uses:** {invite.uses}"
            if invite.max_uses > 0:
                invite_info += f"/{invite.max_uses}"
            invite_info += f"\n**Created by:** {invite.inviter.mention if invite.inviter else 'Unknown'}"
            
            if invite.max_age == 0:
                invite_info += "\n**Expires:** Never"
            else:
                invite_info += f"\n**Expires:** {invite.max_age}s after creation"
            
            embed.add_field(
                name=f"Invite: {invite.url}",
                value=invite_info,
                inline=False
            )
        
        await ctx.send(embed=embed)
        
    except discord.Forbidden:
        await ctx.send("❌ I don't have permission to view invites!")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {str(e)}")


@bot.command(name='autoinvite', help='Automatically creates and posts a permanent invite link')
@commands.has_permissions(manage_guild=True)
async def auto_invite(ctx):
    """Creates a permanent invite link and posts it"""
    try:
        # Create a permanent invite
        invite = await ctx.channel.create_invite(
            max_age=0,
            max_uses=0,
            reason=f"Auto invite by {ctx.author}"
        )
        
        embed = discord.Embed(
            title="🌟 Where Winds Meet Guild - Permanent Invite",
            description="Join our guild and adventure together!",
            color=discord.Color.gold()
        )
        embed.add_field(name="Invite Link", value=f"{invite.url}", inline=False)
        embed.add_field(name="Features", value="✨ Active community\n🎮 Guild events\n🤝 Helpful members", inline=False)
        embed.set_footer(text="This invite never expires and has unlimited uses!")
        
        await ctx.send(embed=embed)
        
    except discord.Forbidden:
        await ctx.send("❌ I don't have permission to create invites!")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {str(e)}")


@bot.command(name='help_wwm', help='Shows help information for Where Winds Meet bot')
async def help_wwm(ctx):
    """Displays help information for the bot"""
    embed = discord.Embed(
        title="🎮 Where Winds Meet Guild Bot - Help",
        description="Auto invite bot for managing guild invites",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="!createinvite [max_age] [max_uses]",
        value="Creates a new invite link\nExample: `!createinvite 3600 10` (expires in 1 hour, 10 uses)",
        inline=False
    )
    
    embed.add_field(
        name="!inviteinfo",
        value="Shows all active invites for the guild",
        inline=False
    )
    
    embed.add_field(
        name="!autoinvite",
        value="Creates a permanent invite link with unlimited uses",
        inline=False
    )
    
    embed.add_field(
        name="!help_wwm",
        value="Shows this help message",
        inline=False
    )
    
    embed.set_footer(text="Most commands require 'Manage Server' permission")
    
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    """Global error handler for commands"""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command!")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Missing required argument: {error.param}")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Invalid argument provided!")
    else:
        print(f"Error: {error}")
        await ctx.send("❌ An error occurred while executing the command.")


def main():
    """Main function to run the bot"""
    if not TOKEN:
        print("Error: DISCORD_TOKEN not found in environment variables!")
        print("Please create a .env file with your bot token.")
        return
    
    try:
        bot.run(TOKEN)
    except discord.LoginFailure:
        print("Error: Invalid Discord token!")
    except Exception as e:
        print(f"Error running bot: {e}")


if __name__ == "__main__":
    main()
