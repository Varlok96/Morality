import player
import game


cheater = player.Cheater()
cooperator = player.Cooperator()
copycat = player.Copycat()
grudger = player.Grudger()
detective = player.Detective()
my_player = player.My_Player()

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

game.play(my_player, cheater)
game.play(my_player, cooperator)
game.play(my_player, copycat)
game.play(my_player, grudger)
game.play(my_player, detective)


game.top3()