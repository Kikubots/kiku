"""
syntax - .shout message

"""

from Lion import CMD_HELP
from Lion.utils import admin_cmd


@kiku.on(admin_cmd(pattern=r"shout", outgoing=True))
@kiku.on(sudo_cmd(pattern=r"shout", allow_sudo=True))
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(" ".join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await eor(args, "`" + msg + "`")


CMD_HELP.update({"shout": ".shout <message>\nUse - Shout the message word-by-word."})
