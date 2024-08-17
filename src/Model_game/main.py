import player
import game


cheater = player.Cheater()
cooperator = player.Cooperator()
copycat = player.Copycat()
grudger = player.Grudger()
detective = player.Detective()

game = game.Game()

game.play(cheater, cooperator)
game.play(cheater, copycat)
game.play(cheater, grudger)
game.play(cheater, detective)
game.play(cooperator, copycat)
game.play(cooperator, grudger)
game.play(cooperator, detective)
game.play(copycat, grudger)
game.play(copycat, detective)
game.play(grudger, detective)


game.top3()