from PyQt6.QtWidgets import QApplication

from bowling_view import BowlingView
from bowling_model import BowlingGameLogic


class BowlingController:
    def __init__(self, model: BowlingGameLogic, view: BowlingView):
        self.model = model
        self.view = view
        self.view.show()
        self.view.controller = self

    def update_score(self, frame, pins, throw_type):
        if throw_type != "regular":
            self.model.throw(throw_type)
        else:
            self.model.throw(pins)

        # Update the score for all frames up to the current frame
        for frame in range(self.model.get_current_frame() + 1):
            score = self.model.score(frame)
            self.view.update_score(frame, score)

    def reset_game(self):
        self.model.reset_game()  # Reset the game state
        for frame in range(10):
            self.view.update_score(frame, 0)
