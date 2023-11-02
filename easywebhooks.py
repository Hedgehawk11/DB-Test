from discord_webhook import DiscordWebhook

def send(content):
    webhook = DiscordWebhook('https://discord.com/api/webhooks/1152409919698501712/8vwW6ha4Z35-lIVdlvXcPDV8cGoesSt9rgo07kCxPOyHDkwLcZClquQNxtu2pJ9TQDRT', content=content)
    webhook.execute()