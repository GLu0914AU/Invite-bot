# Where Winds Meet Guild Auto Invite Bot

An automated Discord bot for managing guild invites for "Where Winds Meet" communities.

## Features

- 🎫 **Automatic Invite Generation**: Create permanent or temporary invite links
- 👋 **Welcome Messages**: Automatically greet new members
- 📊 **Invite Management**: View and track all active invites
- 🎮 **Guild-Specific**: Tailored for Where Winds Meet communities

## Commands

| Command | Description | Permissions Required |
|---------|-------------|---------------------|
| `!createinvite [max_age] [max_uses]` | Creates a new invite link with optional expiration and usage limits | Manage Server |
| `!inviteinfo` | Shows all active invites for the guild | Manage Server |
| `!autoinvite` | Creates a permanent invite link with unlimited uses | Manage Server |
| `!help_wwm` | Shows help information for all bot commands | None |

### Command Examples

```bash
# Create a permanent invite (never expires, unlimited uses)
!autoinvite

# Create an invite that expires in 1 hour (3600 seconds)
!createinvite 3600 0

# Create an invite with 10 maximum uses
!createinvite 0 10

# Create an invite that expires in 24 hours with 50 max uses
!createinvite 86400 50

# View all active invites
!inviteinfo
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- A Discord account
- Discord Developer Portal access

### Step 1: Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section
4. Click "Add Bot"
5. Under "Privileged Gateway Intents", enable:
   - Presence Intent
   - Server Members Intent
   - Message Content Intent
6. Copy the bot token (you'll need this later)

### Step 2: Invite the Bot to Your Server

1. Go to the "OAuth2" > "URL Generator" section
2. Select scopes: `bot`
3. Select bot permissions:
   - Manage Channels
   - Create Instant Invite
   - Send Messages
   - Embed Links
   - Read Message History
   - Use External Emojis
4. Copy the generated URL and open it in your browser
5. Select your server and authorize the bot

### Step 3: Install Dependencies

```bash
# Clone the repository
git clone https://github.com/GLu0914AU/Invite-bot.git
cd Invite-bot

# Install required packages
pip install -r requirements.txt
```

### Step 4: Configure the Bot

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your configuration:
   ```env
   DISCORD_TOKEN=your_bot_token_here
   GUILD_ID=your_server_id_here
   INVITE_CHANNEL_ID=your_channel_id_here
   ```

   To get IDs (Developer Mode must be enabled in Discord settings):
   - **Guild ID**: Right-click your server name → Copy ID
   - **Channel ID**: Right-click a channel → Copy ID

### Step 5: Run the Bot

```bash
python bot.py
```

You should see output like:
```
YourBotName#1234 has connected to Discord!
Bot is in 1 guild(s)
- Your Server Name (id: 123456789)
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DISCORD_TOKEN` | Your Discord bot token | Yes |
| `GUILD_ID` | The ID of your Discord server | Yes |
| `INVITE_CHANNEL_ID` | Channel ID for welcome messages | Yes |

## Running as a Service

### Linux (systemd)

Create a service file `/etc/systemd/system/wwm-invite-bot.service`:

```ini
[Unit]
Description=Where Winds Meet Invite Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/Invite-bot
ExecStart=/usr/bin/python3 /path/to/Invite-bot/bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl enable wwm-invite-bot
sudo systemctl start wwm-invite-bot
```

### Using Docker (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY bot.py .
CMD ["python", "bot.py"]
```

Build and run:
```bash
docker build -t wwm-invite-bot .
docker run -d --env-file .env wwm-invite-bot
```

## Troubleshooting

### Bot doesn't respond to commands

- Check that the bot has "Message Content Intent" enabled in Discord Developer Portal
- Ensure the bot has proper permissions in your server
- Verify the bot is online (check Discord server member list)

### Permission errors

- Make sure the bot role has "Manage Server" or "Administrator" permissions
- Check channel-specific permissions for the bot

### Bot crashes on startup

- Verify your `.env` file has valid values
- Check that `DISCORD_TOKEN` is correct
- Ensure Python dependencies are installed: `pip install -r requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is open source and available under the MIT License.

## Support

For questions or issues related to "Where Winds Meet", please join our Discord community or open an issue on GitHub.
