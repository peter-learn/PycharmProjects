# coding=utf-8
# 当前版本2.3
# =======================V2.3=================
# 2021.9.7
# 1、修复胜利显示对应玩家的功能 √
# 2、修复食物太小不明显的问题 √
# 3、修复胜利条件文字、图像显示不全的问题 √
# 4、背景图片、ipad控制按键修改
# =======================V2.1=================
# 1、修复分数显示、长度显示字体大小不能随地图大小变化的问题 √
# 2、修复ipad按键触控范围bug √
# 3、增加图片接口封装 √
# 4、复活起始位置修改 √
# 5、去除开始界面 √
# 6、增加ipad按键图片 √
# 7、修复障碍物图片显示bug（列表里面写1和2显示的是相同的障碍） √
# 8、修复双人模式下蛇的身体一样的bug √
# 9、修复使用触屏控制后，在此使用键盘时恒定朝一侧前进的bug √
# =======================V2.0=================
# 1、去除背景音乐
# 2、修改矩阵模式
# =======================V1.5=================
# 1、增加背景音乐
# 2、增加ipad控制

import sys
import random
import pygame
import math

# import xeslib


pygame.init()
clock = pygame.time.Clock()
# 初始化窗口大小
WIDTH, HEIGHT = 900, 900
# 方格大小
SQUARE = 100
# ipad按键开关
ipad_control_switch = False

# 用到的图片和音乐相对路径
background_image_filename = 'bg1.png'
grass_image_filename = 'grass.png'
head1_image_filename = 'snake_head1.png'
head2_image_filename = 'snake_head2.png'
body1_image_filename = 'snake_body1.png'
body2_image_filename = 'snake_body2.png'
food_image_filename = ['food-1.png', 'food-2.png', 'food-3.png', 'food-4.png', 'food-5.png', 'food-6.png',
                       'food-7.png', 'food-8.png']
map1_image_filename = 'map1.png'
map2_image_filename = 'map2.png'
map3_image_filename = 'map3.png'
boom_image_filename = 'boom.png'
player_image_filename = 'ipad_control1.png'
gameover1_image_filename = 'gameover1.png'
gameover2_image_filename = 'gameover2.png'


# 重复播放背景音乐
# pygame.mixer.music.load(background_music_filename)
# pygame.mixer.music.play(-1)

def set_map(seq):
    # 全地图所有位置
    global map_pos, WIDTH, HEIGHT, screen, crash_list1, food_list, crash_list2, crash_list3
    map_pos = seq
    # 获得列表中元素的最长长度最为宽
    list_len = []
    for n in map_pos:
        list_len.append(len(n))
    # print("list_len:",list_len)
    WIDTH = max(list_len) * SQUARE
    HEIGHT = len(map_pos) * SQUARE
    print("宽：", WIDTH, "高：", HEIGHT)
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)
    # 障碍物1位置
    crash_list1 = []
    # 障碍物2位置
    crash_list2 = []
    # 障碍物3位置
    crash_list3 = []
    # 食物位置
    food_list = []
    try:
        # 遍历时先竖后横，j是y坐标，i是x坐标
        for i in range(len(map_pos)):
            for j in range(max(list_len)):
                if map_pos[i][j] == 3:
                    crash_list3.append((j * SQUARE, i * SQUARE))
                if map_pos[i][j] == 2:
                    crash_list2.append((j * SQUARE, i * SQUARE))
                if map_pos[i][j] == 1:
                    crash_list1.append((j * SQUARE, i * SQUARE))
                if map_pos[i][j] == 0:
                    food_list.append((j * SQUARE + int(SQUARE / 3), i * SQUARE + int(SQUARE / 3)))
    except Exception as e:
        print(e, "小列表长度不统一，请检查列表长度")

    background_image_filename = 'bg1.png'
    # 加载背景图片
    background = pygame.image.load(background_image_filename).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    map_image1 = pygame.image.load(map1_image_filename)
    map_image1 = pygame.transform.scale(map_image1, (SQUARE, SQUARE))

    map_image2 = pygame.image.load(map2_image_filename)
    map_image2 = pygame.transform.scale(map_image2, (SQUARE, SQUARE))

    try:
        map_image3 = pygame.image.load(map3_image_filename)
        map_image3 = pygame.transform.scale(map_image3, (SQUARE, SQUARE))
    except Exception as e:
        pass

    # 显示障碍
    for i in crash_list1:
        screen.blit(map_image1, (i[0], i[1]))

    # 显示障碍
    for i in crash_list2:
        screen.blit(map_image2, (i[0], i[1]))
    try:
        for i in crash_list3:
            screen.blit(map_image3, (i[0], i[1]))
    except Exception as e:
        pass
    # print()
    pygame.display.update()


