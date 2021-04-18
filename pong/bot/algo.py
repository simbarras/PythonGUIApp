class BotAlgo:

    def update_player(self, ball, player):
        vel = 2
        if player.center_y < ball.center_y:
            return 1 * vel
        if player.center_y > ball.center_y:
            return -1 * vel
        else:
            return 0
