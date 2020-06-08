# -*- coding: utf-8 -*-
import tweepy, re, time, json, os
from keys import * #import ACCESS_TOKENs and API_KEYs
from collections import Counter

keywords = ['BlackLivesMatter','#BlackLivesMatter']
counter_dict = Counter()
# In case of some error(like no network connection 🙄 ) Counter dict can be set from last line on data.txt
#counter_dict = Counter({"✊🏿": 813, "🤢": 33, "👏🏿": 24, "🤷🏽‍♀️": 6, "☕": 5, "‼": 307, "📢": 13, "🤯": 23, "😳": 38, "😕": 14, "📹": 26, "😒": 31, "😤": 30, "💔": 229, "💞": 24, "👏": 169, "❤": 1063, "✊": 203, "✊🏻": 292, "✊🏼": 399, "✊🏽": 812, "✊🏾": 989, "😩": 46, "🤸🏿‍♂️": 1, "💌": 3, "🖤": 852, "😬": 17, "💪🏽": 20, "🤦🏽‍♂️": 15, "💝": 6, "🇳🇱": 4, "😜": 5, "🥺": 243, "👌🏽": 3, "🙄": 85, "🖋": 16, "📨": 15, "🎨": 5, "💜": 230, "🧡": 53, "💛": 80, "💚": 117, "💙": 92, "💖": 74, "💗": 47, "◼": 4, "➡": 21, "🎈": 4, "😢": 124, "🇵🇸": 4, "💯": 129, "😊": 46, "🌎": 25, "😇": 10, "👼🏽": 3, "🙏🏽": 179, "🤷🏽‍♂️": 12, "🇺🇸": 105, "🦅": 5, "👇🏼": 23, "💪🏻": 4, "😠": 41, "💡": 8, "🙌🏿": 15, "💪🏿": 14, "🙏🏿": 34, "👸🏿": 2, "🙏🏻": 49, "😓": 17, "😔": 90, "💥": 35, "😍": 108, "🤘🏽": 1, "👊🏽": 20, "😂": 406, "🙈": 24, "🤔": 151, "🤬": 146, "📷": 13, "✨": 119, "🧐": 19, "📸": 19, "🙃": 18, "🙌🏾": 37, "🦠": 6, "👀": 73, "💕": 114, "🦋": 13, "🌸": 17, "🤡": 76, "🙅🏽‍♂️": 1, "🤧": 13, "👇": 184, "😭": 522, "🏬": 1, "🔥": 192, "🚒": 2, "♥": 123, "🙏": 191, "🔔": 3, "🙏🏾": 118, "😅": 41, "🙌🏼": 23, "❗": 72, "💎": 4, "🎵": 9, "🎶": 24, "👕": 4, "👏🏾": 87, "👏🏽": 73, "💢": 2, "🚶🏾‍♂️": 4, "🎥": 10, "🔁": 4, "🤲🏽": 6, "🤲🏾": 3, "🤲🏿": 5, "🤝": 21, "🏽": 4, "🏾": 4, "🏿": 5, "🤦🏾‍♂️": 18, "🖐🏼": 3, "🖐🏽": 5, "🖐🏾": 5, "🖐🏿": 4, "✌🏻": 19, "🤜🏻": 6, "🤛🏿": 11, "👍🏿": 5, "🤴🏿": 1, "🤴🏾": 8, "🏳️‍🌈": 44, "🤗": 29, "😯": 7, "🥰": 91, "😮": 23, "✌": 70, "🙇‍♀️": 8, "😹": 11, "🤲🏻": 20, "🙏🏼": 46, "💀": 55, "🌍": 20, "👋": 24, "🌹": 26, "🤟🏻": 2, "🤘🏻": 5, "😆": 17, "🤦‍♀️": 20, "🔗": 81, "😞": 26, "💪🏾": 23, "👏🏼": 72, "🤞🏾": 8, "📈": 9, "🤳🏾": 1, "📝": 9, "💪🏼": 10, "👋🏽": 2, "😷": 27, "🚮": 4, "👏🏻": 49, "🏳": 4, "🌈": 26, "🤚": 1, "🌚": 2, "🤭": 13, "🤷": 3, "😎": 37, "🐍": 2, "🤷‍♂️": 11, "™": 12, "☝": 5, "🥝": 1, "🙌🏻": 10, "👇🏽": 26, "📺": 5, "🐎": 3, "🤦🏽‍♀️": 13, "🖕": 13, "☺": 14, "👑": 51, "😈": 16, "👌": 21, "☮": 15, "🐖": 2, "🖕🏻": 13, "🚔": 4, "👼": 3, "🥀": 1, "🚨": 109, "❣": 23, "💓": 27, "🤜🏽": 5, "👊🏻": 16, "🇹🇴": 1, "😪": 22, "🤞": 3, "🇵🇷": 26, "😌": 41, "🖕🏾": 11, "🤦🏻‍♂️": 9, "🤷🏻‍♂️": 16, "👃": 1, "🤮": 43, "⚫": 10, "💪": 32, "🗣": 123, "👎": 6, "🚫": 12, "🙌": 49, "😣": 11, "🍒": 2, "😃": 15, "🏃🏽‍♂️": 1, "📚": 8, "💰": 7, "💵": 10, "⁉": 13, "👍🏻": 14, "🤑": 3, "👊": 13, "🤜": 3, "✅": 23, "💸": 2, "😨": 4, "📍": 10, "🏇🏽": 1, "🏇🏾": 1, "🙌🏽": 20, "💨": 5, "🦄": 3, "🔊": 21, "🎙": 15, "🌞": 14, "😁": 13, "⚡": 21, "🇬🇭": 8, "🌕": 2, "🇿🇼": 3, "▪": 14, "👮‍♀️": 2, "🐐": 9, "🕊": 28, "🇵🇭": 9, "👈": 3, "😡": 92, "🖕🏽": 10, "🎉": 7, "🤩": 14, "📣": 17, "💫": 17, "🧚🏽": 2, "🏡": 5, "🇳🇿": 17, "🏴󠁧󠁢󠁳󠁣󠁴󠁿": 5, "🤟": 3, "💁🏼‍♀️": 1, "🧠": 3, "👻": 2, "🤷🏾‍♂️": 18, "🤣": 168, "🤙🏻": 1, "👊🏼": 15, "👊🏾": 24, "👊🏿": 30, "✌🏼": 14, "🇭🇰": 2, "🤷🏿‍♀️": 3, "😖": 10, "🇦🇺": 3, "📊": 1, "🕷": 2, "🔴": 19, "🔵": 1, "🥋": 1, "🐷": 7, "🙂": 12, "👫": 4, "👽": 7, "🧵": 4, "👉": 15, "🇸🇾": 1, "👁": 16, "👄": 5, "🗽": 15, "©": 7, "🤨": 18, "🤦🏻‍♀️": 13, "🙆🏿‍♀️": 3, "🧢": 2, "🕯": 3, "🇬🇧": 12, "🇨🇳": 2, "😰": 5, "⏬": 3, "😿": 1, "⬇": 55, "😱": 20, "🇪🇸": 2, "😥": 24, "🇿🇦": 5, "💁🏽‍♀️": 2, "🎷": 4, "🥴": 25, "📉": 1, "🤛": 1, "😲": 10, "⬛": 6, "🇸🇦": 1, "⏳": 1, "😶": 6, "😧": 5, "💩": 15, "🤦‍♂️": 19, "🧚‍♂️": 3, "👌🏼": 6, "👍🏼": 10, "🖕🏼": 4, "🎤": 9, "🐬": 1, "🐾": 6, "👇🏻": 20, "🇰🇪": 2, "👍": 41, "🇮🇳": 3, "🤷🏻‍♀️": 12, "😝": 23, "💃🏼": 1, "🤒": 2, "🤕": 1, "😵": 4, "🏛": 5, "🧿": 4, "⚠": 42, "®": 2, "👎🏼": 3, "🤦🏽": 1, "😏": 19, "👇🏾": 27, "👇🏿": 22, "🥵": 15, "👍🏽": 15, "🖖🏼": 1, "😀": 6, "😄": 5, "🏃": 7, "🤪": 21, "😫": 21, "📦": 1, "👌🏻": 6, "🐘": 4, "💋": 8, "☂": 1, "✈": 5, "😘": 36, "💅🏽": 2, "✂": 6, "📽": 1, "🛑": 15, "☹": 3, "😴": 14, "👆🏽": 8, "🔪": 2, "🍞": 1, "🧀": 1, "🇨🇦": 12, "🐺": 6, "✌🏽": 18, "🤛🏾": 4, "🤜🏾": 3, "🐶": 2, "🥳": 6, "👩": 2, "👩‍💻": 2, "🇨🇵": 1, "🍎": 2, "🌟": 8, "🤦🏾‍♀️": 10, "🏁": 6, "🦆": 3, "🇲🇽": 7, "🏴": 8, "🌏": 5, "💃🏻": 1, "✋🏽": 3, "🇰🇷": 1, "🇯🇵": 1, "🇫🇷": 6, "🇩🇪": 9, "🇮🇹": 5, "🤫": 4, "🤦🏼‍♀️": 5, "🧼": 1, "👎🏽": 7, "👉🏻": 5, "😉": 13, "😗": 5, "🤦": 5, "♀": 1, "🤟🏾": 3, "😑": 17, "🤞🏼": 2, "🦗": 16, "🌻": 3, "✍": 3, "🎯": 4, "🖐🏻": 2, "❓": 6, "👎🏻": 1, "🤴🏽": 2, "👆🏾": 9, "🌙": 3, "🎮": 1, "⤵": 3, "💁🏽‍♂️": 3, "👍🏾": 14, "🧚🏽‍♀️": 1, "🎁": 2, "❔": 2, "🆘": 1, "🇲🇻": 3, "📮": 2, "📌": 4, "🌵": 2, "🤷🏾‍♀️": 9, "🏆": 9, "🇵🇪": 3, "🍊": 3, "🔑": 1, "🙊": 4, "🍀": 2, "🧘🏾‍♂️": 1, "😐": 21, "🗳": 8, "✌🏾": 12, "✌🏿": 10, "⚪": 2, "🗿": 1, "🇺🇬": 1, "🌧": 2, "🌊": 3, "🤙🏽": 3, "👱🏻‍♀️": 2, "🔕": 1, "🙋‍♀️": 4, "🐸": 2, "😟": 7, "📱": 5, "🇩🇿": 2, "🤦🏼‍♂️": 3, "🦢": 1, "🏝": 1, "🌺": 1, "🤦🏿‍♂️": 2, "🐯": 5, "☝🏽": 3, "🤟🏽": 3, "🤛🏽": 1, "🧚‍♀️": 4, "🤟🏿": 3, "📬": 6, "✉": 5, "🔹": 18, "🐻": 1, "🦍": 5, "🌐": 2, "📖": 2, "🦎": 1, "📎": 6, "🎂": 1, "🇺🇲": 13, "🔸": 5, "▶": 5, "📲": 4, "🐛": 2, "🔽": 4, "💅🏼": 3, "🤥": 3, "🎭": 3, "⬆": 6, "👋🏼": 3, "⚖": 12, "💃🏾": 3, "🥂": 1, "❌": 10, "👥": 2, "🙇": 1, "💶": 1, "💴": 1, "🤓": 7, "👯‍♀️": 1, "🇸🇮": 3, "🇹🇳": 1, "💣": 4, "🛸": 1, "🐝": 6, "🐦": 1, "💘": 5, "🌼": 1, "⛓": 2, "🤰🏽": 1, "☑": 20, "😋": 5, "🤠": 5, "🤲": 5, "🕋": 1, "🇲🇭": 1, "🤷‍♀️": 9, "🏷": 4, "💁🏻‍♀️": 1, "🤙🏼": 3, "☘": 5, "🇮🇪": 2, "🙅🏿‍♀️": 1, "🙅🏿‍♂️": 1, "🤞🏽": 5, "🏴󠁧󠁢󠁥󠁮󠁧󠁿": 3, "✋": 2, "✍🏽": 1, "🙋🏻": 1, "🤤": 4, "🙆": 5, "⏭": 1, "📞": 6, "🥊": 3, "🇲🇲": 1, "⌛": 1, "🔻": 4, "✖": 2, "📋": 1, "♊": 4, "🎇": 1, "🎆": 1, "⚜": 1, "🤘": 8, "❕": 4, "👋🏻": 1, "🇦🇿": 1, "🗑": 2, "🚩": 6, "1️⃣": 2, "2️⃣": 2, "3️⃣": 1, "4️⃣": 1, "5️⃣": 1, "📡": 1, "🏃🏻‍♂️": 1, "🧩": 1, "🏀": 4, "👦🏿": 1, "👦🏻": 1, "🤐": 3, "♻": 2, "🍬": 2, "🍭": 1, "🕴🏻": 3, "🇸🇻": 1, "🍑": 3, "🇨🇲": 1, "📰": 3, "✋🏻": 3, "🧚🏻‍♀️": 2, "💟": 5, "🤰🏾": 3, "🌀": 1, "👎🏾": 1, "🚶": 1, "😻": 2, "🇦🇸": 1, "🌴": 2, "🌫": 1, "🧚🏼‍♂️": 1, "🖖🏻": 2, "☠": 8, "😚": 9, "🧕🏾": 1, "🇮🇷": 1, "👉🏿": 23, "👈🏿": 10, "👉🏾": 10, "👈🏾": 8, "👉🏽": 4, "👈🏽": 4, "👉🏼": 3, "👈🏼": 2, "👆🏻": 1, "👆🏼": 3, "👆🏿": 9, "♾": 1, "👸": 2, "🍵": 1, "🔝": 1, "👸🏼": 1, "👆": 1, "🥐": 1, "👾": 1, "◻": 1, "🙆‍♀️": 1, "🙋🏼‍♀️": 1, "🍃": 3, "🐽": 1, "🤷🏼‍♂️": 1, "🤷🏿‍♂️": 2, "🤷🏼‍♀️": 6, "👸🏽": 1, "💆🏾‍♀️": 2, "🤙🏿": 5, "🐊": 1, "🍫": 1, "🇳🇬": 2, "▫": 2, "👮🏼": 1, "🇷🇺": 1, "🎺": 3, "⬅": 1, "👿": 2, "👮": 1, "🍄": 1, "🌷": 5, "🇵🇦": 1, "⛈": 1, "☀": 9, "🌤": 2, "🌖": 1, "🌜": 1, "⭐": 3, "🙁": 5, "🤚🏻": 1, "🔜": 2, "🇩🇴": 5, "👨🏿‍🦲": 1, "🇧🇧": 1, "🐩": 2, "👌🏾": 4, "🎹": 1, "☝🏾": 1, "🦘": 1, "🅿": 3, "💉": 4, "🇧🇯": 1, "👂": 4, "🙋‍♂️": 2, "🇵🇹": 1, "🧥": 1, "👩🏿‍🦱": 1, "☁": 1, "↘": 2, "🦟": 8, "👂🏾": 2, "👹": 7, "🖖": 1, "💭": 2, "♠": 1, "✝": 24, "🏹": 2, "💁🏾‍♀️": 2, "🏈": 1, "🐹": 1, "💃": 1, "🌱": 3, "🙇🏻‍♀️": 1, "🇭🇹": 1, "👅": 1, "🚚": 1, "👷🏽‍♀️": 1, "🧱": 1, "🤛🏻": 2, "➖": 18, "🎬": 3, "🔂": 3, "🎓": 1, "💧": 1, "🖕🏿": 1, "🤴": 1, "🧚🏿": 1, "😦": 3, "🚑": 1, "🌠": 1, "🤘🏿": 2, "😙": 3, "🚀": 11, "🇬🇾": 4, "🆚": 2, "⏩": 3, "🔐": 10, "🇲🇨": 1, "👺": 2, "🗺": 1, "🎧": 3, "🕉": 1, "🙋🏻‍♂️": 1, "🙋🏼‍♂️": 1, "🙋🏽‍♂️": 1, "🙋🏾‍♂️": 1, "🙋🏿‍♂️": 1, "🇨🇩": 3, "🤴🏼": 1, "🕺🏿": 1, "👮‍♂️": 1, "🚖": 1, "🖐": 1, "✏": 1, "🧻": 1, "💐": 1, "🍺": 1, "⛽": 2, "👣": 1, "🧚🏻": 2, "🏼": 1, "🔫": 3, "🧑": 1, "👌🏿": 1, "🤙": 1, "👶🏾": 1, "🧑🏾": 1, "🦱": 1, "👨🏽‍🦱": 1, "👨🏾": 2, "👨🏾‍🦲": 1, "👴🏾": 1, "🤜🏼": 2, "🎸": 2, "🙇🏾‍♀️": 4, "🛢": 1, "🙉": 2, "🇱🇷": 1, "🦸🏼‍♂️": 2, "💦": 2, "🇹🇷": 1, "🇵🇰": 1, "🍿": 1, "🤜🏿": 2, "🛫": 1, "🙅🏾‍♀️": 1, "⚽": 3, "🤳": 1, "👸🏾": 1, "💊": 1, "👚": 1, "👩🏻": 1, "💻": 1, "✋🏼": 1, "✋🏾": 1, "✋🏿": 1, "🤙🏾": 1, "🏏": 1, "🍉": 3, "🥦": 1, "🧰": 1, "🙅🏾‍♂️": 1, "♦": 1, "💍": 2, "🏃🏾‍♀️": 1, "🚻": 1, "🇫🇮": 5, "🌿": 1, "🥇": 1, "💁‍♂️": 2, "🐤": 1, "📛": 2, "✔": 10, "🏠": 1, "⛸": 1, "⛑": 2, "🤟🏼": 1, "💆🏻‍♀️": 1, "✍🏾": 1, "🤛🏼": 1, "💁🏻‍♂️": 1, "🎃": 1, "🍾": 1, "⏮": 1, "🐮": 1, "🏃🏼‍♂️": 1, "🏃🏾": 1, "🏃🏼‍♀️": 1, "🛍": 1, "🐳": 1, "🐱": 1, "♣": 1, "🧙‍♀️": 1, "👎🏿": 1, "🧚🏼‍♀️": 2})