def load(head_image, body_image):
    global HeadImg, BodyImg, map_image1, map_image2, map_image3, grass_image_filename, head1_image_filename, head2_image_filename, body1_image_filename, body2_image_filename, food_image_filename, boom_image_filename, player_image_filename, gameover1_image_filename, gameover2_image_filename, background, ipad_control, over1, over2

    HeadImg = pygame.image.load(head_image).convert_alpha()
    HeadImg = pygame.transform.scale(HeadImg, (int(SQUARE / 2), int(SQUARE / 2)))
    BodyImg = pygame.image.load(body_image).convert_alpha()
    BodyImg = pygame.transform.scale(BodyImg, (int(SQUARE / 2), int(SQUARE / 2)))

    # 加载背景图片
    background = pygame.image.load(background_image_filename).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    ipad_control = pygame.image.load(player_image_filename)
    ipad_control = pygame.transform.scale(ipad_control, (WIDTH, HEIGHT))
    # 墙壁图片
    map_image1 = pygame.image.load(map1_image_filename)
    map_image1 = pygame.transform.scale(map_image1, (SQUARE, SQUARE))

    map_image2 = pygame.image.load(map2_image_filename)
    map_image2 = pygame.transform.scale(map_image2, (SQUARE, SQUARE))

    try:
        map_image3 = pygame.image.load(map3_image_filename)
        map_image3 = pygame.transform.scale(map_image3, (SQUARE, SQUARE))
    except Exception as e:
        pass

    # 加载结束图片
    over1 = pygame.image.load(gameover1_image_filename).convert_alpha()
    over1 = pygame.transform.scale(over1, (WIDTH, HEIGHT))
    over2 = pygame.image.load(gameover2_image_filename).convert_alpha()
    over2 = pygame.transform.scale(over2, (WIDTH, HEIGHT))


# 定义一个按钮类,判断has的坐标是否在给定坐标内
class Button():
    def __init__(self, x1, x2, y1, y2):
        self.right = x2
        self.left = x1
        self.bottom = y2
        self.top = y1

    def has(self, pos):
        if self.right >= pos[0] >= self.left and self.bottom >= pos[1] >= self.top:
            return True
        else:
            return False


# 用于返回食物出现的位置
def foodpos():
    global map_pos, food_list
    pos_final = random.choice(food_list)
    return pos_final[0], pos_final[1]


