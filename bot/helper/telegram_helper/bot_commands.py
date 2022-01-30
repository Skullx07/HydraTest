from bot import BOT_NO

class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{BOT_NO}'
        self.MirrorCommand = f'mirror{BOT_NO}'
        self.UnzipMirrorCommand = f'extract{BOT_NO}'
        self.TarMirrorCommand = f'tar{BOT_NO}'
        self.CancelMirror = f'cancel{BOT_NO}'
        self.CancelAllCommand = f'cancelall{BOT_NO}'
        self.ListCommand = 'look'
        self.SpeedCommand = 'sptest'
        self.CountCommand = f'count{BOT_NO}'
        self.StatusCommand = f'status{BOT_NO}'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'unauth'
        self.AddSudoCommand = 'addsudo'
        self.RmSudoCommand = 'rmsudo'
        self.PingCommand = 'ping'
        self.RestartCommand = f'res{BOT_NO}'
        self.StatsCommand = f'stats{BOT_NO}'
        self.HelpCommand = f'help{BOT_NO}'
        self.LogCommand = f'log{BOT_NO}'
        self.CloneCommand = f"clone{BOT_NO}"
        self.WatchCommand = f'watch{BOT_NO}'
        self.TarWatchCommand = f'tarwatch{BOT_NO}'
        self.deleteCommand = f'del{BOT_NO}'

BotCommands = _BotCommands()
