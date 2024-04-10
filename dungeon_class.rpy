class DungeonEvent:
    def __init__(self, _id, content, status):
        """

        :param content: 具体内容
        :param status: 0 不可触发 非0 可触发
        """
        self.id = _id
        self.content = content
        self.status = status


class DungeonGrid:
    def __init__(self, _id, pos, event, status):
        """

        :param pos:相对位置xy坐标0~1
        :param event: DungeonEvent
        :param status: 0 gray 已探测 无交互; 1 green 已探测 安全 可交互; 2 red 已探测 危险 可交互; 3 blue 连接其他地图; 4 未探测
        """
        self.id = _id
        self.pos = pos
        self.event = event
        self.status = status
        self.link_w = None
        self.link_a = None
        self.link_s = None
        self.link_d = None


class DungeonLink:
    def __init__(self, _id, link_grid_ids, event, status):
        """

        :param link_grid_ids: 所连接的两个dungeon grid的id
        :param event: DungeonEvent
        :param status: 0 不通 1 通 可能会由dungeon event或剧情等改变
        """
        self.id = _id
        self.link_grid_ids = link_grid_ids
        self.event = event
        self.status = status


class Dungeon:
    def __init__(self, name, bg, intro, dungeon_grid_list, dungeon_link_list, dungeon_event_list):
        """

        :param name:
        :param bg:
        :param intro:
        :param dungeon_grid_list:
        :param dungeon_link_list:
        :param dungeon_event_list:
        """
        self.name = name
        self.bg = bg
        self.intro = intro
        self.grid_list = dungeon_grid_list
        self.link_list = dungeon_link_list
        self.event_list = dungeon_event_list