class Snake():
    '''
    蛇类，用于控制蛇的移动和碰撞检测以及输赢状态
    '''

    def __init__(self, pos, speed):
        '''
        head_image:头部图片路径
        pos:头部初始位置
        speed:每秒前进的速度
        body_image:身体图片路径
        '''
        self.head = HeadImg
        self.pos = pos
        self.speed = speed
        self.body_image = BodyImg
        self.rotation = 0
        self.path = []  # 头部走过的路径(坐标)
        self.x = 0  # 当前头部的x坐标
        self.y = 0  # 当前头部的y坐标
        self.is_dead = False  # 死亡状态判断
        self.is_win = False  # 输赢状态判断
        self.length = snake_start  # 初始身体长度
        self.body = []  # 所有身体的坐标
        self.posx = pos[0]
        self.posy = pos[1]
        self.dead_flag = False

    def update(self, time_passed_seconds=0.1):
        '''
        更新位置
        time_passed_seconds:间隔时间(秒)
        '''
        if self.is_dead or self.is_win:
            return
        # 计算前进方向
        x = math.sin(self.rotation * math.pi / 180)
        y = math.cos(self.rotation * math.pi / 180)
        # 转换为单位速度向量
        heading = [x, y]
        self.posx += -heading[0] * self.speed * time_passed_seconds
        self.posy += -heading[1] * self.speed * time_passed_seconds
        # 穿墙
        if self.posx > WIDTH:
            self.posx = 0
        if self.posx < 0:
            self.posx = WIDTH
        if self.posy > HEIGHT:
            self.posy = 0
        if self.posy < 0:
            self.posy = HEIGHT
        # 获取旋转后的蛇头
        rotated_sprite = pygame.transform.rotate(self.head, self.rotation)
        # 获得长宽
        self.w, self.h = rotated_sprite.get_size()
        # 绘制蛇的坐标
        self.x = self.posx - self.w / 2
        self.y = self.posy - self.h / 2
        screen.blit(rotated_sprite, (self.x, self.y))
        # 添加移动路径
        pos = (self.x, self.y)
        self.path.append(pos)
        # if len(self.path) > 100:
        #     self.path.pop()
        # 刷新身体
        self.body = []
        sp = int(round(330 / self.speed))
        for i in range(self.length):
            index = (i + 1) * sp + 1
            location = self.path[-min(index, len(self.path))]
            screen.blit(self.body_image, location)
            self.body.append(location)
        le = max(self.length * 200 * 2, 60)
        if len(self.path) > le:
            self.path = self.path[int(-le * 2):]
        # 检测输赢
        self.is_wins()
        self.is_lost()

    def rotation_angle_p1(self, keys, str):
        '''
        玩家1头部的旋转角度
        keys:按下的键
        '''
        if self.is_dead or self.is_win:
            return
        # 根据按键确定x和y的值
        x, y = 0, 0
        # pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d

        if keys[ord('a')] or str == "L":
            y = +1
        if keys[ord('d')] or str == "R":
            y = -1
        if keys[ord('w')] or str == "U":
            x = +1
        if keys[ord('s')] or str == "D":
            x = -1
        # 定义角度导向元祖，根据xy的值确定旋转角度
        directs = ((225, 180, 135), (270, None, 90), (315, 0, 45))
        direct = directs[x + 1][y + 1]
        # 如果没有按下的键就还是原来的角度，否则更新角度
        if direct is None:
            self.rotation = self.rotation
        else:
            self.rotation = direct

    def rotation_angle_p2(self, keys):
        '''
        玩家2头部的旋转角度
        keys:按下的键
        '''
        if self.is_dead or self.is_win:
            return
        # 根据按键确定x和y的值
        x, y = 0, 0
        if keys[ord('j')]:
            y = +1
        if keys[ord('l')]:
            y = -1
        if keys[ord('i')]:
            x = +1
        if keys[ord('k')]:
            x = -1
        # 定义角度导向元祖，根据xy的值确定旋转角度
        directs = ((225, 180, 135), (270, None, 90), (315, 0, 45))
        direct = directs[x + 1][y + 1]
        # 如果没有按下的键就还是原来的角度，否则更新角度
        if direct is None:
            self.rotation = self.rotation
        else:
            self.rotation = direct

    def eat_food(self, pos, is_boom):
        '''
        食物碰撞检测
        pos:食物位置
        is_boom:是否是地雷
        '''
        if self.is_dead or self.is_win:
            return
        # 根据食物位置和蛇头位置检测是否碰撞
        if abs(self.x - pos[0]) < self.w / 1.5 and abs(self.y - pos[1]) < self.h / 1.5:
            if is_boom:
                # 如果是地雷，播放吃地雷音效
                # pygame.mixer.Sound(catboom_music_filename).play()
                # 每次吃地雷减速12，速度有封顶
                if self.speed > 50:
                    self.speed -= 12
            else:
                # 如果是食物，播放吃食物音效
                # pygame.mixer.Sound(cat_music_filename).play()
                # 每次吃食物长度加1，速度减6，速度有封顶
                self.length = self.length + 1
                if self.speed > 50:
                    self.speed -= 6
            return True
        return False

    def crash_map(self):
        for i in (crash_list1 + crash_list2 + crash_list3):
            mapposx, mapposy = i[0], i[1]
            # 使用坐标检测是否碰撞
            if not ((mapposx > (self.x + int(SQUARE / 2))) or ((mapposx + SQUARE) < self.x) or (
                    mapposy > (self.y + int(SQUARE / 2))) or ((mapposy + SQUARE) < self.y)):
                self.dead_flag = True

    # def reset(self,x,y):
    #     self.length = 4
    #     self.posx = x
    #     self.posy = y

    def is_wins(self):
        '''
        判断玩家是否胜利，如果长度大于一定值则胜利
        '''
        if self.length == score_end - 1:
            self.is_win = True
        else:
            self.is_win = False

    def is_lost(self):
        '''
        判断玩家是否死亡，如果长度小于等于0则胜利
        '''
        if self.length <= 0:
            self.is_dead = True
        else:
            self.is_dead = False


FoodImg = []


