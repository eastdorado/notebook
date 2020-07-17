#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @Product: PyCharm
#  @Project: python
#  @File    : majing.py
#  @Author  : big
#  @Email   : shdorado@126.com
#  @Time    : 2020/6/26 13:16
#  功能：

import copy
import sys

from utilities import Utils


class DataMj(object):
    LINE = str(sys._getframe().f_lineno)

    # self.tiles_dot = []  # 饼子
    # self.tiles_bamboo = []  # 条子
    # self.tiles_character = []  # 万子
    # self.tiles_wind = ['东风', '南风', '西风', '北风']    # 番子： the honor tiles (dragon+wind)
    # self.tiles_dragon = ['红中', '发财', '白板']  # 中发白：red dragon、green dragon、white dragon
    # self.tiles = (11, 12, 13, 14, 15, 16, 17, 18, 19,  # 万 各4张
    #               11, 12, 13, 14, 15, 16, 17, 18, 19,
    #               11, 12, 13, 14, 15, 16, 17, 18, 19,
    #               11, 12, 13, 14, 15, 16, 17, 18, 19,
    #               21, 22, 23, 24, 25, 26, 27, 28, 29,  # 饼 各4张
    #               21, 22, 23, 24, 25, 26, 27, 28, 29,
    #               21, 22, 23, 24, 25, 26, 27, 28, 29,
    #               21, 22, 23, 24, 25, 26, 27, 28, 29,
    #               31, 32, 33, 34, 35, 36, 37, 38, 39,  # 条 各4张
    #               31, 32, 33, 34, 35, 36, 37, 38, 39,
    #               31, 32, 33, 34, 35, 36, 37, 38, 39,
    #               31, 32, 33, 34, 35, 36, 37, 38, 39,
    #               41, 42, 43, 44, 45, 46, 47,  # 东南西北 中发白 各4张
    #               41, 42, 43, 44, 45, 46, 47,
    #               41, 42, 43, 44, 45, 46, 47,
    #               41, 42, 43, 44, 45, 46, 47,
    #               51, 52, 53, 54, 55, 56, 57, 58)  # 春夏秋冬，梅兰菊竹 各1张
    # 数据格式:类型=value/10, 数值=value%10
    # self.majmap = {"0": "一万", "1": "二万", "2": "三万", "3": "四万", "4": "五万",
    #                "5": "六万", "6": "七万", "7": "八万", "8": "九万",
    #                "10": "一饼", "11": "二饼", "12": "三饼", "13": "四饼", "14": "五饼",
    #                "15": "六饼", "16": "七饼", "17": "八饼", "18": "九饼",
    #                "20": "一条", "21": "二条", "22": "三条", "23": "四条", "24": "五条",
    #                "25": "六条", "26": "七条", "27": "八条", "28": "九条",
    #                "30": "东风", "31": "南风", "32": "西风", "33": "北风", "34": "红中",
    #                "35": "发财", "36": "白板",
    #                "40": "春", "41": "夏", "42": "秋", "43": "冬", "44": "梅",
    #                "45": "兰", "46": "菊", "47": "竹"}

    g_tile_ids = (0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,  # 万
                  0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19,  # 筒
                  0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29,  # 条
                  0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37,  # 东南西北，中发白
                  0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48)  # 春夏秋冬，梅兰菊竹

    g_tile_names = ("一万", "二万", "三万", "四万", "五万", "六万", "七万", "八万", "九万",
                    "一饼", "二饼", "三饼", "四饼", "五饼", "六饼", "七饼", "八饼", "九饼",
                    "一条", "二条", "三条", "四条", "五条", "六条", "七条", "八条", "九条",
                    "东风", "南风", "西风", "北风", "红中", "发财", "白板",
                    "春", "夏", "秋", "冬", "梅", "兰", "菊", "竹")

    @staticmethod
    def name_is(index):
        ret = ''
        if -1 < index < 42:  # 合法的才显示，非法的忽略
            ret = DataMj.g_tile_names[index]
            # print(index, ret)
        return ret

    @staticmethod
    def print_list_names(cards):
        if not isinstance(cards, list) and len(cards) == 0:  # 合法的才显示，非法的忽略
            print('print_list:非法的 cards')
            return
        tmp = []
        for each in cards:
            if DataMj.is_valid(each):
                tmp.append(DataMj.name_is(DataMj.value2index(each)))
            else:
                print('print_list:非法的 id %#x' % each)
        print(tmp)

    @staticmethod
    def creat_cards_by_names(ll):
        if not ll:  # 合法的才显示，非法的忽略
            return
        tmp = []
        for each in ll:
            ret = DataMj.name2id(each)
            # ret = DataMj.name_is(DataMj.value2index(each))
            if ret:
                tmp.append(ret)

        # print(tmp)
        return tmp

    @staticmethod
    def value2index(tile_id=0x00):
        """
        通过牌的 name和 pic 获得索引和名称
        :param tile_id:
        :return:
        """

        index = -1

        # if tile_id < 1 or tile_id > 0x48:
        #     return index - 1
        if DataMj.is_valid(tile_id):
            rank = tile_id & 0x0F  # 获得牌面的大小

            if tile_id < 0x31:
                # print('value = ', value)
                if 0 < rank < 10:
                    color = tile_id >> 4  # 获得牌的花色/类型
                    index = color * 9 + rank - 1  # * 9
                    # index = (color << 3) + color + value  # * 9
            elif tile_id < 0x38:
                index = 26 + rank
            elif 0x40 < tile_id:
                index = 33 + rank

        # print("%#x, %d" % (tile_id, index))
        return index

    # @staticmethod
    # def index2value(index):
    #     tile_name = ((index // 9) << 4) | (index % 9)
    #     return tile_name

    @staticmethod
    # id 有效性判断
    def is_valid(card_id):
        return card_id in DataMj.g_tile_ids

    @staticmethod
    # 获得牌的花色
    def get_suit(card_id):
        ret = None
        if DataMj.is_valid(card_id) and card_id < 0x30:  # 非字牌、花牌
            ret = card_id & 0x00F0  # 花色(配牌) 筒、条、万
        return ret

    @staticmethod
    # 获得牌的数字
    def get_rank(card_id):
        ret = None
        if DataMj.is_valid(card_id) and card_id < 0x30:  # 非字牌、花牌
            ret = card_id & 0x000F  # 获得牌面的大小 一~九
        return ret

    @staticmethod
    def id2name(tile_id):
        return DataMj.name_is(DataMj.value2index(tile_id))

    @staticmethod
    def name2id(name):
        return DataMj.g_tile_ids[DataMj.g_tile_names.index(name)]

    @staticmethod
    def test():
        # for i in range(-2, 0x50):
        #     # index = (DataMj.value2index(i))
        #     # print('%#x' % i, index, DataMj.name_is(index))
        #     print(DataMj.id2name(i))

        for each in DataMj.g_tile_names:
            print(DataMj.name2id(each))


