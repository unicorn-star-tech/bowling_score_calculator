class BowlingGameLogic:
    def reset_game(self):
        self.throws = [0] * 21
        self.current_throw = 0

    def __init__(self):
        self.throws = [0] * 21
        self.current_throw = 0

    def throw(self, pins):
        self.throws[self.current_throw] = pins
        self.current_throw += 1

    def score(self, frame=None):
        score = 0
        frame_index = 0

        if frame is not None:
            max_frame = min(frame, 9)  # Cap frame to ensure it's within bounds
        else:
            max_frame = 9  # Score all frames

        for frame in range(max_frame + 1):
            frame_index = min(max_frame + 1, frame_index)  # max frame bounds

            if self.is_strike(frame_index):
                score += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                score += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.sum_of_balls_in_frame(frame_index)
                frame_index += 2

        return score

    def is_strike(self, frame_index):
        return self.throws[frame_index] == 10

    def strike_bonus(self, frame_index):
        return self.throws[min(frame_index + 1, 10)] + self.throws[min(frame_index + 2, 10)]

    def is_spare(self, frame_index):
        return self.throws[frame_index] + self.throws[min(frame_index + 1, 10)] == 10

    def spare_bonus(self, frame_index):
        return self.throws[min(frame_index + 2, 10)]

    def sum_of_balls_in_frame(self, frame_index):
        return self.throws[frame_index] + self.throws[min(frame_index + 1, 10)]