def load_other():
    global FoodImg, food_image_filename, boom_image_filename
    for i in food_image_filename:
        food_image = pygame.image.load(i).convert_alpha()
        food_image = pygame.transform.scale(food_image, (int(SQUARE / 2), int(SQUARE / 2)))
        FoodImg.append(food_image)
    reduce_image = pygame.image.load(boom_image_filename).convert_alpha()
    reduce_image = pygame.transform.scale(reduce_image, (int(SQUARE / 2), int(SQUARE / 2)))
    FoodImg = [FoodImg, [reduce_image]]


class Food():
    '''
    食物类，用于生成和刷新食物位置
    '''

    def __init__(self, num):
        '''
        food_image:食物图片路径
        '''
        self.num = num
        self.food_image = random.choice(FoodImg[num])
        self.w = int(SQUARE / 2)  # 食物宽度
        self.h = int(SQUARE / 2)  # 食物高度
        self.is_eaten = False  # 食物是否被吃
        self.x, self.y = foodpos()  # 食物刷新x,y坐标

    def reset(self):
        '''
        被吃掉时刷新食物位置
        '''
        if self.is_eaten:
            self.x, self.y = foodpos()
            self.eat = False
            self.food_image = random.choice(FoodImg[self.num])

    def bulid_mini(self):
        '''
        绘制不同种类的食物
        '''
        screen.blit(self.food_image, (self.x, self.y))

    def bulid_img(self):
        '''
        直接通过图片绘制食物
        '''
        screen.blit(self.food_image, (self.x, self.y))


# 设置速度
speed_set = 10


def speed(num=20):
    global speed_set
    speed_set = num


# 设置游戏结束分数
score_end = 24


def end(num=24):
    global score_end
    score_end = num


# 双人模式
double_flag = False


def double():
    global double_flag
    double_flag = True


snake_start = 4


def start(num=5):
    global snake_start
    snake_start = num


def wall_1(name):
    global map1_image_filename
    map1_image_filename = name


def wall_2(name):
    global map2_image_filename
    map2_image_filename = name


def wall_3(name):
    global map3_image_filename
    map3_image_filename = name


def snake_1(name1, name2='snake_body1.png'):
    global head1_image_filename, body1_image_filename
    head1_image_filename = name1
    body1_image_filename = name2


def snake_2(name1, name2='snake_body2.png'):
    global head2_image_filename, body2_image_filename
    head2_image_filename = name1
    body2_image_filename = name2


def boom(name):
    global boom_image_filename
    boom_image_filename = name


def ipad_control():
    global ipad_control_switch
    ipad_control_switch = True


