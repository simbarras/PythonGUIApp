import numpy as np
import neat


class NeuralBot:
    gen = 0
    net = None
    genome = None
    vel = 10;

    def start_genome(self, genome, config):
        self.net = neat.nn.FeedForwardNetwork.create(genome, config)
        self.genome = genome
        self.genome.fitness = 0
        self.gen = 0

    def play(self, root, ball, player):
        pipe_ind = 0

        self.genome.fitness += 0.1
        # Write inputs
        output = self.net.activate()
        return output[0] * 10

    def run(self, config_file):
        config = neat.Config(neat.DefaultGenome, neat.DefaultReprodutcion, neat.DefaultSpecieSet,
                             neat.DefaultStagnation, config_file)

        population = neat.Population(config)
        population.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatictisReporter()
        population.add_reporter(stats)

        winner = population.run(eval_genomes, 1)
        print("\nBest genome:\n{!s}".format(winner))

    def play(self, playground, ball, player):
        np.dot(2, 2)
