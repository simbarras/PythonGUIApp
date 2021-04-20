class BotAlgo:

    def update_player(self, ball, player):
        vel = 10
        if player.center_y < ball.center_y - vel:
            return 1 * vel
        if player.center_y > ball.center_y + vel:
            return -1 * vel
        else:
            return 0
