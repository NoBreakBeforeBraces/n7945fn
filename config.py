from collections import OrderedDict

nid = 'syosetu_n7945fn'

title = 'D Genesis 迷宫出现三年后'

description = """自从地球上出现迷宫后已经过去了三年。
在综合化工企业的材料研究部上班，不受上司待见的我，在奥运设施的建设工地上突然变成了世界第一。

这是一个在看似合理的世界上获得了不可思议能力的主人公，过着尽可能不牵扯上世界动向的生活的，悠闲（主人公如此愿望）故事。
虽然设定很SF，但内容主要都是主人公的日常生活。

另，本故事纯属虚构。故事中出现的人物、团体、名称等，不论多么相似，都属于虚构，与现实存在的事物没有任何关系。

旧题：迷宫出现三年后。突然成了世界第一的我便辞职过上了悠闲生活。
"""

author = "之 貫紀"

menu = OrderedDict()
menu["序章"] = ("0000.tex",)
menu["第1章 于是我便辞掉了工作"] = [f'{i:0>4}.tex' for i in range(1, 16)]
menu["第2章 D Powers 启航"] = [f'{i:0>4}.tex' for i in range(16, 38)]
menu["第3章 异界语言理解"] = [f'{i:0>4}.tex' for i in range(38, 51)]

sub_characters = [
    ("𠳐", "当"),
    ("𩽾", "安"),
    ("𩾌", "康")
]


masiro_forum_id = 245
masiro_menu_thread_type = 2621
masiro_thread_type = lambda section_title, file: 2624
masiro_title_format = lambda file, section_title, chap_title: chap_title


lk_forum_id = 173
lk_thread_id = 1000215

lk_title_format = lambda file, section_title, chap_title: chap_title
