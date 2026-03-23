################################################################################
# 温灼 Demo — 主线一 + 番外一
################################################################################

# ── 角色定义 ────────────────────────────────────────────────────────────────────
define wz  = Character("温灼",   color="#b06ae0")   # 主角
define df  = Character("东方苍梧", color="#d4aa30")  # 师父
define jqm = Character("姬千渺", color="#3aacee")   # 副鬼使
define ylx = Character("喻凌霄", color="#60b040")   # 喻凌霄
define axue= Character("敖雪",   color="#40d0cc")   # 小师妹
define sf  = Character("山匪",   color="#a07040")   # 山匪
define gh  = Character("幽魂",   color="#88aacc")   # 恶鬼 / 穆小哥的魂
define ly  = Character("林大娘", color="#c0a080")   # 老妪（番外一）
define nar = Character(None, what_italic=False, what_color="#dddddd")  # 旁白
define wy = Character("???", color="#d4a0c0")    # 未知角色（预留）其实是n年后的温妍 会在前传里正式出场
define mx = Character("???", color="#80261a")    # 穆宣，随后续主角查案揭开身份

define flash = Dissolve(0.1, alpha=True)

image CG_1 = "images/CG_1.png"
image CG_2 = "images/CG_2.jpg"

################################################################################
# 游戏入口
################################################################################
label start:
    jump title_card

################################################################################
# 开场题字：逐字打出，停顿，淡出进主界面
################################################################################
label title_card:

    scene black with fade
    pause 1.2

    python:
        store.col_right = []
        store.col_left  = []

    show screen title_poem_vertical
    pause 0.5

    # 右列逐字——每次append一个字然后用renpy.pause等待
    python:
        for ch in "司命簿上三千载":
            store.col_right.append(ch)
            renpy.show_screen("title_poem_vertical")
            renpy.pause(0.3, hard=True)

    pause 1.0

    # 左列逐字
    python:
        for ch in "不及此火一瞬明":
            store.col_left.append(ch)
            renpy.show_screen("title_poem_vertical")
            renpy.pause(0.3, hard=True)

    pause 3.0

    hide screen title_poem_vertical
    scene black with fade
    pause 0.5

    jump opening

################################################################################
# 序章前：竹林入镜，旧人追来
################################################################################
label opening:

    scene black with fade
    pause 1.0

    nar "中元将至，血月渐显，黄泉之门大开，百鬼夜行。"
    nar "温灼领了上任的令牌，正欲离去——"

    play music "audio/bgm_ambient.ogg" fadein 2.0
    scene bg_grove with dissolve:
        zoom 2.2
        xalign 0.5
        yalign 0.3

    pause 0.8

    scene bg_grove with dissolve:
        zoom 1.5

    pause 0.5

    nar "身后有人唤她。"
    nar "她没有回头。"

    show wenzhuo black nobg at right:
        zoom 0.65
        xalign 0.75
        yalign 1.2

    pause 0.3

    wy "……灼姐姐。"

    nar "温灼停住了脚步。"
    nar "片刻，她侧过头，声音很轻，却很凉。"

    wz "跟来做什么。"

    nar "不是疑问句。"

    wy "我……我只是想——"

    nar "她转身，不发一言，抬手示意后者跟上，拐进了一旁更深的竹林。"
    nar "来人愣了一瞬，还是跟了上去。"

    wz "说吧。"

    show wenyan at left:
        zoom 0.9
        xalign 0.2
        yalign 1.2

    nar "竹影簌簌。来人张了张口，半晌，才挤出一句话来——"

    wy "……当年阿韫姐的事，我很抱歉。"

    jump prologue

################################################################################
# 序章：0 — 旧人造访，拒绝接受道歉
################################################################################
label prologue:

    scene bg_grove:
        zoom 1.5
    show wenzhuo black nobg at right:
        zoom 0.65
        xalign 0.75
        yalign 1.2
    show wenyan at left:
        zoom 0.9
        xalign 0.2
        yalign 1.2

    nar "树影无声。远处是长夜，近处是旧事。"
    nar "周遭安静得宛若时间停滞了很久，很久，久到来人以为不会得到任何回应。"

    nar "终于，温灼的一声轻嗤结束了这令人窒息的死寂。"

    wz  "抱歉？"
    wz  "呵……你不必抱歉。"

    nar "来人面露喜色，又有些焦急："

    wy  "那你是原谅我了？"
    wz  "原谅？"
    wy "我们还是……"
    wz  "不，我不接受你的道歉。"
    wy "那我、我要如何才能补偿你？"

    wz "补偿？"

    nar "她勾了勾唇，仿佛听到什么天大的荒唐。"

    wz "好啊……"
    nar "她的声音变得冰冷，字字如刀："
    wz "我要你经历生不如死的病痛折磨，被最信赖的人漠视、背叛、抛弃；"
    wz "我要你于万丈深渊处苦苦挣扎，心火燃了灭灭了燃，无处申冤；"
    wz "我要你经历和我一样的苦痛、绝望、虚无——"
    wz "将过去的那个软弱无能的自己，彻底杀死。"
    wz "冷漠无情，杀伐果决。"
    wz "然后拿着你的刀，踩着地狱业火，每走一步都淌着鲜血——"
    wz "重新站到我面前。"

    nar "来人愣住了，脸色煞白。又是一阵死寂。"

    wy  "……你、你！"
    wz  "呵，做不到么？"
    wy  "我……"
    wz  "做不到的话，就滚吧。"
    wy  "我……！"
    wz  "别再来见我了。"

    nar "红色的身影消失在竹林深处。"
    nar "温灼没有看。"

    hide wenyan

    play sound "audio/sfx_wind.ogg"
    nar "风过竹梢，沙沙作响。"
    nar "她站了很久，久到连自己也说不清在等什么。"
    nar "最后，她抬手理了理衣襟，往山上走去。"

    stop music fadeout 2.0

    scene bg_mountain with fade:
        zoom 2.0
        xalign 0.5
        yalign 0.5

    pause 0.8

    play music "audio/bgm_MountainWind_add.ogg" fadein 2.0
    nar "山顶上，有一道挺拔的身影。"
    nar "他背对着她，望着远处连绵的山峦，不知站了多久。"

    scene bg_mountain with dissolve:
        zoom 1.5

    show dongfang night at right:
        matrixcolor BrightnessMatrix(0.15)
        zoom 0.62
        xalign 0.7
        yalign 1.0

    pause 0.5

    nar "温灼走近，没有出声。"
    nar "他也没有回头——只是开口，像是早就知道她会来。"

    jump scene_0_5

