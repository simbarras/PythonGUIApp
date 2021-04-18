class BotAlgo:
    ball = None
    player = None

    def __init__(self, ball, player):
        self.ball = ball
        self.player = player
        print(str(ball.velocity_y))

    def update_player(self, dt):
        self.player.center_y = self.ball.center_y
        print(str(self.player.center_y))
