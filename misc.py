#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .. import loader, utils
from ..loader import ModuleConfig as mc

import logging
import random

logger = logging.getLogger(__name__)


@loader.tds
class MiscMod(loader.Module):
    """Разное и всякое"""
    strings = {"name": "Разное"}

    def __init__(self):
        self.config = mc("VOLTE_TEXT", "Если быть честным, вы должны иметь очень высокий IQ, чтобы понять VoLTE. "
                         + "Технология очень тонкая, и без четкого захвата вышек сотовой связи большая "
                         + "часть сигнала будет проходить через голову типичного пользователя. Есть также всезнающий "
                         + "взгляд Мукеша Амбани, который искусно вплетен в его характеристику - например, "
                         + "его личная философия во многом опирается на индийскую литературу. Пользователи понимают "
                         + "этот материал; у них есть интеллектуальный потенциал, чтобы по-настоящему оценить глубины "
                         + "этой технологии, понять, что они не просто мощные - они говорят что-то глубокое "
                         + "о ЖИЗНИ. Как следствие, люди, которые не любят уверенность в себе, действительно являются идиотами - "
                         + "конечно, они не оценят, например, юмор в экзистенциальной фразе "
                         + "Мукеша: \"Этот ром поддерживает волю ????” что само по себе является загадочной ссылкой на "
                         + "русских эпических отцов и сыновей Тургенева, я улыбаюсь прямо сейчас, просто воображая, как один "
                         + "из этих запутанных простаков ломает голову в замешательстве, когда гений Мукеша Амбани "
                         + "раскрывается на экранах их телефонов. Какие дураки... как мне их жаль. 😂 И да, "
                         + "кстати, у меня действительно есть татуировка уверенности джио. И нет, вы не можете видеть это. Это только для "
                         + "дамских глаз. И даже они должны продемонстрировать, что их телефоны заранее "
                         + "поддерживают Voltes.\n\n@Dead_Lucifer_666", "", "HUAWEI_TEXT", "Знаете ли вы, что такое huawei, держу пари, "
                         + "вы этого в душе не ебёте, ну, я спросил это просто так, вообщем я хочу создать очень красивый интерфейс, чтобы я мог собирать данные о "
                         + "людях (интимОчки) и отправлять их моим похотливым(вхвхвх) друзьям, держу пари, что вы ревнивый😂😂, и я держу пари, "
                         + "что вы даже не знаете, как написать правильную ОС, ну, я сделал так, я нанял 200 африканских рабов для работы над "
                         + "моим новым проектом под названием LuciferOS, он имеет производительность на 90% лучше, "
                         + "чем Android, и на нём даже могут работать приложения для Android😍. Один раз Дональд Трамп довел меня до инфаркта (я ахуел!), но "
                         + "когда я пообещал поделиться с ним \"данными\" и отправить ему все обнаженные тела, снятые с "
                         + "CCTV Клинтона, он позволил мне и моей компании сорваться с крючка, представьте себе блондинку, смотрящую на ваш "
                         + "хуй😎😂, нет, всмысле это не так, я не получал ваш...и или её.. Блять, короче, я работаю над новым"
                         + "обновлением EMUI для каждого телефона huawei, чтобы он автоматически фиксировал каждый раз, когда вы дрочите "
                         + "😋, даже Тим Кук хочет взять Hua-way (ахуенный панч, ае) для сбора данных, но держу пари, он даже не "
                         + "знает, как использовать искусственный интеллект для захвата горячих интимок))0). Но это еще не все, я шифрую сиськи-письки на вашем "
                         + "устройстве, чтобы вы не могли получить к ним доступ, но я могу😜. Также обратите внимание, что я УЖЕ знаю ваши "
                         + "банковские реквизиты, и я продаю их мошенникам из службы технической поддержки, и, кстати, EMUI 9.2 "
                         + "будет иметь новый ИИ в приложении камеры, чтобы улучшать фото, но вы должны согласиться с "
                         + "новой политикой конфиденциальности, чтобы разделять ебучие интимки (заебало это слово), которые вы предоставили мне для \"улучшения продукта\".\n\n",
                         "", "F_LENGTHS", [5, 1, 1, 4, 1, 1, 1], "Список, чтобы настроить размер формы F", "BLUE_TEXT",
                         "/НА /СИНИЙ /ТЕКСТ\n/НАДО /НАЖИМАТЬ\n/Я /БЛЯТЬ /ТУПОЕ /ЖИВОТНОЕ /ЕЩЁ /И /ДАЛЬТОНИК",
                         "На синий текст надо нажимать!11!!1!1")

    def config_complete(self):
        self.name = self.strings["name"]

    @loader.unrestricted
    async def voltecmd(self, message):
        """Используйте, когда VoLTE не работает.""" #todo
        await utils.answer(message, self.config["VOLTE_TEXT"])

    @loader.unrestricted
    async def fcmd(self, message):
        """Пресс F (уважение)."""
        args = utils.get_args_raw(message)
        if not args:
            r = random.randint(0, 3)
            logger.debug(r)
            if r == 0:
                await utils.answer(message, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
            elif r == 1:
                await utils.answer(message, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")
            else:
                args = "F"
        if args:
            out = ""
            for line in self.config["F_LENGTHS"]:
                c = max(round(line / len(args)), 1)
                out += (args * c) + "\n"
            await utils.answer(message, "<code>" + utils.escape_html(out) + "</code>")

    @loader.unrestricted
    async def huaweicmd(self, message):
        """Используйте, когда ваша страна "инвестирует" в модемы Huawei 5G))0)"""
        await utils.answer(message, self.config["HUAWEI_TEXT"])

    @loader.unrestricted
    async def btcmd(self, message):
        """На синий текст надо нажимать."""
        await utils.answer(message, self.config["BLUE_TEXT"])