dirname = os.path.dirname(os.path.abspath(__file__))
datatxt = os.path.join(dirname, 'data.txt')

# Create a file data.txt file - remove/comment if restarting the script in case of some errors with stream connection
with open(datatxt, mode='a', encoding='utf-8') as f:
	json.dump([], f)

emoji_regex = re.compile('[#*0-9]️⃣|[©®‼⁉™ℹ↔-↙↩↪⌚⌛⌨⏏⏩-⏳⏸-⏺Ⓜ▪▫▶◀◻-◾☀-☄☎☑☔☕☘]|☝[🏻-🏿]?|[☠☢☣☦☪☮☯☸-☺♀♂♈-♓♟♠♣♥♦♨♻♾♿⚒-⚗⚙⚛⚜⚠⚡⚪⚫⚰⚱⚽⚾⛄⛅⛈⛎⛏⛑⛓⛔⛩⛪⛰-⛵⛷⛸]|⛹(?:️‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[⛺⛽✂✅✈✉]|[✊-✍][🏻-🏿]?|[✏✒✔✖✝✡✨✳✴❄❇❌❎❓-❕❗❣❤➕-➗➡➰➿⤴⤵⬅-⬇⬛⬜⭐⭕〰〽㊗㊙🀄🃏🅰🅱🅾🅿🆎🆑-🆚]|🇦[🇨-🇬🇮🇱🇲🇴🇶-🇺🇼🇽🇿]|🇧[🇦🇧🇩-🇯🇱-🇴🇶-🇹🇻🇼🇾🇿]|🇨[🇦🇨🇩🇫-🇮🇰-🇵🇷🇺-🇿]|🇩[🇪🇬🇯🇰🇲🇴🇿]|🇪[🇦🇨🇪🇬🇭🇷-🇺]|🇫[🇮-🇰🇲🇴🇷]|🇬[🇦🇧🇩-🇮🇱-🇳🇵-🇺🇼🇾]|🇭[🇰🇲🇳🇷🇹🇺]|🇮[🇨-🇪🇱-🇴🇶-🇹]|🇯[🇪🇲🇴🇵]|🇰[🇪🇬-🇮🇲🇳🇵🇷🇼🇾🇿]|🇱[🇦-🇨🇮🇰🇷-🇻🇾]|🇲[🇦🇨-🇭🇰-🇿]|🇳[🇦🇨🇪-🇬🇮🇱🇴🇵🇷🇺🇿]|🇴🇲|🇵[🇦🇪-🇭🇰-🇳🇷-🇹🇼🇾]|🇶🇦|🇷[🇪🇴🇸🇺🇼]|🇸[🇦-🇪🇬-🇴🇷-🇹🇻🇽-🇿]|🇹[🇦🇨🇩🇫-🇭🇯-🇴🇷🇹🇻🇼🇿]|🇺[🇦🇬🇲🇳🇸🇾🇿]|🇻[🇦🇨🇪🇬🇮🇳🇺]|🇼[🇫🇸]|🇽🇰|🇾[🇪🇹]|🇿[🇦🇲🇼]|[🈁🈂🈚🈯🈲-🈺🉐🉑🌀-🌡🌤-🎄]|🎅[🏻-🏿]?|[🎆-🎓🎖🎗🎙-🎛🎞-🏁]|🏂[🏻-🏿]?|[🏃🏄](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🏅🏆]|🏇[🏻-🏿]?|[🏈🏉]|🏊(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🏋🏌](?:️‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🏍-🏰]|🏳(?:️‍🌈)?|🏴(?:‍☠️|󠁧󠁢(?:󠁥󠁮󠁧|󠁳󠁣󠁴|󠁷󠁬󠁳)󠁿)?|[🏵🏷-👀]|👁(?:️‍🗨️)?|[👂👃][🏻-🏿]?|[👄👅]|[👆-👐][🏻-🏿]?|[👑-👥]|[👦👧][🏻-🏿]?|👨(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?👨|[🌾🍳🎓🎤🎨🏫🏭]|👦(?:‍👦)?|👧(?:‍[👦👧])?|[👨👩]‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[💻💼🔧🔬🚀🚒🦰-🦳])|[🏻-🏿](?:‍(?:[⚕⚖✈]️|[🌾🍳🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?)?|👩(?:‍(?:[⚕⚖✈]️|❤️‍(?:💋‍)?[👨👩]|[🌾🍳🎓🎤🎨🏫🏭]|👦(?:‍👦)?|👧(?:‍[👦👧])?|👩‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[💻💼🔧🔬🚀🚒🦰-🦳])|[🏻-🏿](?:‍(?:[⚕⚖✈]️|[🌾🍳🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦰-🦳]))?)?|[👪-👭]|👮(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|👯(?:‍[♀♂]️)?|👰[🏻-🏿]?|👱(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|👲[🏻-🏿]?|👳(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[👴-👶][🏻-🏿]?|👷(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|👸[🏻-🏿]?|[👹-👻]|👼[🏻-🏿]?|[👽-💀]|[💁💂](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|💃[🏻-🏿]?|💄|💅[🏻-🏿]?|[💆💇](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[💈-💩]|💪[🏻-🏿]?|[💫-📽📿-🔽🕉-🕎🕐-🕧🕯🕰🕳]|🕴[🏻-🏿]?|🕵(?:️‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🕶-🕹]|🕺[🏻-🏿]?|[🖇🖊-🖍]|[🖐🖕🖖][🏻-🏿]?|[🖤🖥🖨🖱🖲🖼🗂-🗄🗑-🗓🗜-🗞🗡🗣🗨🗯🗳🗺-🙄]|[🙅-🙇](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🙈-🙊]|🙋(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|🙌[🏻-🏿]?|[🙍🙎](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|🙏[🏻-🏿]?|[🚀-🚢]|🚣(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🚤-🚳]|[🚴-🚶](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🚷-🚿]|🛀[🏻-🏿]?|[🛁-🛅🛋]|🛌[🏻-🏿]?|[🛍-🛒🛠-🛥🛩🛫🛬🛰🛳-🛹🤐-🤗]|[🤘-🤜][🏻-🏿]?|🤝|[🤞🤟][🏻-🏿]?|[🤠-🤥]|🤦(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🤧-🤯]|[🤰-🤶][🏻-🏿]?|🤷(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🤸🤹](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|🤺|🤼(?:‍[♀♂]️)?|[🤽🤾](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🥀-🥅🥇-🥰🥳-🥶🥺🥼-🦢🦰-🦴]|[🦵🦶][🏻-🏿]?|🦷|[🦸🦹](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🧀-🧂🧐]|[🧑-🧕][🏻-🏿]?|🧖(?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🧗-🧝](?:‍[♀♂]️|[🏻-🏿](?:‍[♀♂]️)?)?|[🧞🧟](?:‍[♀♂]️)?|[🧠-🧿]')

