from turtle import Turtle

# 初始位置
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snack:
    def __init__(self):
        # 儲存所有蛇身長度
        self.segments = []
        # 創建第一隻蛇
        self.create_snack()
        self.head = self.segments[0]

    def create_snack(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(position)
        self.segments.append(new_body)

    def extend(self):
        # 增加蛇身的長度 ，segments[-1].position()蛇的尾巴部分
        self.add_segment(self.segments[-1].position())

    def move(self):
        # 移動蛇身，由尾巴開始更新至頭之前的位置， range(start, stop, step)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # 最後頭部向前一格
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
