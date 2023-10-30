from typing import Literal


class BowlingGameLogic:
    def __init__(self):
        self.reset_game()

    def get_current_frame(self) -> int:
        # 0-indexed version of current frame
        return min(self.current_throw // 2, 9)

    def get_current_throw(self) -> int:
        return self.current_throw

    def reset_game(self):
        self.throws = [0] * 21
        self.current_throw = 0

    def throw(self, pins: int | Literal["strike"] | Literal["spare"]):
        if pins == "strike":
            self.throws[self.current_throw] = 10
            if self.current_throw < 18:
                self.current_throw += 2
            else:
                self.current_throw += 1
        elif pins == "spare":
            self.throws[self.current_throw] = 10 - self.throws[self.current_throw - 1]
            self.current_throw += 1
        else:
            self.throws[self.current_throw] = pins
            self.current_throw += 1

    def score(self, target_frame: int) -> int:
        score = 0
        for frame in range(target_frame + 1):
            if self.is_last_frame(frame):
                score += self.last_frame_score()
            elif self.is_strike(frame):
                score += 10 + self.strike_bonus(frame)
            elif self.is_spare(frame):
                score += 10 + self.spare_bonus(frame)
            else:
                score += self.sum_of_balls_in_frame(frame)
            print(frame, score)
        return score

    def is_last_frame(self, frame):
        return frame == 9

    def last_frame_score(self):
        throw = len(self.throws) - 3
        return sum(self.throws[throw:])

    def is_strike(self, frame):
        return self.throws[frame * 2] == 10

    def strike_bonus(self, frame):
        return sum(self._next_values((frame + 1) * 2, 2))

    def is_spare(self, frame):
        if frame >= 10:
            return False
        throw = frame * 2
        return self.throws[throw] + self.throws[throw + 1] == 10

    def spare_bonus(self, frame):
        return sum(self._next_values((frame + 1) * 2, 1))

    def sum_of_balls_in_frame(self, frame):
        throw = frame * 2
        if frame == 10:
            return self.throws[throw]
        return self.throws[throw] + self.throws[throw + 1]

    def _next_values(self, start_from: int, count: int) -> list[int]:
        values = []
        for value in self.throws[start_from:]:
            if count == 0:
                break
            if value != 0:
                values.append(value)
                count -= 1
        return values
