# -*- coding: utf-8 -*-

from config import *
from io import StringIO


print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  exec.py importado.{/cyan}'))


@bot.message_handler(commands=['exec'])
def command_exec(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        botan.track(
            botan_token,
            cid,
            to_json(m),
            "/exec"
        )
    except:
        pass
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) == 1:
            bot.send_message(
                cid,
                "Uso: /exec _<code>_ - Ejecuta el siguiente bloque de código.",
                parse_mode="Markdown")
            return
        cout = StringIO()
        sys.stdout = cout
        cerr = StringIO()
        sys.stderr = cerr
        code = ' '.join(m.text.split()[1:])
        try:
            exec(code)
        except Exception as e:
            bot.send_message(cid, send_exception(e), parse_mode="Markdown")
        else:
            if cout.getvalue():
                bot.send_message(cid, str(cout.getvalue()))
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
