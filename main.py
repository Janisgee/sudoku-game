from view.app import App
from model.game_model import Game_model
from control.controller import Controller

if __name__ == "__main__" :
  model = Game_model()
  model.set_new_game()
  controller = Controller(model)
  theApp = App(controller,model)
  theApp.on_execute()