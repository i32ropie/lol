# -*- coding: utf-8 -*-

from config import *
import re
from bs4 import BeautifulSoup

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_patch.py importado.{/cyan}'))


@bot.message_handler(commands=['update_patch'])
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp(m.text.lstrip('/').split(' ')[0].split('@')[0].lower())
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        invisible_character = "⁣"
        for x in [x for x os.listdir('extra_data') if x.startswith('patch')]:
            # If patch is empty, continue
            if not [y for y in open(x)]:
                continue
            # Get last line from each patch
            last_line = [y.strip() for y in open(x)][-1]
            # Extract URL
            patch_url_base = last_line.split()[-1]
            # Extract patch number
            patch_id_base = re.search('[0-9]+', patch_url_base).group(0)
            # Calculate new one
            patch_id_new = str(int(patch_id_base) + 1)
            # Generate new URL
            patch_url_new = patch_url_base.replace(patch_id_base, patch_id_new)

            # Extract patch number from last line
            patch_id_base = re.search('[0-9]+\.[0-9]+', last_line).group(0)
            # Generate new patch number
            patch_id_new = patch_id_base.split('.')
            patch_id_new[-1] = str(int(patch_id_new[-1]) + 1)
            patch_id_new = ".".join(patch_id_new)
            # Update last line URL
            new_last_line = last_line.replace(patch_url_base, patch_url_new).replace(patch_id_base, patch_id_new)

            r = requests.get(patch_url_new)
            if r.status_code != 200:
                return bot.send_message(uid, "Error parseando la siguiente URL: {}".format(patch_url_new))

            soup = BeautifulSoup(r.text, 'html.parser')
            youtube_link = ""
            try:
                for y in soup.findAll('iframe'):
                    if 'youtu' in y.attrs['src']:
                        youtube_link = y.attrs['src']
                        break
            except:
                bot.send_message(uid, "Error obteniendo URL de youtube")
            if youtube_link:
                new_patch_notes = "[{}]({}){}\n\n{}".format(invisible_character, youtube_link, '\n\n'.join(list(filter(None, [x.strip() for x in soup.find('blockquote').prettify().split('\n') if not '<' in x]))), new_last_line)
            else:
                new_patch_notes = "{}\n\n{}".format('\n\n'.join(list(filter(None, [x.strip() for x in soup.find('blockquote').prettify().split('\n') if not '<' in x]))), new_last_line)
            with open(x, 'w') as f:
                f.write(new_patch_notes)