# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  beta.py importado.{/cyan}'))


@bot.message_handler(commands=['beta'])
def command_beta(m):
    cid = m.chat.id
    uid = m.from_user.id
    # try:
    #     botan.track(
    #         botan_token,
    #         cid,
    #         to_json(m),
    #         "/beta"
    #     )
    # except:
    #     pass
    try:
        send_udp('beta')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        if len(m.text.split()) != 3:
            bot.send_message(cid, responses["beta"]["error"])
        else:
            action = m.text.split()[1]
            ID = m.text.split()[2]
            if action not in ['add', 'del'] or not isint(ID):
                bot.send_message(cid, responses["beta"]["error"])
            else:
                if action == "add":
                    if not is_user(ID):
                        bot.send_message(
                            cid, responses["beta"]["add"]["error"]["not_user"] %
                            (ID), parse_mode="Markdown")
                    elif is_beta(int(ID)):
                        bot.send_message(
                            cid, responses["beta"]["add"]["error"]["already_beta"] %
                            (ID), parse_mode="Markdown")
                    else:
                        bot.send_message(
                            cid, responses["beta"]["add"]["success"] %
                            (ID))
                        extra["beta"].append(int(ID))
                        with open("extra_data/extra.json", "w") as f:
                            json.dump(extra, f)
                elif action == "del":
                    if not is_beta(int(ID)):
                        bot.send_message(
                            cid, responses["beta"]["del"]["error"] %
                            (ID), parse_mode="Markdown")
                    else:
                        bot.send_message(
                            cid, responses["beta"]["del"]["success"] %
                            (ID))
                        extra["beta"].remove(int(ID))
                        with open("extra_data/extra.json", "w") as f:
                            json.dump(extra, f)