################################################################################
# 0.5 — 师父，眼角的泪
################################################################################
label scene_0_5:

    scene bg_mountain:
        zoom 1.5
    show wenzhuo black nobg at left:
        zoom 0.65
        xalign 0.25
        yalign 1.2
    show dongfang night at right:
        matrixcolor BrightnessMatrix(0.15)
        zoom 0.62
        xalign 0.7
        yalign 1.0

    df  "处理完了？"
    wz  "嗯。"
    df  "杀了她了？"
    wz  "……让她滚了。"
    df  "哼，你倒是心软。"
    wz  "弟子无能。"
    df  "过来。"
    wz  "师父，何事？"

    nar "他轻轻抬手，替她拭去眼角的泪痕。"

    wz  "！……师父，我……"
    df  "无碍。"
    wz  "谢谢师父。"
    df  "走吧。"

    menu:
            "\"师父，去哪？\"":
                jump wander_1
            "跟上去。":
                jump wander_2

label wander_1:

    nar "东方苍梧侧转过身，"
    df  "陪吾走走。"
    wz  "哦。"

    jump wander_3

label wander_2:

    nar "她跟了上去。东方苍梧却停下了脚步。"

    wz  "师父还有何事？"
    df  "不问去哪里了？"

    nar "她摇了摇头，没有说话。"

    jump wander_3

label wander_3:

    df  "今日中元，又逢血月。你既为黄泉鬼使，可知应当如何？"
    wz  "维系阴阳秩序，令各司其职。"
    df  "若有恶鬼伤人，如何？"
    wz  "制服送还地狱。"
    df  "若有人无知无畏误入异局？"
    wz  "保其平安，消抹记忆，送回人间。"
    df  "若有人鬼勾结，倒阴为阳，混淆是非？"
    wz  "……按律，斩杀之，粉碎之，泯灭之。"
    df  "看来，是都记住了。"
    wz  "谨遵师父教诲。"
    df  "去吧。"

    hide wenzhuo black
    nar "温灼点点头，几个闪身背影便消失在夜色中。"
    nar "他凝望着她离开的方向，眼神晦暗不明；"
    nar "良久，他俯身拾起一片红叶把玩，发出了一声微不可察的叹息。"

    jump scene_1

################################################################################
# 1 — 中元夜：山匪与恶鬼
################################################################################
label scene_1:

    stop music fadeout 2.0
    scene bg_cottage_night with dissolve
    play music "audio/bgm_night.ogg" fadein 1.5
    show wenzhuo tatakai at center:
        zoom 0.35
        yalign 2.5

    nar "入夜。温灼循着异动，找到了一间茅草屋前———"
    nar "三下五除二、极为干脆利落地收拾了一只几遇发作的恶鬼，抬手便有缚灵锁将其牢牢捆上;"
    nar "接着抬眸冷眼打量周围：一旁跌坐着一个吓得半死的山匪。"

    play sound "audio/sfx_sword.ogg"
    wz  "你为何伤人？"
    nar "她用剑指着逐渐清醒的青年幽魂，"

    hide wenzhuo tatakai
    show ghost at center:
        zoom 0.45
        yalign 1.0

    gh  "那山匪偷我家中财物不说，还伤我母亲！"

    nar "恶鬼一脸怒容；"
    nar "她揉了揉眉心，用脚踢了踢那个差点就没命的山匪。"

    hide ghost
    show wenzhuo tatakai at left:
        zoom 0.35
        xalign 0.25
        yalign 2.5
    show shanfei at right:
        zoom 0.5
        xalign 0.75
        yalign 1.2

    wz  "那你呢？偷人财物便罢了，为何还伤人？"
    sf  "我…我…她…她…"
    wz  "说话。"
    sf  "我本来是想拿了东西就走的！但没想到那老太婆睡得浅，醒了，死死抱着我不撒手，还要大喊大叫！"
    sf  "我…我一时心急…就…就…"
    wz  "所以，你就动手打老人家？"

    nar "她忍着想直接砍人的冲动，收紧缚灵锁，拦住正欲发作的恶鬼。"

    sf  "我…我也是没办法…今年庄稼收成不好，赋税又重…"
    sf  "家里妻儿并不晓得我落了寇，只以为我是跟了商队做买卖的…"
    sf  "我要是被捉去见了官…我媳妇儿她一定会改嫁！那…那我儿子怎么办！"

    hide shanfei
    hide wenzhuo tatakai
    show ghost at center:
        zoom 0.45
        yalign 1.0

    gh  "那是我给我娘存的治病钱！"
    gh  "她，她一直舍不得用，想给我换口好点的棺材……"

    nar "幽魂先是咆哮，转而呜咽。"

    ly  "儿啊，是你吗？"

    nar "结界外的草屋里，老妪微微转醒，轻声咳嗽。"

    gh  "娘……"

    nar "幽魂转向屋子的方向，嚎啕大哭。"
    nar "山匪脸上红一阵白一阵，说不出话来。"

    hide ghost
    show wenzhuo tatakai at left:
        zoom 0.35
        xalign 0.25
        yalign 2.5
    show ghost at right:
        zoom 0.45
        xzoom -1
        xalign 0.8
        yalign 1.0

    nar "温灼叹了口气，放下了剑。"

    wz  "去吧。但别靠老人家太近。"
    wz  "你也知道人鬼殊途，她现在身体不好，你阴气太重，只会加剧她的病情。"
    gh  "我、我知道的。"
    wz  "丑时之前，自己回去领罚。"
    wz  "别想逃，你逃不掉的。"
    gh  "谢、谢谢大人。"

    hide ghost

    nar "她微微颔首，将目光转向山匪。"

    show shanfei at right:
        zoom 0.5
        xalign 0.75
        yalign 1.2

    sf  "……我，"

    nar "山匪吞了口唾沫。"

    wz  "人间的事不归我管。"

    nar "山匪的眼睛亮了亮——"
    nar "她扔过去一个小药瓶，冷声道："

    wz  "把这个喝了。"

    nar "山匪愣了一下，接过药瓶，手止不住地抖。"
    nar "……"

    sf  "大人饶命！大人饶命啊！！！"
    wz  "杀人者就要有被杀的觉悟，不是吗？"
    sf  "我落寇不久，未曾夺人性命啊！"
    wz  "倘若今日并非中元，那老妇做鬼的儿子不在场，遭你如此重击，怕也性命堪忧。"
    wz  "更何况，刚刚我若没出手，你已葬身鬼腹、命丧黄泉了。"
    wz  "留你苟延残喘这几刻，竟还不知足么？"
    sf  "大人饶命，大人饶命啊!"
    sf  "我家中还有妻儿…一家全靠我一人了啊！"
    wz  "真是可笑。"
    wz  "你有家人，别人的家人就不是人了么？"
    sf  "我……留小的一命，必竭尽全力为老人家养老送终！"
    sf  "有我一口饭吃就不能饿着老人家！有我一件衣穿就不能冻着老人家！"
    wz  "是么？"
    wz  "都要靠打家劫舍来养活妻儿的山匪，说的话又有几分可信？"
    sf  "我，我从现在开始从良！"
    sf  "我会想办法，我尽力！我可以对天发誓！"

    wz  "喝了。"
    nar "她的语气很平，却很冷，丝毫不容置疑。"
    sf  "大人……"
    wz  "喝。"

    nar "山匪无奈，只好喝下药。"

    wz  "从现在开始，你会慢慢忘记今夜见过的鬼，"
    wz  "但你对天发过的誓始终有效。"

    nar "山匪有些不敢相信自己的耳朵，试探地发问："

    sf  "也就是说我不会死？"
    wz  "如果你还伤天害理，可以试试自己会不会死。"
    sf  "谢过大人、谢过大人！小的一定重新做人！"
    wz  "东西放下，滚。"
    sf  "好好好小的马上滚、马上就滚！"

    hide shanfei

    nar "山匪的背影消失在夜色里。"
    nar "四周重归寂静。"
    nar "温灼回头，看向那间草屋。"

    play sound "audio/sfx_ghost.ogg"
    show ghost at center:
        zoom 0.3
        xzoom -1
        xalign 0.7
        yalign 0.65
        alpha 0.7

    nar "青年的魂魄还悬在门口，迟迟没有离去。"
    nar "她没有催他。"
    nar "只是站在原地，等着。"

    pause 0.8

    nar "屋内，老妇人翻了个身，轻声唤了一句什么。"
    nar "那个字，听不真切。"
    nar "但青年的魂魄颤了颤。"

    nar "良久，他转过身，朝她深深一揖。"

    hide ghost
    play sound "audio/sfx_ghost.ogg"
    nar "然后，消散在中元夜的风里。"

    nar "她望着那个方向，站了片刻。"
    nar "按规矩，今夜之事本不该如此了结。"
    nar "她知道。"
    nar "她只是……不想管那么多。"

    nar "她收起缚灵锁，转身离开。"

    stop music fadeout 2.0

    jump scene_1_5

