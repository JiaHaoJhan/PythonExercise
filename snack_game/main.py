from turtle import Screen
from snack import Snack
from food import Food
from scoreboard import Scoreboard
import time

# 初始化畫面參數
screen = Screen()
# 設定畫面大小 600*600
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
# 關閉動畫
screen.tracer(0)

# 初始化並建立第一隻蛇
snack = Snack()
# 初始化並建立食物
food = Food()
# 初始化記分板
scoreboard = Scoreboard()
# 監聽玩家控制
screen.listen()
screen.onkey(snack.up, "w")
screen.onkey(snack.down, "s")
screen.onkey(snack.left, "a")
screen.onkey(snack.right, "d")

game_is_on = True
while game_is_on:
    # 搭配screen.tracer(0)使其顯示
    screen.update()
    # delay 1s
    time.sleep(0.1)
    snack.move()

    # 蛇接觸到食物
    if snack.head.distance(food) < 15:
        snack.extend()
        food.create_new_food()
        scoreboard.add_score()
    # 檢查是否碰到牆壁
    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # 檢查是否有碰到蛇身，for迴圈去除第一個頭部位置
    for segment in snack.segments[1:]:
        if snack.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