def play():
    global speed_set, double_flag, HeadImg, BodyImg, map_image1, grass_image_filename, head1_image_filename, head2_image_filename, body1_image_filename, body2_image_filename, food_image_filename, boom_image_filename, background, ipad_control, over1, over2
    # 每隔固定时间触发一次事件
    time0 = 0
    time3 = 0
    # 初始化两个玩家
    load(head1_image_filename, body1_image_filename)
    snake_P1 = Snake([SQUARE * 2, HEIGHT - int(SQUARE / 2)], speed_set)
    load(head2_image_filename, body2_image_filename)
    snake_P2 = Snake([SQUARE * 3, HEIGHT - int(SQUARE / 2)], speed_set)
    # 初始化食物和地雷
    load_other()
    food = Food(0)
    food2 = Food(0)
    food3 = Food(0)
    food4 = Food(0)
    food5 = Food(0)
    food6 = Food(0)
    food7 = Food(0)
    food8 = Food(0)
    food9 = Food(0)
    food10 = Food(0)
    food_boom = Food(1)
    # 开始和结束的状态
    end = False
    sat = False
    # 获取字体
    font_size = int(max(WIDTH, HEIGHT) / 35)
    if font_size <= 25:
        font_size = 25
    cur_font = pygame.font.SysFont("SimHei", font_size)
    # 添加系统时钟
    clock = pygame.time.Clock()
    # 加载背景音乐
    # audio = xeslib.playbgMusic("snake.mp3")
    # audio.play()
    # 按键
    left_button = Button(0, int(WIDTH / 3), int(HEIGHT / 3), int(HEIGHT / 3 * 2))
    right_button = Button(int(WIDTH / 3 * 2), WIDTH, int(HEIGHT / 3), int(HEIGHT / 3 * 2))
    up_button = Button(int(WIDTH / 3), int(WIDTH / 3 * 2), 0, int(HEIGHT / 3))
    down_button = Button(int(WIDTH / 3), int(WIDTH / 3 * 2), int(HEIGHT / 3 * 2), HEIGHT)

    go = None
    while True:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            #     sat = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if left_button.has(pos):
                    go = 'L'
                if right_button.has(pos):
                    go = 'R'
                if up_button.has(pos):
                    go = 'U'
                if down_button.has(pos):
                    go = 'D'
            if event.type == pygame.KEYDOWN:
                go = None
            # 游戏结束时按空格键再玩一次
            # if event.key == pygame.K_SPACE and end:
            #     return play()
        screen.blit(background, (0, 0))
        # 如果游戏没开始则显示开始画面
        # if not sat:
        #     screen.blit(ipad_control, (0,0))
        #     pygame.display.update()
        #     continue
        # 间隔时间(秒)
        # time_passed_sec=clock.tick()/1000.0

        if not end:
            # 玩家p1操作
            snake_P1.rotation_angle_p1(pygame.key.get_pressed(), go)
            snake_P1.update()
            snake_P1.crash_map()
            if snake_P1.dead_flag:
                snake_P1.posx, snake_P1.posy = SQUARE * 2, HEIGHT - int(SQUARE / 2)
                snake_P1.path = []
                snake_P1.length = snake_start
                snake_P1.rotation = 0
                snake_P1.body = []
                snake_P1.dead_flag = True
            else:
                time0 = pygame.time.get_ticks()

            # 撞墙后重新开始
            if snake_P1.dead_flag:
                # 显示时间
                time1 = pygame.time.get_ticks()
                start_render1 = cur_font.render('等待重新开始', True, (255, 255, 255))
                screen.blit(start_render1, (SQUARE * 2 - int(SQUARE / 4), HEIGHT - SQUARE))

                if (time1 - time0) > 3000:
                    time0 = time1
                    snake_P1.dead_flag = False
            if double_flag:
                snake_P2.rotation_angle_p2(pygame.key.get_pressed())
                snake_P2.update()
                snake_P2.crash_map()
                if snake_P2.dead_flag:
                    snake_P2.posx, snake_P2.posy = SQUARE * 3, HEIGHT - int(SQUARE / 2)
                    snake_P2.path = []
                    snake_P2.length = snake_start
                    snake_P2.rotation = 0
                    snake_P2.body = []
                    snake_P2.dead_flag = True
                else:
                    time3 = pygame.time.get_ticks()

                # 撞墙后重新开始
                if snake_P2.dead_flag:
                    # 显示时间
                    # print("p2")
                    time4 = pygame.time.get_ticks()
                    start_render2 = cur_font.render('等待重新开始', True, (255, 255, 255))
                    screen.blit(start_render2, (SQUARE * 3 + int(SQUARE / 4), HEIGHT - int(SQUARE * 0.5)))

                    if (time4 - time3) > 3000:
                        time3 = time4
                        snake_P2.dead_flag = False
        # 吃食物判断
        if snake_P1.eat_food((food.x, food.y), False):
            food.is_eaten = True
            food.reset()
        if snake_P1.eat_food((food2.x, food2.y), False):
            food2.is_eaten = True
            food2.reset()
        if snake_P1.eat_food((food3.x, food3.y), False):
            food3.is_eaten = True
            food3.reset()
        if snake_P1.eat_food((food4.x, food4.y), False):
            food4.is_eaten = True
            food4.reset()
        if snake_P1.eat_food((food5.x, food5.y), False):
            food5.is_eaten = True
            food5.reset()
        if snake_P1.eat_food((food6.x, food6.y), False):
            food6.is_eaten = True
            food6.reset()
        if snake_P1.eat_food((food7.x, food7.y), False):
            food7.is_eaten = True
            food7.reset()
        if snake_P1.eat_food((food8.x, food8.y), False):
            food8.is_eaten = True
            food8.reset()
        if snake_P1.eat_food((food9.x, food9.y), False):
            food9.is_eaten = True
            food9.reset()
        if snake_P1.eat_food((food10.x, food10.y), False):
            food10.is_eaten = True
            food10.reset()
        if double_flag:
            if snake_P2.eat_food((food.x, food.y), False):
                food.is_eaten = True
                food.reset()
            if snake_P2.eat_food((food2.x, food2.y), False):
                food2.is_eaten = True
                food2.reset()
            if snake_P2.eat_food((food3.x, food3.y), False):
                food3.is_eaten = True
                food3.reset()
            if snake_P2.eat_food((food4.x, food4.y), False):
                food4.is_eaten = True
                food4.reset()
            if snake_P2.eat_food((food5.x, food5.y), False):
                food5.is_eaten = True
                food5.reset()
            if snake_P2.eat_food((food6.x, food6.y), False):
                food6.is_eaten = True
                food6.reset()
            if snake_P2.eat_food((food7.x, food7.y), False):
                food7.is_eaten = True
                food7.reset()
            if snake_P2.eat_food((food8.x, food8.y), False):
                food8.is_eaten = True
                food8.reset()
            if snake_P2.eat_food((food9.x, food9.y), False):
                food9.is_eaten = True
                food9.reset()
            if snake_P2.eat_food((food10.x, food10.y), False):
                food10.is_eaten = True
                food10.reset()

        # 吃地雷让自己掉一节长度
        if snake_P1.eat_food((food_boom.x, food_boom.y), True):
            snake_P1.length -= 1
            food_boom.is_eaten = True
            food_boom.reset()
        if double_flag:
            if snake_P2.eat_food((food_boom.x, food_boom.y), True):
                snake_P2.length -= 1
                food_boom.is_eaten = True
                food_boom.reset()
        # 生成食物
        food.bulid_mini()
        food2.bulid_mini()
        food3.bulid_mini()
        food4.bulid_mini()
        food5.bulid_mini()
        food6.bulid_mini()
        food7.bulid_mini()
        food8.bulid_mini()
        food9.bulid_mini()
        food10.bulid_mini()
        food_boom.bulid_img()
        # 显示障碍
        for i in crash_list1:
            screen.blit(map_image1, (i[0], i[1]))
        for i in crash_list2:
            screen.blit(map_image2, (i[0], i[1]))
        try:
            for i in crash_list3:
                screen.blit(map_image3, (i[0], i[1]))
        except Exception as e:
            pass
        # 显示得分文字
        screen.blit(cur_font.render("玩家1长度:{0}".format(snake_P1.length + 1), 1, (0, 0, 0)), (0, int(SQUARE / 4)))
        if double_flag:
            screen.blit(cur_font.render("玩家2长度:{0}".format(snake_P2.length + 1), 1, (0, 0, 0)),
                        (WIDTH - SQUARE * 3, int(SQUARE / 4)))
        screen.blit(cur_font.render("目标长度:{0}".format(score_end), 1, (0, 0, 0)),
                    (WIDTH - SQUARE * 3, HEIGHT - SQUARE * 1))

        # 如果有玩家赢，显示结束画面
        if snake_P1.is_win or snake_P2.is_dead:
            screen.blit(background, (0, 0))
            screen.blit(over1, (0, 0))
            screen.blit(snake_P1.head, (WIDTH / 2 + SQUARE, HEIGHT / 2 - SQUARE * 2))
            screen.blit(cur_font.render("玩家", 1, (0, 0, 0)), (WIDTH / 2 - SQUARE * 1.5, HEIGHT / 2 - SQUARE * 2))
            # end = True
            # break
        if snake_P2.is_win or snake_P1.is_dead:
            screen.blit(background, (0, 0))
            screen.blit(over1, (0, 0))
            screen.blit(snake_P2.head, (WIDTH / 2 + SQUARE, HEIGHT / 2 - SQUARE * 2))
            screen.blit(cur_font.render("玩家", 1, (0, 0, 0)), (WIDTH / 2 - SQUARE * 1.5, HEIGHT / 2 - SQUARE * 2))
            # end = True
            # break

        # 显示ipad按键
        if ipad_control_switch:
            screen.blit(ipad_control, (0, 0))
        # 刷新屏幕
        pygame.display.update()


if __name__ == '__main__':
    # map = [
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    #     [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0],
    #     [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 2, 0, 3, 0, 3, 0],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0]
    # ]

    map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # map = [
    #     [0, 0, 0, 0, 2],
    #     [1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 2],
    #     [0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0],
    # ]
    # 设置障碍物，对应列表中的123
    # wall_1('test1.jpg')
    # wall_2('test2.png')
    # wall_3('bg.png')
    # # 设置蛇头
    # snake_1('test3.png')
    # snake_2('test4.png')
    # boom('map1.png')
    set_map(map)
    speed(20)
    start(3)
    end(4)
    double()
    ipad_control()
    play()

    # map = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]

    # map = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    #     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]

    # map = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]

    # map = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # ]