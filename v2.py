# v2.py - Admin-only Discord VPS creator scaffold
import os
import asyncio
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')
ADMIN_IDS = set(int(i.strip()) for i in os.getenv('ADMIN_IDS', '').split(',') if i.strip())

intents = discord.Intents.default()
intents.message_content = False
bot = commands.Bot(command_prefix='!', intents=intents)

# Utility: check admin/whitelist
async def is_admin(interaction: discord.Interaction) -> bool:
    # Bot owner
    app = await bot.application_info()
    if interaction.user.id == app.owner.id:
        return True
    # explicit whitelist
    if interaction.user.id in ADMIN_IDS:
        return True
    # guild administrator
    if isinstance(interaction.user, discord.Member):
        if interaction.user.guild_permissions.administrator:
            return True
    return False

# Helper to wrap admin enforcement
def admin_only(func):
    async def wrapper(interaction: discord.Interaction, *args, **kwargs):
        if not await is_admin(interaction):
            return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
        return await func(interaction, *args, **kwargs)
    return wrapper

# Register commands
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Syncing commands...")
    guild = None
    if GUILD_ID:
        try:
            guild = discord.Object(id=int(GUILD_ID))
        except Exception:
            guild = None
    await bot.tree.sync(guild=guild)
    print("Commands synced.")

# --- Command stubs ---

@bot.tree.command(name="create", description="Create a VPS (admin-only)")
async def create(interaction: discord.Interaction):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message("Creating VPS... (stub)")
    # TODO: implement creation logic

@bot.tree.command(name="node", description="Manage node (admin-only)")
async def node(interaction: discord.Interaction, action: str = "status"):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message(f"Node action `{action}` received. (stub)")

@bot.tree.command(name="deploy", description="Deploy a VPS (admin-only)")
async def deploy(interaction: discord.Interaction, image: str = "ubuntu-22.04"):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message(f"Deploying image `{image}`... (stub)")
    # TODO: call provisioning function

@bot.tree.command(name="sendvps", description="Send VPS details to user (admin-only)")
async def sendvps(interaction: discord.Interaction, user: discord.User):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    # TODO: fetch VPS details and DM
    await interaction.response.send_message(f"Sent VPS details to {user.mention} (stub)")

@bot.tree.command(name="regen-ssh", description="Regenerate SSH for VPS (admin-only)")
async def regen_ssh(interaction: discord.Interaction, vps_id: str):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message(f"Regenerating SSH for `{vps_id}`... (stub)")

@bot.tree.command(name="stop", description="Stop a VPS (admin-only)")
async def stop(interaction: discord.Interaction, vps_id: str):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message(f"Stopping `{vps_id}`... (stub)")

@bot.tree.command(name="start", description="Start a VPS (admin-only)")
async def start(interaction: discord.Interaction, vps_id: str):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message(f"Starting `{vps_id}`... (stub)")

@bot.tree.command(name="restart", description="Restart a VPS (admin-only)")
async def restart(interaction: discord.Interaction, vps_id: str):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message(f"Restarting `{vps_id}`... (stub)")

@bot.tree.command(name="resources", description="Show VPS resources (admin-only)")
async def resources(interaction: discord.Interaction, vps_id: str):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    # TODO: query real metrics
    await interaction.response.send_message(f"Resources for `{vps_id}`: CPU 1, RAM 512MB, Disk 10GB (stub)")

@bot.tree.command(name="sharedipv4", description="Attach shared IPv4 to VPS (admin-only)")
async def sharedipv4(interaction: discord.Interaction, vps_id: str):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message(f"Assigning shared IPv4 to `{vps_id}`... (stub)")

@bot.tree.command(name="tunnel", description="Open tunnel to VPS (admin-only)")
async def tunnel(interaction: discord.Interaction, vps_id: str):
    if not await is_admin(interaction):
        return await interaction.response.send_message("⛔ Admins only.", ephemeral=True)
    await interaction.response.send_message(f"Creating tunnel for `{vps_id}`... (stub)")

# Simple in-memory store for demo (replace with DB in production)
VPS_STORE = {}

if __name__ == '__main__':
    if not TOKEN:
        raise SystemExit("DISCORD_TOKEN is not set in environment")
    bot.run(TOKEN)
