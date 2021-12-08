# -*- coding: utf-8 -*-

from config import *
import re
from bs4 import BeautifulSoup
from lxml import html
import os

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  update_patch.py importado.{/cyan}'))


@bot.message_handler(commands=['update_patch'])
def update_patch_auto(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        invisible_character = "⁣"
        for x in [x for x in os.listdir('extra_data') if x.startswith('patch')]:
            # First we root of the file
            x = "extra_data/{}".format(x)
            # If patch is empty, continue
            if not [y for y in open(x)]:
                continue
            # Get last line from each patch
            last_line = [y.strip() for y in open(x)][-1]
            # Extract URL
            patch_url_base = last_line.split()[-1]
            # Extract patch number
            patch_id_url_base = re.search(r'[0-9]+-[0-9]+', patch_url_base).group(0)

            # Calculate new one
            # patch_id_new = str(int(patch_id_base) + 1)
            # Generate new URL
            # patch_url_new = patch_url_base.replace(patch_id_base, patch_id_new)

            # Extract patch number from last line
            patch_id_base = re.search(r'[0-9]+\.[0-9]+', last_line).group(0)
            # Generate new patch number
            patch_id_new = patch_id_base.split('.')
            patch_id_new[-1] = str(int(patch_id_new[-1]) + 1)
            patch_id_url_new = "-".join(patch_id_new)
            patch_url_new = patch_url_base.replace(patch_id_url_base, patch_id_url_new)
            patch_id_new = ".".join(patch_id_new)
            # Update last line URL
            new_last_line = last_line.replace(patch_url_base, patch_url_new).replace(patch_id_base, patch_id_new)

            r = requests.get(patch_url_new)
            r.encoding = r.apparent_encoding
            if r.status_code != 200:
                bot.send_message(cid, "Error parseando la siguiente URL: {}".format(patch_url_new))
                continue

            soup = BeautifulSoup(r.text, 'html.parser')
            tree = html.fromstring(r.content)
            highlights = tree.xpath('//img[contains(@src, "Infographic") or contains(@src, "Patch-")]/@src')
            if highlights:
                highlights = highlights[0]
            # youtube_link = ""
            # try:
            #     for y in soup.findAll('iframe'):
            #         if 'youtu' in y.attrs['src']:
            #             youtube_link = y.attrs['src']
            #             break
            # except:
            #     bot.send_message(cid, "Error obteniendo URL de youtube")
                new_patch_notes = "[{}]({}){}\n\n{}".format(
                    invisible_character, 
                    highlights,
                    re.sub(r'<a href="(.*)">(.*)</a>', r'[\2](\1)', ''.join(list(filter(None, [x.strip().replace('<br/>', '\n').replace('<a',' <a') for x in soup.find('blockquote').prettify().split('\n') if not '<bl' in x and not '<e' in x and not '</e' in x and not '</bl' in x])))), 
                    new_last_line)
            else:
                new_patch_notes = "{}\n\n{}".format(
                    re.sub(r'<a href="(.*)">(.*)</a>', r'[\2](\1)', ''.join(list(filter(None, [x.strip().replace('<br/>', '\n').replace('<a',' <a') for x in soup.find('blockquote').prettify().split('\n') if not '<bl' in x and not '<e' in x and not '</e' in x and not '</bl' in x])))), 
                    new_last_line)
            with open(x, 'w', encoding='utf-8') as f:
                f.write(new_patch_notes)
        bot.send_message(cid, "Done :)")