################################################################################
# 1.5 — 副鬼使登场
################################################################################
label scene_1_5:

    play music "audio/bgm_backup.ogg" fadein 2.0

    scene bg_night_street with dissolve
    show wenzhuo black nobg at left:
        zoom 0.65
        xalign 0.25
        yalign 1.2
    show jiiqianmiao at right:
        zoom 0.75
        xalign 0.75
        yalign 5.5

    jqm "呦，这不是新上任的鬼使大人么？今晚的业绩怎么样啊？"

    nar "温灼无视他，径直走过。"

    jqm "哎哎哎，鬼使大人，别这么冷漠嘛。"

    nar "他嬉皮笑脸地跟了上来。温灼止步，侧目。"

    wz  "副（故意加重）鬼使大人有何贵干？"
    jqm "刚刚，我好像感受到恶鬼的气息了？"

    nar "他看向她空空如也的身后，眯着眼睛上下打量她。"
    nar "笑意不达眼底。"

    wz  "是么？"

    nar "她的语气平得像一潭死水，什么都看不出来。"
    nar "他盯着她看了一会儿，笑容重新浮上来。"

    jqm "哎～别走啊别走啊，人家想和您老人家多待一会儿嘛。"
    wz  "去南风馆蹲点了？"
    jqm "嗯？为何如此说？"
    wz  "一身风尘，油腻得很。"

    nar "他并不恼，仍笑眯眯地跟着。"

    jqm "鬼使大人如此优秀，令人情难自禁嘛。"
    wz  "哦？所以你有受虐倾向，上次败得不够惨？"
    jqm "咳…我…"

    nar "他正欲开口解释，却突然感受到了什么风吹草动；"
    nar "两人不约而同看向不远处——"

    wz  "啧。"

    nar "温灼一个起身，扶着剑蹿了出去。"

    jqm "哎，小心点啊。"

    nar "副鬼使拿好铁扇，轻盈地跟了上去。"

    jump scene_2

################################################################################
# 2 — 幻境：梅花院与孤独的孩子
################################################################################
label scene_2:

    stop music fadeout 2.0
    play music "audio/bgm_illusion.ogg" fadein 2.0

    $ clue_letter = False      # 梳妆台信件（必须项）
    $ clue_child = False       # 孩子痕迹
    $ clue_altar = False       # 庭院祭坛/梅树
    $ clue_seal = False        # 封印残迹
    $ explored_count = 0       # 已探索数量

    scene bg_ruins with pixellate:
        zoom 1.5
    show wenzhuo tatakai at left:
        zoom 0.35
        xalign 0.25
        yalign 2.5
    show jiiqianmiao at right:
        zoom 0.75
        xalign 0.75
        yalign 5.5

    wz  "是幻境。"
    jqm "你蹿得太快了。"
    wz  "那你为什么跟进来了？"
    jqm "咳…业绩总不能都让你冲了？"

    nar "温灼环视四周，月色冷白，梅花开得诡异地盛——明明只是九月。"
    nar "废墟深处，有几处还残存着当年的样子。"

    wz  "分头查。"
    jqm "哎？"
    wz  "有意见？"
    jqm "……没有。"

    nar "他收起折扇，往另一侧走去。"

    jump explore_loop

################################################################################
# 探索循环
################################################################################
label explore_loop:

    scene bg_ruins with dissolve:
        zoom 1.5
    show wenzhuo tatakai at left:
        zoom 0.35
        yalign 2.5

    # 动态提示
    if (not clue_letter or not clue_child):
        nar "找找看有什么线索吧。"

    menu:
        "【梳妆台】走进内室，查看梳妆台。" if not clue_letter:
            jump explore_dresser
        "【遗忘的角落】墙角有些细微的踪迹……" if not clue_child:
            jump explore_child
        "【庭院梅树】院中那棵梅树有些不对劲。" if not clue_altar:
            jump explore_altar
        "【地板裂缝】地板上似乎有什么符文残迹。" if not clue_seal:
            jump explore_seal
        "【离开】差不多了，去找姬千渺汇合。" if (clue_letter and clue_child):
            jump explore_done
 
