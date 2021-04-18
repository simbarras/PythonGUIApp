from random import randint

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from pong.bot.algo import BotAlgo


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        self.player1.bounceBall(self.ball)
        self.player2.bounceBall(self.ball)

        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
            # print("Y: " + str(self.ball.velocity_y))

        if (self.ball.x < self.x):
            self.player2.score += 1
            print(str(self.ball.velocity_x))
            self.serve_ball(vel=(4, 0))
            self.player1.center_y = self.center_y
            self.player2.center_y = self.center_y
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))
            self.player1.center_y = self.center_y
            self.player2.center_y = self.center_y

    def on_touch_move(self, touch):
        if touch.x < self.width / 2:
            self.move(self.player1, touch.y)
        if touch.x > self.width / 2:
            self.move(self.player2, touch.y)

    def move(self, player, y):
        player.center_y = y


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounceBall(self, ball):
        if self.collide_widget(ball):
            ball.velocity_y = ball.velocity_y - 0.02 * (self.center_y - ball.center_y)
            if ball.velocity_x * ball.velocity_x < 900:
                if ball.velocity_x < 0:
                    ball.velocity_x -= 0.5
                else:
                    ball.velocity_x += 0.5

            ball.velocity_x = -ball.velocity_x
            #print(str(ball.velocity_x))
            #print(str(ball.velocity_y))


class PongApp(App):
    bot = None

    def build(self):
        game = PongGame()
        game.serve_ball()
        bot = BotAlgo(game.ball, game.player2)
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        Clock.schedule_interval(bot.update_player, 1.0 / 60.0)

        return game


if __name__ == '__main__':
    PongApp().run()

