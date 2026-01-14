# Quick Start Guide

Get your Where Winds Meet Guild Invite Bot up and running in 5 minutes!

## Prerequisites

- Python 3.8+ installed
- A Discord account with a server
- Basic knowledge of Discord settings

## Step-by-Step Setup

### 1. Create Your Bot (2 minutes)

1. Visit https://discord.com/developers/applications
2. Click **"New Application"**
3. Name it (e.g., "WWM Invite Bot")
4. Go to **"Bot"** section → Click **"Add Bot"**
5. Under **"Privileged Gateway Intents"**, enable:
   - ✅ Presence Intent
   - ✅ Server Members Intent  
   - ✅ Message Content Intent
6. Click **"Reset Token"** and copy your token (save it securely!)

### 2. Invite Bot to Server (1 minute)

1. Go to **"OAuth2"** → **"URL Generator"**
2. Select **Scopes**: `bot`
3. Select **Bot Permissions**:
   - ✅ Manage Channels
   - ✅ Create Instant Invite
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Read Message History
4. Copy the generated URL, paste in browser
5. Select your server and **Authorize**

### 3. Configure the Bot (1 minute)

```bash
# In your terminal/command prompt
cd Invite-bot
cp .env.example .env
```

Edit `.env` file with your favorite text editor:

```env
DISCORD_TOKEN=paste_your_bot_token_here
GUILD_ID=your_server_id
INVITE_CHANNEL_ID=your_channel_id
```

**How to get IDs:**
- Enable Developer Mode: Discord Settings → Advanced → Developer Mode
- Server ID: Right-click server name → Copy ID
- Channel ID: Right-click any channel → Copy ID

### 4. Install & Run (1 minute)

```bash
# Install dependencies
pip install -r requirements.txt

# Start the bot
python bot.py
```

Or use the start script:
```bash
chmod +x start.sh
./start.sh
```

## Test Your Bot

In your Discord server, try these commands:

```
!help_wwm           # See all commands
!autoinvite         # Create a permanent invite link
!createinvite 3600  # Create invite that expires in 1 hour
!inviteinfo         # View all active invites
```

## Troubleshooting

**Bot is offline?**
- Check your token in `.env`
- Make sure the bot is invited to your server

**Commands not working?**
- Verify Message Content Intent is enabled
- Check bot has proper permissions

**Need help?**
- See full README.md for detailed documentation
- Check that all IDs in `.env` are correct

## Next Steps

- Customize messages in `config.py`
- Set up as a service for 24/7 running (see README.md)
- Configure feature flags in `config.py`

Enjoy your auto invite bot! 🎮