################################################################################
# 探索点 1：梳妆台（必须项）
################################################################################
label explore_dresser:

    hide wenzhuo tatakai
    nar "内室光线昏暗，一张梳妆台立在角落，镜面蒙尘，却不知为何一尘不染地放着一只雕花木盒。"
    nar "温灼拿起木盒，打开——"
    nar "里面叠放着厚厚一沓信件，每一封的落款都是同一个名字：「梅娘」。"
    wz  "「穆郎亲启」……"
    nar "她随手抽出一封，展开，字迹清秀，墨色已经发黄。"
    nar "信里写的都是些寻常事——院子里的猫、新摘的梅子、孩子昨夜说了什么梦话。"
    nar "但每一封的结尾，都只有同一句话。"
    wz  "「郎君，我在等你。」"
    nar "她沉默了片刻，把信叠好放回去，将木盒揣进怀里。"

    $ clue_letter = True
    $ explored_count += 1
    jump explore_loop

################################################################################
# 探索点 2：孩子的角落（必须项）
################################################################################
label explore_child:

    hide wenzhuo tatakai
    nar "墙根处堆着几样东西——一双极小的虎头鞋，一个缺了耳朵的泥塑兔子，还有几根折断的细竹棍。"
    nar "温灼蹲下来，拿起那只泥塑兔子翻了翻，底部刻着两个字。"
    wz  "「阿宣」……"
    nar "她把兔子轻轻放回原处。"
    nar "这院子里还有个孩子——或者说，曾经有个孩子住在这里。"

    $ clue_child = True
    $ explored_count += 1
    jump explore_loop

################################################################################
# 探索点 3：庭院梅树
################################################################################
label explore_altar:

    hide wenzhuo tatakai
    nar "院中那棵梅树老得出奇，树皮皴裂，根部已经半朽，按理早该枯死。"
    nar "但满树的花开得极盛，花瓣落了一地，带着不合时节的浓香。"
    nar "温灼伸手触碰其中一朵——指尖传来一阵凉意，不是花的温度。"
    wz  "执念……"
    nar "她收回手，低头看树根处。"
    nar "根部的土是新翻过的。不久前，有人在这里埋过什么。"
    nar "或者——葬过什么。"

    $ clue_altar = True
    $ explored_count += 1
    jump explore_loop

################################################################################
# 探索点 4：地板封印残迹
################################################################################
label explore_seal:

    hide wenzhuo tatakai
    play sound "audio/sfx_seal.ogg"
    nar "地板的裂缝沿着某种规律延伸，不像是自然风化——温灼蹲下细看，纹路下面隐着半截符文。"
    nar "被人故意磨平了，但痕迹还在。"
    wz  "封印……而且不是普通的手法。"
    nar "她顺着纹路描了一段，眉头微微蹙起。"
    wz  "来头不小。"
    nar "有人曾经用某种封印术，把这个地方从阳间的地图上抹掉过。"
    nar "——不是废弃，是刻意封锁。"

    $ clue_seal = True
    $ explored_count += 1
    jump explore_loop

################################################################################
# 汇合：温灼探索完毕
################################################################################
label explore_done:

    scene bg_ruins with pixellate:
        zoom 1.5
    show wenzhuo tatakai at left:
        zoom 0.35
        xalign 0.25
        yalign 2.5

    nar "探查完一番，温灼在院中站定，将收集到的线索在脑中整理了一遍。"

    if clue_altar and clue_seal:
        nar "废弃的闺阁，反季盛开的梅花，刻意封锁的手法，唤作「阿宣」的孩子……"
        nar "执念的根源就在这院子里。"
    elif clue_altar:
        nar "信件，孩子的痕迹，还有那棵梅树下翻新的土……"
    elif clue_seal:
        nar "信件，孩子的痕迹，还有地板下被刻意磨平的封印痕迹……"
    else:
        nar "信件上的名字，还有那个孩子留下的东西……应该够了。"

    nar "线索还差一块——「穆郎」究竟是什么来头。"

    show jiiqianmiao at right:
        zoom 0.75
        xalign 0.75
        yalign 5.5

    nar "恰好，姬千渺从另一侧踱了回来，折扇轻摇，神情比分头时多了几分正经。"

    jqm "查得怎么样？"
    wz  "你先说。"
    jqm "哟，还挺会用人。"
    wz  "……"
    jqm "好好好，我说。"

    nar "他收起折扇，声音压低了些。"

    jqm "这建筑的格局，我认得——像人间的风月场，而且年头不短了。"
    jqm "另外，院里那些梅花……"

    if clue_altar:
        wz  "梅树根部的土是新翻的，我注意到了。"
        jqm "不只是这个。那些花的灵力痕迹很异常，像是有什么执念被封在里面，以梅为引，久久不散。"
    else:
        jqm "那些花的灵力痕迹很异常，像是有什么执念被封在里面，以梅为引，久久不散。"

    if clue_seal:
        wz  "地板下有封印的痕迹，被人磨平了，但手法不普通。"
        jqm "嗯，这地方在阳间的地图上根本不存在——我查了一下阴差的旧档，三年前有过一条记录，之后就再没有了。"
        jqm "有人把它从两界的档案里一起抹掉了。"
        wz  "刻意封锁……是在隐瞒什么，或者说保护什么？"
        jqm "嗯，但是谁做的、用了什么手法，还需要进一步查。"
    else:
        jqm "这地方在阳间的地图上根本不存在——我查了一下阴差的旧档，三年前有过一条记录，之后就再没有了。"
        jqm "有人把它从两界的档案里一起抹掉了。"
        wz  "刻意封锁……是在隐瞒什么，或者说保护什么？"
        jqm "嗯，但是谁做的，还需要进一步查。"

    nar "两人沉默片刻。"

    wz  "梳妆台上有信，落款是「梅娘」，收件人是「穆郎」。"
    jqm "「穆郎」……所以这里住的是他的人。"
    wz  "还有个孩子住过的痕迹。"
    jqm "孩子？那执念的核心……八成就在这院子里待过的某个人身上。"

    if clue_altar:
        wz  "梅树根部的土是新翻的。人是葬在这里的。"
        jqm "葬的是谁？是那个孩子吗？"
        wz  "不清楚。也有可能是……孩子的母亲？"
        jqm "嗯……或者都有。"
        wz  "……"
        jqm "总之，得找到阵眼，或者说执念的根，才能破除幻境。"

    nar "温灼看了看四周，梅花的香气浓得有些压抑。"
    wz  "所以——有人被封在这里，有人死在这里，还有……"

    nar "她话未说完，视线忽然定住了。"

    nar "梅花开得极盛——明明只是九月。"

    scene CG_1 with dissolve
    pause 2.5

    nar "台阶上坐着一个抱膝的小孩。"
    nar "眨眨眼睛，一声不吭地打量来者。"
    nar "不知道在这里坐了多久——也不知道，是人，还是鬼。"

    scene bg_ruins with pixellate:
        zoom 1.5
    show wenzhuo tatakai at left:
        zoom 0.35
        xalign 0.25
        yalign 2.5
    show jiiqianmiao at right:
        zoom 0.75
        xalign 0.75
        yalign 5.5

    jqm "小朋友，你好。我们不是坏人，你在这干什么呀？"
    mx  "……"
    nar "小孩儿没有说话，只是继续盯着他们看。"

    nar "温灼俯下身，轻声问："
    wz  "「小宣」？"

    nar "小孩儿的眼神微微动了动，却仍旧没有开口。"

    jqm "「小轩」？「气宇轩昂」的「轩」？"
    nar "姬千渺闻言挑了挑眉。"

    nar "小孩儿终于开口，声音很稚嫩，却格外清晰："

    mx  "是「宣告」的「宣」。"

    nar "姬千渺愣了愣，看向温灼。"
    nar "她若无其事地摸了摸小孩儿的头，递给小孩儿一颗话梅糖。"

    wz  "你母亲的名字是「梅娘」吗？"

    nar "小孩接过糖，点点头。"

    wz  "她在家吗？"
    nar "小孩儿摇摇头。"

    wz  "你爹爹是「穆郎」?"
    nar "她仍一脸温柔，温声细语。"
    nar "小孩儿又点了点头。"
    nar "一旁的姬千渺有些吃惊，他从来没见过温灼这副模样："
    nar "这么温柔的鬼使大人——其恐怖程度绝不亚于他迄今为止见过的所有幻境。"

    wz  "可以带我们逛逛吗？"
    jqm "等等——"
    nar "姬千渺还没来得及阻拦，温灼却已经牵起了小孩儿的手。"
    nar "小孩儿没有挣扎，任由她牵着，只是有些犹豫。"
    mx  "爹爹…不让。"
    wz  "因为害怕有坏人欺负娘？"
    mx  "嗯，坏人会把我和娘都抓走。"

    nar "姬千渺不知从哪变出一串冰糖葫芦递给小孩儿，然后偷偷扯了扯温灼的衣袖，接通心音传声："

    jqm "在吗在吗？何方妖孽竟敢冒充我们黄泉鬼使！"
    nar "温灼没有说话，只是对他翻了个白眼。"
    jqm "哦还好还好，是真的！"
    wz  "……说正事。"
    jqm "你再问问孩子他爹啥来头呗？"
    wz  "以这个孩子的警惕程度，我们可能问不出来。"
    wz  "不过根据刚才的线索……孩子他爹的来头不会小，至少也得是个鬼王级别的。"
    nar "她顿了顿，补充道："
    wz  "毕竟，孩子的母亲曾经是个活人。"
    nar "两人的视线不约而同落在了院子中央那棵反季盛开的梅树上。"
    jqm "咳…你是说鬼和活人生了个孩子吗？"
    wz  "从室内的书信内容来看，似乎是这样的。"
    jqm "呃……好不幸。"
    wz  "是挺不幸的，就留孩子一个人在这，不知道爹娘去哪儿了。"
    jqm "我是说我们不幸…"
    wz  "嗯？为何？"
    jqm "呃…你懂吧…就是这事儿我们可能没法儿管，搞不好还会被灭口！"
    nar "温灼无语。"
    wz  "你可以了（咬字极重）姬、大、人，你家什么背景你自己清楚！"
    wz  "快把你八卦的小表情收一收！"
    jqm "哎呀呀，这么没情趣吗？"
    wz  "你是不是一秒不发癫就会死？"

    nar "小孩儿稚嫩的声音打断了两人的虚空扯皮。"

    mx  "姐姐…哥哥…"
    jqm "怎么啦？"
    mx  "娘说…说今天爹爹会来接她…"

    nar "两人愣了愣，互相对视了一眼。"

    mx  "但是她说，她没法带我去…她说她的时候到了，我的还没有…"

    nar "小孩儿有点沮丧，手里的冰糖葫芦都不香了。"

    mx  "他们…他们什么时候能来接我？"
    mx  "我会很听话，不会偷偷跑出院子，不会惹娘生气…"
    mx  "他们……是不是不要我了？"
    wz  "不会的，没有的事。"

    nar "她轻轻握住小孩儿的手。"

    jqm "我们带你去找爹娘。"

    nar "姬千渺握住了小孩儿的另一只手。"

    jump scene_2_5

################################################################################
# 2.5 — 收尾：你并非一无是处
################################################################################
label scene_2_5:

    stop music fadeout 2.0
    play music "audio/bgm_backup.ogg" fadein 2.0

    scene bg_night_street with pixellate
    show wenzhuo black nobg at left:
        zoom 0.65
        xalign 0.25
        yalign 1.2
    show jiiqianmiao at right:
        zoom 0.75
        xalign 0.75
        yalign 5.5

    wz  "没想到你还有这种义气。"
    jqm "彼此彼此。"
    nar "姬千渺轻轻做了个揖，又摇了摇扇子。"
    jqm "这孩子先放我舅舅那好吃好喝伺候着；"
    jqm "然后再麻烦他老人家查一查是哪位同僚在人间的风流债…"
    nar "姬千渺指了指一旁啃着冰糖葫芦的小孩儿："

    hide wenzhuo black nobg
    hide jiiqianmiao
    show muxuan at center:
        zoom 0.5
        xalign 0.5
        yalign 0.6
        
    jqm "你看，他出来以后幻境就散了，这小家伙就是阵眼。"

    hide muxuan
    show wenzhuo black nobg at left:
        zoom 0.65
        xalign 0.25
        yalign 1.2
    show jiiqianmiao at right:
        zoom 0.75
        xalign 0.75
        yalign 5.5

    wz  "有劳了。"
    nar "姬千渺挑眉。"
    jqm "怎么不多夸夸我？"
    wz  "你真棒。"
    jqm "啊，好敷衍啊。"

    nar "温灼沉默。"

    jqm "哎？这次不拿剑抽我了？"

    nar "还是沉默。"

    jqm "怎么不说话？"
    wz  "你并非一无是处。"
    jqm "那当然啦，毕竟我怎么着也是光明正大坐到这个位置上的！"
    wz  "嗯，很棒。"
    jqm "……鬼使大人你知道吗？"
    wz  "嗯？"
    jqm "每次你笑起来我都觉得出现幻觉了……"

    menu:
        "拿剑抽他——":
            pass
        "狠狠地抽 !!!":
            pass

    jqm "啊啊啊别打我多笑笑啊你笑起来很好看啊！！！"

    jump scene_3

################################################################################
# 3 — 小师妹登场 → 喻凌霄闯入
################################################################################
label scene_3:

    stop music fadeout 2.0
    play music "audio/bgm_light.ogg" fadein 2.0

    scene bg_market with dissolve:
        zoom 1.5
    
    show wenzhuo black nobg at center:
        zoom 0.65
        xalign 0.5
        yalign 1.2

    nar "忙忙碌碌一晚上，天明时终于清闲。温灼在早市上买了一碟油饼和一碗豆浆，慢悠悠往回赶。"

    axue "师姐——"

    nar "大老远有人喊。她回眸。"

    hide wenzhuo    
    show wenzhuo black nobg at left:
        zoom 0.65
        xalign 0.25
        yalign 1.2
    show aoxue at right:
        zoom 0.35
        xalign 0.75
        yalign 1.0

    axue "好巧呀师姐！"

    nar "小师妹屁颠屁颠跑过来，有点气喘吁吁。"

    axue "我刚出任务回来，就听同门说师姐出师任黄泉鬼使去了…"
    axue "师姐师姐，你为什么不去仙门呀？"
    axue "待遇丰厚，环境又好，还不用上夜班！"
    axue "师姐你不是最讨厌晚上有人吵你睡觉了吗？"
    wz  "……"
    axue "师姐？"
    wz  "抱歉，我太困了…"
    axue "哦哦哦，那我送你回去…"
    wz  "不必。"
    axue "师姐…"
    wz  "罢了，随你。"
    axue "嘿嘿嘿我就知道师姐最好啦！"
    axue "师姐，鬼使的工作好玩吗？"
    wz  "还行。"
    axue "那等我出师了，也去投靠你好不好？"
    wz  "嗯？你不是想去仙门么？"
    axue "仙门虽好，但是没有师姐啊。"
    wz  "……有我没我都一样的。"
    axue "那不行，看不见你我就会想你，很想很想，没法工作的那种想！"
    wz  "哦。"
    axue "师姐你好冷漠哦！"
    wz  "习惯就好。"
    axue "……我不会放弃的！"
    wz  "行。"
    axue "师姐你知道我在说什么嘛！"
    wz  "知道。"
    axue "我在说什么？"
    wz  "你要当我的小跟班。"
    axue "才不是小跟班！"
    wz  "行。"

    nar "小师妹叽里呱啦一堆，她只是淡淡微笑应和着，"
    nar "仿佛来人有再大的热情也只会像一拳打在棉花上，探不到底。"

    scene bg_outside with dissolve
    show wenzhuo black nobg at left:
        zoom 0.65
        xalign 0.25
        yalign 1.2
    show aoxue at right:
        zoom 0.35
        xalign 0.75
        yalign 1.0

    wz  "就送到这里吧。"
    axue "师姐…"

    nar "小师妹拉住她的手，舍不得放开。"

    wz  "……"
    axue "嘤嘤嘤那我走了…"
    wz  "嗯，注意安全。"

    stop music fadeout 1.5
    play music "audio/bgm_ambient.ogg" fadein 1.5
    scene bg_room_day with dissolve:
        zoom 1.5
    show wenzhuo black nobg at left:
        zoom 0.65
        xalign 0.5
        yalign 1.2

    nar "温灼正欲推门——等等，这门……屋里有人？"
    nar "她单手扶剑，轻轻推开一条缝，屏息静气。"
    nar "没有声音。没有气息。没有灵力波动。"
    nar "但是——"

    $ room_check = 0

    menu:
        "【门锁】仔细检查门锁，确认被动过没有。":
            nar "锁芯有极细微的划痕，不是自然磨损。"
            nar "有人开过这把锁，而且手法很干净，几乎不留痕迹。"
            wz  "……"
            nar "她将这个发现压在心里，没有动作。"
            $ room_check += 1
            jump room_enter

    label room_enter:

    nar "她迈步进屋，手没有离开剑柄。"

    menu:
        "【扫视四角】从左到右，逐一确认屋内死角。":
            nar "左侧书架后——没有。"
            nar "右侧屏风后——没有。"
            nar "床帐内——没有。"
            nar "正常人的藏身之处，都查过了。"
            $ room_check += 1
            jump room_check2
        "【感知灵力】放开感知，探查屋内有无异常灵力残留。":
            nar "她收敛心神，向四周散开一道灵识。"
            nar "……什么都没有。干净得出奇。"
            nar "比正常的空屋子还要干净。"
            wz  "（奇怪……）"
            nar "但就是找不到任何依据。"
            $ room_check += 1
            jump room_check2

    label room_check2:

    menu:
        "【再查一遍】感觉不对，再仔细查一遍。":
            nar "她又把屋子从头到尾过了一遍。"
            if room_check >= 2:
                nar "门锁有痕迹，但屋内一无所获。"
                nar "要么是有人进来又离开了，要么……"
                wz  "（要么这个人的遮掩手段，比我强。）"
                nar "她在这个念头上停了一瞬，然后把它压了下去。"
                nar "一晚上没睡了，大概是疑神疑鬼。"
            else:
                nar "还是什么都没有。"
                nar "她站在屋中央，沉默了片刻。"
            jump room_give_up
        "【算了】查了一圈没发现，太困了。":
            jump room_give_up

    label room_give_up:

    wz  "奇怪……算了……泡个澡睡觉吧。"

    hide wenzhuo black nobg

    nar "美滋滋泡了个澡，一觉睡到下午。伸着懒腰，"

    scene bg_room_night with dissolve:
        zoom 1.5

    stop music fadeout 2.0

    nar "突然发觉身边多了个人!"
    wz  "你他妈——"

    menu:
        "拔剑!":
            play sound "audio/sfx_sword.ogg"
            jump conflict

    label conflict:

    nar "温灼正要挑剑抵上来人的咽喉，却被对方一个侧身压在身下，硬生生抵在床上动弹不得。"

    play music "audio/bgm_conflict.ogg" fadein 1.5
    show CG_2 with dissolve

    nar "傍晚时分，尚未掌灯，屋子里的自然光线很暗；"
    nar "但来人那张从小看到大的、朝夕相处过起码十五年的脸，"
    nar "温灼真的熟悉到不能再熟悉了。"
    nar "那张脸的眼尾泛着难掩的红，嘴角却带着一抹苦涩的笑。"
    ylx "阿灼，是我…"

    scene bg_room_night with dissolve:
        zoom 1.5
    show yulingxiao at left:
        zoom 0.4
        xalign 0.25
        yalign 2.3 
    show wenzhuo nobg at right:
        zoom 0.7
        xalign 0.75
        yalign 1.3

    wz  "我他妈知道是你才劈的！"
    ylx "阿灼，为什么抛下我…"
    wz  "你他妈说清楚是谁抛下谁？"
    ylx "那阿灼为何不来仙门寻我…"
    ylx "是…忘记了我们的婚约了吗？"
    wz  "你他妈婚你约个大头鬼，你的阿灼已经死了！"
    ylx "胡说！！！"
    ylx "阿灼没有死！跟我回去，听话！"
    wz  "我凭什么要听你的话！"
    ylx "凭我是你未婚夫，是你从小黏到大的兄长！"
    ylx "凭你体内的火毒只有我能解，也必须是我来解！"

    nar "温灼没有说话。"
    nar "只是笑了——那种不含任何温度的、彻底陌生的笑。"

    wz  "喻凌霄你够了，"
    wz  "你以为我稀罕活着？"
    wz  "滚！把你的脏手拿开！离我远点！"
    ylx "阿灼…嫌我脏？"
    wz  "脏，脏死了！"
    wz  "你们一脉没一个好东西，祖上给我们下咒，"
    wz  "世世代代女子若是不和你们干那勾档子事就只能火毒发作暴毙身亡，"
    wz  "不就是为了喝我们的血？"
    ylx "……"
    wz  "呵，以为我不知道？"
    ylx "阿灼，你…"
    wz  "阿姐不肯嫁那三妻四妾的狗东西，所以她死了，死在了要和心上人一起走的前一晚！"
    wz  "我亲眼看见她化成滔天的火焰，大火烧了整个院子，烧了三天三夜！"
    wz  "那卖女儿的老贼不让我对外人说，说阿姐是咎由自取！"
    wz  "咎由自取？呵，活该他生不出儿子！"

    nar "喻凌霄没有说话。"
    nar "她也没有给他开口的机会。"

    ylx "阿灼，我…"
    wz  "那么喻凌霄，喻家大少，我问你："
    wz  "那时我去找你，想问个清楚，却被门人拦着不让进。"
    wz  "你人呢，在哪里？回答我！"
    ylx "我…"
    wz  "是，我们家没落了，所以你母亲给你物色了一堆门当户对听话乖巧又「懂事」的新贵小姐，撺掇你毁约；"
    wz  "那么你是怎么想的，嗯？"
    ylx "我从来没想过要毁约！"
    ylx "那是我母亲设的局，我没让她们碰我！"
    ylx "我一脱身，就马上来找你了！"
    ylx "但是，你父亲说，说你…死在那场大火里了…"
    ylx "我不信，我一直在找你…"
    ylx "我找了你很久很久…"
    ylx "能不能…别丢下我…阿灼…"

    nar "屋子里很暗。"
    nar "暗到看不清他眼睛里的东西。"
    nar "或许是真的，或许不是。"
    nar "她不想知道。"

    wz  "喻凌霄，"

    nar "温灼闭上眼，深呼吸。"

    wz  "我已经长大了，不会再黏着你，也不会当听话的娃娃了。"
    ylx "没关系阿灼，跟我回去，母亲那里有我…"
    wz  "呵，听不懂人话？"
    wz  "你个还没断奶的小屁孩儿跟我谈感情？"
    ylx "阿灼，"
    ylx "这是气话对不对？"
    wz  "你他妈别仗着自己天赋异禀就想压我一头！"
    wz  "我告诉你，我今天就是死，也不会跟你回去！"
    ylx "那阿灼可别怪我不客气了。"
    wz  "你他妈——"

    menu:
            "\"师父救我！！！\"":
                pass

    ylx "你还有别的男人？！"

    scene black with fade
    wz  "师父，唔——"
    nar "温灼话还没说完，被喻凌霄一个滚烫的吻封住了嘴。"

    # stop music fadeout 1.0
    play sound "audio/sfx_gold.ogg"
    nar "一道金光闪过。"

    scene bg_room_night with flash:
        zoom 1.5
    show dfcw_sq_nobg at center:
        zoom 0.75
        yalign 2.5

    df  "放肆！"

    nar "喻凌霄回过神来的时候，发现自己已经被掀飞了。"

    show wenzhuo nobg at right:
        zoom 0.7
        xalign 0.75
        yalign 1.3
    show dfcw_sq_nobg at left:
        zoom 0.75
        xalign 0.25
        yalign 2.5

    wz  "师父！"

    nar "东方苍梧抬手，一件袍子轻轻落在温灼身上。"

    df  "莫怕，待吾处理了这厮。"

    hide wenzhuo nobg
    show yulingxiao at right:
        zoom 0.4
        xalign 0.75
        yalign 2.3
    show dfcw_sq_nobg at left:
        zoom 0.75
        xalign 0.25
        yalign 2.5

    ylx "你就是阿灼的「师父」?"
    df  "聒噪，想好死法了？"
    ylx "前辈何必咄咄逼人？"
    df  "伤吾徒儿者，死。"
    ylx "阿灼是我爱妻，我们只是在做夫妻应该做的事。"

    hide yulingxiao
    show wenzhuo nobg at right:
        zoom 0.7
        xalign 0.75
        yalign 1.3

    wz  "我不是！你他妈个臭流氓！"

    hide wenzhuo nobg
    show yulingxiao at right:
        zoom 0.4
        xalign 0.75
        yalign 2.3

    ylx "父母之命，媒妁之言。青梅竹马，郎情妾…"
    df  "吵死了，下辈子注意点。"

    hide yulingxiao
    nar "一个抬掌，喻凌霄消散在金光里。"

    show wenzhuo nobg at right:
        zoom 0.7
        xalign 0.75
        yalign 1.3

    wz  "！……"
    df  "放心，没死，只是让他长长记性。"
    wz  "……多谢师父。"
    df  "你的火毒，我未曾听你说过。"
    wz  "……只是小事。"
    df  "为师会想办法，不要一个人想着去死。"
    wz  "生死本就是常事，徒儿不在乎的。"
    df  "为师在乎。"

    nar "沉默。"
    nar "很长的沉默。"

    hide dfcw_sq_nobg
    show dongfang nobg at left:
        zoom 0.75
        xalign 0.25
        yalign 2.5

    wz  "师父？"
    df  "别怕，师父在这。"

    nar "她没有说话。"
    nar "只是站在那里，没动。"

    wz  "师父，你为什么对我这么好？"
    df  "徒儿值得。"
    wz  "哦。"
    df  "嗯。"

    jump mainline1_end

################################################################################
# 主线一 尾声
################################################################################
label mainline1_end:

    stop music fadeout 3.0

    scene bg_night_street with fade

    nar "中元夜过后，血月已隐。温灼上任黄泉鬼使的第一天，就这样过去了。"
    nar "——接下来，还有很长的路要走。"

    play sound "audio/sfx_page.ogg"
    show screen chapter_end_screen("主线一", "番外一·山匪与短命鬼")

    pause

    hide screen chapter_end_screen

    jump gaiden_1

################################################################################
#  番外一 — 山匪与短命鬼
#  原文为散文叙事，此处改编为旁白+少量对话的视觉小说格式
################################################################################
label gaiden_1:

    play music "audio/bgm_gaiden.ogg" fadein 2.0

    $ sf_gaiden = Character("男子", color="#a07040")  # 番外里身份未揭晓，暂显"男子"

    scene bg_cottage_day with fade:
        zoom 0.75

    nar "【番外一·山匪与短命鬼】"
    nar "宛宁县的山窝窝头里住着一户人家——准确地说，只剩一个老妪。"

    show lindaniang at center:
        zoom 0.4
        xzoom -1
        yalign 1.0

    nar "林大娘的大儿子早年当兵，从此再无音讯；"
    nar "小儿子年初上山采药，遇上暴雨山顶滑坡，才二十出头便走了，还没有娶亲。"
    nar "那破旧的小茅屋里，只剩林大娘一个人吊着一口病痨气。"

    hide lindaniang
    
    nar "不知从哪天起，总有个陌生的中年男子隔三岔五送来衣物、吃食和药，虽然从他的衣着看，自己的日子也不宽裕。"

    show bandit at center:
        zoom 0.5
        xalign 0.25
        yalign 1.0
    
    nar "林大娘起初不打算收。"
    nar "对方却解释说这是她小儿子以前卖药赊给自己的货钱，本打算日后一起结清；"
    nar "但既然青年已经不在了，一直拖欠着老人家的东西也不厚道。坚持再三，林大娘这才收下。"

    scene bg_cottage_night with dissolve
    show bandit at left:
        zoom 0.5
        xalign 0.25
        yalign 1.0
    show lindaniang at right:
        zoom 0.4
        xzoom -1
        xalign 0.75
        yalign 1.0

    nar "有一天林大娘颤颤巍巍拉着他留他吃晚饭，他本想推脱，老太太却坚持。"

    nar "饭间，林大娘说感谢他这些天来的照顾——如果她儿子还活着，应该也是这样的吧。"

    sf_gaiden  "如果我娘还在……大概也会像现在这样，和我一起吃饭吧。"

    nar "半晌，林大娘提了一个请求："
    ly  "小伙子，恁能找人把俺娃的坟迁到风水稍好点儿的地方不？"
    ly  "俺寻思迁完坟恁也不欠俺啥了，以后莫得来了。恁看中不中？"
    nar "男子迟疑了一下，点了点头。"

    hide lindaniang
    hide bandit

    scene bg_cottage_day with dissolve:
        zoom 0.75

    nar "然而坟迁完后，那男子还是照旧来看望林大娘。"
    nar "只是这天，门没有像往常一样开。"
    nar "他以为老太太睡着了，悄悄把东西放在桌上，转身欲走——"
    nar "走了没两步，鬼使神差，他又退了回去。"

    nar "林大娘在床上睡着，神情很安详。"
    nar "他颤抖着伸手探了探鼻息，愣了愣，又轻轻晃了晃她——"
    nar "老太太始终没有醒。"

    nar "老太太下葬时，他突然觉得心里空了一块。"

    scene bg_field with fade

    nar "收拾老太太的遗物时，他发现了一张字条——是林大娘托路过的识字人代写的，"
    nar "他着急忙荒赶下山找到了市集上的说书先生，请他将字条念给自己听："
    ly  "俺就知道恁是骗俺的。"
    ly  "俺娃没跟俺说有谁欠药钱——"
    ly  "俺年纪大了，眼睛是花了，但耳朵还灵着呐，"
    ly  "恁说话声和那天抢东西那个人一模一样嘞。"
    ly  "但俺相信恁是个好人，肯定有啥说不出来的苦。"
    nar "剩下的内容，是她还有多少积蓄藏在什么地方——虽然不多，但自己也终于用不上了，这世道大家都不容易，他还是拿回去给家里小孩吧。"
    nar "结尾只有一句话——"
    ly  "孩子，愿菩萨保佑你。"

    nar "他无言良久。说不清这到底是祝福还是诅咒，"
    nar "只是他的余生，大概要一直这样如此艰难地直立行走了。"

    nar "——后来，宛宁县有人见过一个男子，在山路上慢慢走着，背着一筐草药，衣裳虽旧，步子却很稳。"
    nar "他没有再做山匪。"

    show screen chapter_end_screen("番外一", "山匪与短命鬼  完")
    pause
    hide screen chapter_end_screen

    scene black with fade
    pause 1.0

    show screen demo_end_screen
    pause
    hide screen demo_end_screen

    return

################################################################################
# 界面：章节结束卡
################################################################################
screen chapter_end_screen(chapter, subtitle):
    frame:
        xalign 0.5
        yalign 0.5
        padding (80, 50)
        background "#00000099"
        vbox:
            spacing 18
            text chapter  xalign 0.5 size 40 color "#c890f0"
            text subtitle xalign 0.5 size 22 color "#aaaaaa"
            text "（点击继续）" xalign 0.5 size 16 color "#666666"

################################################################################
# 界面：Demo 结束卡
################################################################################
screen demo_end_screen():
    frame:
        xalign 0.5
        yalign 0.5
        padding (100, 70)
        background Solid("#000000cc")
        vbox:
            spacing 30
            text "Demo  终" xalign 0.5 size 36 color "#e8c87a"
            text "欲知后事如何，请听下回分解。" xalign 0.5 size 24 color "#ccb98a"
            null height 10
            text "感谢游玩《温灼》Demo版" xalign 0.5 size 18 color "#888888"
            text "本作目前仍在制作中，敬请期待正式版。" xalign 0.5 size 16 color "#666666"
            null height 6
            text "（点击退出）" xalign 0.5 size 14 color "#555555"
