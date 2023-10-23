from PyQt6.QtWidgets import QApplication

from bowling_view import BowlingView
from bowling_model import BowlingGameLogic


class BowlingController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.show()
        self.view.controller = self
        self.current_frame = 0  # Initialize the current frame
        self.current_throw = 0  # Initialize the current throw

    def update_score(self, frame, pins, throw_type):
        if throw_type == "strike":
            self.model.throw(10)  # Always record 10 pins for a strike
        else:
            self.model.throw(pins)

        # Update the score for all frames up to the current frame
        for frame in range(self.current_frame + 1):
            score = self.model.score(frame)
            self.view.update_score(frame, score)

        # Update the current frame and throw
        if throw_type == "strike":
            self.current_frame += 1
            self.current_throw = 0
        elif self.current_throw == 1 or throw_type == "spare":
            self.current_frame += 1
            self.current_throw = 0
        else:
            self.current_throw += 1

    def reset_game(self):
        self.model.reset_game()  # Reset the game state
        self.current_frame = 0
        self.current_throw = 0
        for frame in range(10):
            self.view.update_score(frame, 0)