class MaJing(object):
    def __init__(self, parent=None):
        # noinspection PyArgumentList
        super(MaJing, self).__init__()
        self.parent = parent

        # 牌局的总体参数
        self.tiles_count = 136  # 麻将牌的总数 144, 136, 108
        # self.delay = 10  # 叫牌后的停顿时间
        self.player_names = ('东座', '南座', '西座', '北座')
        self.dealer = 1  # 庄家方位 0：东 1：南，1始终是本家，
        self.dice = 99  # 骰子  points 点数    cheat 抽老千
        self.lots = 0  # 出牌的手数，可以判断各人打出的牌数
        self.speaker = None  # 目前的出牌者
        self.hot_card = None  # 目前的出牌

        self.oker = None  # 鬼牌，钻石牌
        # self.tile_ejected = None  # 弹起的牌
        # self.tile_shadow = None  # 本家叫/热牌的影子牌

        self.round = []  # 一圈/一局的暗牌, 仅有牌号和标志位(0:正常 1:明牌 2:牌卡弹出)
        self.card_players = [[0] * 13 for i in range(4)]  # 四家的牌面最多18张，每张牌含牌号
        # # 每张牌的状态，0:普通牌，1:碰牌，2:吃牌，3:明杠，4:绕杠 5:暗杠

        # self.card_ground = [[0], [0], [0], [0]]  # 四家落地牌，各家桌上废牌
        self.dark_cards = []  # 暗牌，除自己手牌和落地牌外的看不见的牌

        self.para = [10, 2, 1]  # 计算每张牌的分值
        self.scale = 50

        self.begin = True
        self.winning = False  # 已胡牌
        self.can_discard = False  # 本家可以出牌否

    # 洗牌，砌牌，全部 ID
    def shuffling(self):
        tmp = []
        for i in range(4):
            tmp.extend(DataMj.g_tile_ids[0:27])
            if self.tiles_count > 108:
                tmp.extend(DataMj.g_tile_ids[27:34])
        if self.tiles_count > 136:
            tmp.extend(DataMj.g_tile_ids[34:42])

        self.dark_cards = sorted(tmp)  # 都算暗牌

        self.round.clear()
        # 随机洗牌
        for i in range(self.tiles_count):
            index = Utils.rand_int(0, self.tiles_count - i - 1)
            self.round.append(tmp[index])
            tmp.pop(index)

        # DataMj.print_list_names(self.round)
        # print(sorted(self.round))
        # self.round.sort() # 不返回任何东西
        # print(self.round)
        # print(self.card_players)

    # 起牌
    def deal(self):
        """
        抓牌顺时针抓,打牌逆时针打
        :return:
        """
        if self.tiles_count < 54:  # 不够起牌的
            return

        self.dealer %= 4  # 轮流坐庄 4人麻将

        # 庄家掷骰子找到二次掷骰人，并确定开门方向
        # die1 = random.randint(1, 12)
        die_1 = Utils.rand_int(1, 12)
        door = (self.dealer + die_1 - 1) % 4  # 开门方向
        # 二次掷骰子
        # die2 = random.randint(1, 12)
        die_2 = Utils.rand_int(1, 12)
        dice = (door + 1) * 34 - die_2 * 2
        # zero = dice % self.tiles_count      # 开始摸牌的位置
        new_round = self.round[dice:]
        new_round.extend(self.round[:dice])
        self.round = new_round  # 重新起算
        # print(len(self.round))

        self.lots = 0
        # 给玩家发牌，顺时针抓牌
        for k in range(3):  # 发三次牌，每人每次拿连续的4张
            for i in range(4):
                player_id = (i + self.dealer) % 4  # 循环坐庄
                for j in range(4):
                    index = j + 4 * k  # 槽位
                    # player_id 也代表卡牌类型
                    self.card_players[player_id][index] = self.round.pop(0)  # 牌号，兼做排序用
                    self.lots += 1

        # 每人再模一张，叫牌空置
        for i in range(4):
            player_id = (i + self.dealer) % 4  # 从庄家开始
            self.card_players[player_id][12] = self.round.pop(0)  # 返回弹出值
            self.lots += 1

            # for j in range(13, 18):
            #     self.card_players[player_id][j] |= 0xff  # 叫牌，确保排在最后，每台不用清零

            self.card_players[player_id].sort()  # 排序

        # 庄家不多摸，现在从庄家开始摸牌再发牌
        self.speaker = self.dealer  # 目前的摸/出牌者

        # for i in range(4):
        #     print(self.card_players[i])
        # DataMj.print_list_names(self.card_players[i])

    # 摸牌
    def draw(self):
        """
        检测到哪家摸牌了，接着叫牌，也就是出牌
        :return:
        """
        while True:  # 逆时针打牌
            if len(self.round) < 1 or self.winning:  # 荒牌或胡牌
                break

            self.speaker %= 4  # 确保不溢出
            player_cards = self.card_players[self.speaker]

            card_id = self.round.pop(0)  # 进张
            self.lots += 1
            # print(f'{self.player_names[self.speaker]}摸牌，得 {DataMj.id2name(card_id)}')

            player_cards.append(card_id)  # 进张了

            player_cards.sort()
            if self.match(player_cards):  # 判断自摸没有
                self.winning = True
                continue
            else:
                if self.kong(card_id, True):  # 判断杠上开花没有
                    continue
                else:  # 仅杠牌后继续出牌，或没有杠牌后正常出牌
                    index = self.cards_score(player_cards)  # 分值最小的牌，需要打出去
                    self.hot_card = player_cards[index]
                    player_cards.pop(index)  # 打出去了

                    i = self.dark_cards.index(self.hot_card)
                    self.dark_cards.pop(i)  # 变成明牌

            # print(f'{self.player_names[self.speaker]}出牌，抛出 {DataMj.id2name(self.hot_card)}')

            if self.ting():
                continue
            elif self.kong(self.hot_card):
                continue
            elif self.pung():
                continue
            elif self.chow():
                continue
            else:
                self.speaker += 3  # 右手是下家，让下家摸牌、出牌

        if self.winning:
            self.win(self.speaker)
        else:
            print('荒牌，流局了!')

    # 和、胡
    def win(self, speaker):
        print(f'{self.player_names[speaker]} \033[7;32m胡牌\033[7;32m\033[0m !\033[0m')
        DataMj.print_list_names(self.card_players[speaker])

    # 胡牌判断，cardList: 是手上的牌，需要从小到大排列
    def match(self, player_cards, is_win=False):
        # 递归算法：配对成功的弹出，一直到手上牌都弹出为止
        if len(player_cards) == 0 and is_win:
            return True

        rst = False
        # AA
        if not is_win and len(player_cards) >= 2 and player_cards[0] == player_cards[1]:
            list1 = [] + player_cards
            list1.pop(0)
            list1.pop(0)
            rst = self.match(list1, True)

        # AAA
        if not rst and len(player_cards) >= 3 and player_cards[0] == player_cards[1] == player_cards[2]:
            list1 = [] + player_cards
            list1.pop(0)
            list1.pop(0)
            list1.pop(0)
            rst = self.match(list1, is_win)

        # AAAA
        if not rst and len(player_cards) >= 4 and \
                player_cards[0] == player_cards[1] == player_cards[2] == player_cards[3]:
            list1 = [] + player_cards
            list1.pop(0)
            list1.pop(0)
            list1.pop(0)
            list1.pop(0)
            rst = self.match(list1, is_win)

        # ABC
        if not rst and len(player_cards) >= 3:
            list1 = []
            a = player_cards[0]
            if a > 0x30:  # 风、龙、花牌
                return rst

            b = False
            c = False
            for i in range(1, len(player_cards)):
                if not b and player_cards[i] == a + 1:
                    b = True
                elif not c and player_cards[i] == a + 2:
                    c = True
                else:
                    list1.append(player_cards[i])

            if b and c:
                rst = self.match(list1, is_win)

        return rst

    def cards_score(self, player_cards, print_it=False):
        # player_cards：手上的牌
        # x+/-3:0   x+/-2:10   x+/-1:20   x:100
        # xxxx:400   xxx:300   xx:200   x x+1 x+2:130   x x+1:120   x x+2:110

        scores = []

        # dark = []+self.dark_cards  # 每家的暗牌不一样，要减去自己牌。 未出现过的牌
        dark = copy.deepcopy(self.dark_cards)  # 深拷贝
        for each in player_cards:
            if each in dark:
                dark.pop(dark.index(each))
        # dark = list(set(self.dark_cards) - set(player_cards))
        # print('cha', len(dark), len(self.dark_cards), len(player_cards))
        # print(dark, '\n', self.dark_cards, '\n', player_cards)

        for c in player_cards:
            score = 0
            for cc in player_cards:
                gap = abs(cc - c)
                if c > 0x30:
                    if gap == 0:  # 风、龙、花牌 成双
                        score += self.para[gap] * self.scale
                else:
                    if gap < 3:
                        score += self.para[gap] * self.scale

            for cc in dark:  # 未出现的牌中还有比较多的A，B,那么凑出AAA或ABC牌的几率加大了
                gap = abs(cc - c)
                if c > 0x30:
                    if gap == 0:  # 风、龙、花牌 成双
                        score += self.para[gap]
                else:
                    if gap < 3:
                        score += self.para[gap]

            scores.append(score)

        if print_it:
            print(scores)

        return scores.index(min(scores))

    # 听牌
    def ting(self):
        for i in range(self.speaker + 3, self.speaker, -1):  # 从下家开始
            speaker = i % 4
            new_cards = self.card_players[speaker]
            new_cards.append(self.hot_card)
            new_cards.sort()
            if self.match(new_cards):  # 放炮了
                print(f"{self.player_names[self.speaker]} \033[1;35m放炮\033[1;35m\033[0m 于 \033[0m"
                      f"\033[5;31m{DataMj.id2name(self.hot_card)}\033[5;31m\033[0m ! \033[0m")
                self.speaker = speaker
                self.winning = True  # 放炮胡
                return True
            else:
                new_cards.pop(new_cards.index(self.hot_card))  # 再次把热牌弹出去

        return False

    # 杠
    def kong(self, card_id, is_self_drawn=False):
        """
        明杠：①玩家手中有三张一样的牌，其它玩家打出了第四张一样的牌，玩家可以选择杠牌，这种叫做直杠，只收一家的筹码；
        ②玩家手上已经碰了三张一样的牌，当玩家自己又摸起了第四张一样的牌，这时可以选择杠牌，这种叫做绕杠，这种杠牌可以收三家的筹码。
        暗杠：玩家有四张一样的牌就可以拿出来进行下雨。这样的杠牌可以收三家的筹码。
        :param card_id:
        :param is_self_drawn: 自摸时的判断
        :return:
        """

        if is_self_drawn:  # 自己摸的牌， 可以绕杠和暗杠
            tmp = []  # 已经加了新牌
            state = -1

            cards = self.card_players[self.speaker]
            for i in range(14):
                if card_id == cards[i]:
                    tmp.append(i)
                    st = cards[i] & 0x0F00  # 每张牌的状态，0:普通牌，1:碰牌，2:吃牌，3:明杠，4:绕杠 5:暗杠
                    state = st if st > state else state

            if len(tmp) > 3:  # 这里要不要杠是个杠的策略问题，再细化
                if state == 4:
                    print(f"\033[0m{self.player_names[self.speaker]}\033[0m \033[1;33m绕杠\033[1;33m "
                          f"\033[5;32m{DataMj.id2name(card_id)}\033[5;32m \033[0m!\033[0m")
                else:
                    print(f"\033[0m{self.player_names[self.speaker]}\033[0m \033[1;35m暗杠\033[1;35m "
                          f"\033[5;32m{DataMj.id2name(card_id)}\033[5;32m \033[0m!\033[0m")
                    # print(f"{self.player_names[self.speaker]} 暗杠 {DataMj.id2name(card_id)}！")

                for each in tmp:
                    each |= 0x0400 if state == 1 else 0x0500  # 4:绕杠 5:暗杠

                tail = self.round.pop()  # 屁股上摸了一张牌
                cards.append(tail)

                # 判断是否杠上开花
                cards.sort()
                if self.match(cards):
                    print(f"摸到 {DataMj.id2name(tail)}，杠上开花！")
                    self.winning = True  # 杠上开花
                    return True
                else:  # 重新出牌,流程在上面
                    pass
            return False  # 没有杠后胡牌，就继续出牌，而因为是自摸，所以发牌者没有变

        else:  # 别人打出的热牌，可以直杠/明杠
            for i in range(self.speaker + 3, self.speaker, -1):  # 从下家开始
                tmp = [card_id]
                state = -1

                speaker = i % 4
                cards = self.card_players[speaker]

                for j in range(13):
                    if card_id == cards[j]:
                        tmp.append(j)
                        st = cards[j] & 0x0F00  # 每张牌的状态，0:普通牌，1:碰牌，2:吃牌，3:明杠，4:绕杠 5:暗杠
                        state = st if st > state else state

                if len(tmp) > 3 and state == 0:  # 这里要不要杠是个杠的策略问题，再细化
                    print(f"\033[0m{self.player_names[speaker]}\033[0m \033[1;34m明杠\033[1;34m "
                          f"\033[0m{self.player_names[self.speaker]} 的 \033[0m"
                          f"\033[5;32m{DataMj.id2name(self.hot_card)}\033[5;32m \033[0m!\033[0m")
                    self.speaker = speaker  # 杠后成为当前发牌者

                    for each in tmp:
                        each |= 0x0300  # 只能是3:明杠

                    cards.append(card_id)  # 加入热牌，且排序
                    tail = self.round.pop()  # 屁股上摸一张牌
                    cards.append(tail)

                    # 判断是否杠上开花
                    cards.sort()
                    if self.match(cards):
                        print(f"摸到{DataMj.id2name(tail)}，杠上开花！")
                        self.winning = True  # 杠上开花
                    else:  # 杠牌后继续出牌
                        index = self.cards_score(cards)  # 分值最小的牌，需要打出去
                        self.hot_card = cards[index]
                        cards.pop(index)  # 打出去了

                        i = self.dark_cards.index(self.hot_card)
                        self.dark_cards.pop(i)  # 变成明牌

                    return True  # 杠牌后就要重新确定发牌者

            return False  # 否则发牌者不变，继续后面的判断

    # 碰
    def pung(self):
        # 碰碰胡在ting()里处理过了

        for i in range(self.speaker + 3, self.speaker, -1):  # 从下家开始
            tmp = [self.hot_card]

            speaker = i % 4
            cards = self.card_players[speaker]

            for j in range(13):
                if self.hot_card == cards[j]:
                    tmp.append(j)

            if len(tmp) > 2:  # 这里要不要碰是个策略问题，再细化
                print(f"\033[0m{self.player_names[speaker]}\033[0m \033[1;31m碰\033[1;31m "
                      f"\033[0m{self.player_names[self.speaker]} 的 \033[0m"
                      f"\033[5;32m{DataMj.id2name(self.hot_card)}\033[5;32m \033[0m!\033[0m")
                self.speaker = speaker  # 碰后成为当前发牌者

                for each in tmp:
                    each |= 0x0100  # 1:碰牌   每张牌的状态，0:普通牌，1:碰牌，2:吃牌，3:明杠，4:绕杠 5:暗杠

                cards.append(self.hot_card)  # 加入热牌，且排序
                cards.sort()

                # 判断是否碰碰胡
                # if self.match():
                #     print("碰碰胡", DataMj.id2name(tail))
                #     return True
                # else:  # 杠牌后继续出牌
                index = self.cards_score(cards)  # 分值最小的牌，需要打出去
                self.hot_card = cards[index]
                cards.pop(index)  # 打出去了

                i = self.dark_cards.index(self.hot_card)
                self.dark_cards.pop(i)  # 变成明牌

                return True  # 重新选择了发牌者

        return False  # 轮流完了，还是没有碰掉，则继续吃的判断

    # 吃
    def chow(self, cards=None):
        """
        左边是上家，坐你右边的是下家，坐你对面的是对家
        只能吃上家的牌
        :param hot_ID:
        :return:
        """
        if self.hot_card > 0x30:  # 字牌、花牌不能吃
            return False

        return False
        # speaker = (self.speaker + 3) % 4  # 右手下家可以吃热牌
        # cards = self.card_players[speaker]

        cbd_list = []  # 手牌里与热牌同类型的所有牌
        sequences = []  # 顺子集合        一组 Meld 	一个顺子、刻子或杠子

        rank = DataMj.get_rank(self.hot_card)  # 牌面的大小 一~九
        suit = DataMj.get_suit(self.hot_card)  # 花色(配牌) 筒、条、万
        print(rank, '%#x' % suit, '%#x' % self.hot_card, DataMj.id2name(self.hot_card))
        # print(DataMj.print_list_names(cards))

        for each in cards:
            if suit == DataMj.get_suit(each):
                cbd_list.append(each)

        size = len(cbd_list)
        DataMj.print_list_names(cbd_list)

        if size >= 2:
            for i in range(0, size - 1):
                if DataMj.get_rank(cbd_list[i]) == rank - 2 and DataMj.get_rank(cbd_list[i + 1]) == rank - 1:
                    sequences.append([cbd_list[i], cbd_list[i + 1], self.hot_card])
                if DataMj.get_rank(cbd_list[i]) == rank - 1 and DataMj.get_rank(cbd_list[i + 1]) == rank + 1:
                    sequences.append([cbd_list[i], self.hot_card, cbd_list[i + 1]])
                if DataMj.get_rank(cbd_list[i]) == rank + 1 and DataMj.get_rank(cbd_list[i + 1]) == rank + 2:
                    sequences.append([self.hot_card, cbd_list[i], cbd_list[i + 1]])

        # 假设吃B，已有ABC
        if size >= 3:
            for i in range(1, size - 1):
                if DataMj.get_rank(cbd_list[i - 1]) == rank - 1 and \
                        DataMj.get_rank(cbd_list[i]) == rank and \
                        DataMj.get_rank(cbd_list[i + 1]) == rank + 1:
                    sequences.append([cbd_list[i - 1], self.hot_card, cbd_list[i + 1]])

        # 假设吃B，已有ABBC
        if size >= 4:
            for i in range(1, size - 2):
                if DataMj.get_rank(cbd_list[i - 1]) == rank - 1 and \
                        DataMj.get_rank(cbd_list[i]) == rank and \
                        DataMj.get_rank(cbd_list[i + 2]) == rank + 1:
                    sequences.append([cbd_list[i - 1], self.hot_card, cbd_list[i + 1]])

        # 假设吃B，已有ABBBC
        if size >= 5:
            for i in range(1, size - 3):
                if DataMj.get_rank(cbd_list[i - 1]) == rank - 1 and \
                        DataMj.get_rank(cbd_list[i]) == rank and \
                        DataMj.get_rank(cbd_list[i + 3]) == rank + 1:
                    sequences.append([cbd_list[i - 1], self.hot_card, cbd_list[i + 1]])

        # 假设吃B，已有ABBBBC
        if size >= 6:
            for i in range(1, size - 4):
                if DataMj.get_rank(cbd_list[i - 1]) == rank - 1 and \
                        DataMj.get_rank(cbd_list[i]) == rank and \
                        DataMj.get_rank(cbd_list[i + 4]) == rank + 1:
                    sequences.append([cbd_list[i], self.hot_card, cbd_list[i + 1]])

        if len(sequences) > 0:
            print('所有顺子：', len(sequences), sequences)
            for each in sequences:
                DataMj.print_list_names(each)

        return False


def main():
    # DataMj.test()

    mahing = MaJing()
    mahing.shuffling()
    mahing.deal()
    mahing.draw()

    # cards = [0x01, 0x01, 0x24, 0x23, 0x22, 0x2, 0x3, 0x04, 0x33, 0x33, 0x33, 0x17, 0x19, 0x18]
    # names = ['一饼', '二饼', '三万', '三万', '四万', '四万', '四条', '五条', '六条', '七条', '七条', '八条', '八条']
    # mahing.hot_card = DataMj.name2id('三条')
    # print(mahing.hot_card, DataMj.id2name(mahing.hot_card))
    #
    # cards = DataMj.creat_cards_by_names(names)
    # cards.sort()
    # DataMj.print_list_names(cards)
    # mahing.chow(cards)
    #
    # mahing.cards_score(cards, True)
    # print(mahing.match(cards))

    # i = DataMj.g_tile_ids[9]
    # print(type(i), sys.getsizeof(i))


if __name__ == '__main__':
    main()
