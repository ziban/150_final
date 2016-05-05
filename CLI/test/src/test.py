from pytg import Telegram
tg = Telegram(
    telegram="../../tg/bin/telegram-cli",
    pubkey_file="../../tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender

