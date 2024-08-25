def train(bot):
    from chatterbot.trainers import DictTrainer

    from datalib import data

    trainer=DictTrainer(bot)
    trainer.train(data)