#Create a Stream listener
class EmojiStreamListener(tweepy.StreamListener):

	def __init__(self):
		# inherit class attributes
		super(EmojiStreamListener, self).__init__()
		# add tweets counter and time logger variables
		self.started = time.time()
		self.tweet_counter = 42586

	def on_status(self, status):

		if hasattr(status, "retweeted_status"):
			pass
			# avoid retweets without comments
		else:
			# check if text has been truncated
			if hasattr(status,"extended_tweet"):
				text = status.extended_tweet["full_text"]
			else:
				text = status.text
			emoji_array = emoji_regex.findall(text)
			# print(emoji_array)
			self.tweet_counter += 1
			# print(self.tweet_counter)
			counter_dict.update(emoji_array)
			elapsed = time.time() - self.started
			#write counter state to file every minute
			if elapsed > 60 :
				self.started = time.time()
				with open(datatxt, mode='a') as fd:
					line = '#:'+ str(self.tweet_counter) + '|time:'+ str(self.started) + '|dict:' + json.dumps(counter_dict, ensure_ascii=False) + '\n'
					fd.write(line)

	def on_error(self, status_code):
		print(status_code)
		if status_code == 420:
			print("420 error: sleeping for 15 min...")
			time.sleep(15 * 60)
		return True

#create a Stream
class EmojiStream():

	def __init__(self, auth, listener):
		self.stream = tweepy.Stream(auth=auth, listener=listener)

	def start(self, keywords):
		self.stream.filter(track=keywords, languages=['en'])

#start the Stream
if __name__ == "__main__":
	listener = EmojiStreamListener()

	auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	stream = EmojiStream(auth, listener)
	stream.start(keywords)
