from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QLabel, QLineEdit, QWidget, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent


class BowlingView(QMainWindow):
    def __init__(self):
        self.controller = None  # Initialize the controller
        super(BowlingView, self).__init__()
        self.setWindowTitle("Bowling Scorecard")
        self.setFixedSize(800, 260)

        # Create three widgets for Frames, Throws, and Scores
        self.frames_widget = QWidget()
        self.throws_widget = QWidget()
        self.scores_widget = QWidget()

        # Layouts for each widget
        frames_layout = QGridLayout()
        throws_layout = QGridLayout()
        scores_layout = QGridLayout()

        self.frames_widget.setLayout(frames_layout)
        self.throws_widget.setLayout(throws_layout)
        self.scores_widget.setLayout(scores_layout)

        # Style for the Frames widget
        self.frames_widget.setStyleSheet(
            "background-color: lightgray; border: 1px solid gray;")

        # Style for the Throws widget
        self.throws_widget.setStyleSheet(
            "background-color: lightblue; border: 1px solid blue;")

        # Style for the Scores widget
        self.scores_widget.setStyleSheet(
            "background-color: lightgray; border: 1px solid gray;")

        self.frame_labels = []
        self.throw_inputs = []
        self.score_labels = []

        # Populate the Frames widget with labels
        for i in range(9):
            frame_label = QLabel(f"Frame {i + 1}", self)
            frame_label.setFixedWidth(50)
            frames_layout.addWidget(frame_label, 0, i)
            self.frame_labels.append(frame_label)

        # Make the 10th Frame wider
        frame_label_10 = QLabel(f"Frame 10", self)
        frame_label_10.setFixedWidth(85)
        frames_layout.addWidget(frame_label_10, 0, 9)
        self.frame_labels.append(frame_label_10)

        # Populate the Throws widget with input boxes
        for i in range(21):
            throw_input = BowlingLineEdit(self)
            throw_input.setFixedWidth(20)
            throws_layout.addWidget(throw_input, 0, i)
            self.throw_inputs.append(throw_input)

        # Populate the Scores widget with labels
        for i in range(9):
            score_label = QLabel("", self)
            score_label.setFixedWidth(50)
            scores_layout.addWidget(score_label, 0, i)
            self.score_labels.append(score_label)

        # Make the 10th Score wider
        score_label_10 = QLabel("", self)
        score_label_10.setFixedWidth(85)
        scores_layout.addWidget(score_label_10, 0, 9)
        self.score_labels.append(score_label_10)

        # Create a central widget that contains the three sub-widgets
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.frames_widget)
        layout.addWidget(self.throws_widget)
        layout.addWidget(self.scores_widget)
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

        # Create a label for error messages
        self.error_label = QLabel("", self)
        # Red text for error messages
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)

        # Create a reset button
        reset_button = QPushButton("RESET", self)
        reset_button.setFixedHeight(30)
        layout.addWidget(reset_button)

        # Connect the reset button to a function for resetting the scorecard
        reset_button.clicked.connect(self.reset_scorecard)

    def update_score(self, frame, score):
        if frame < len(self.score_labels):  # Check if the frame is within the label list
            self.score_labels[frame].setText(str(score))
        else:
            print("Game over.")

    def reset_scorecard(self):
        self.controller.reset_game()
        # Clear the input boxes and reset the scores
        for throw_input in self.throw_inputs:
            throw_input.clear()
        for score_label in self.score_labels:
            score_label.clear()


class BowlingLineEdit(QLineEdit):
    def __init__(self, view):
        super().__init__(view)
        self.view = view

    def keyPressEvent(self, event):
        key = event.key()

        if key == 16777252:  # Ignore Caps Lock key
            event.ignore()
            return

        if key == 16777248:  # Ignore Shift key
            event.ignore()
            return

        frame = self.view.throw_inputs.index(self)
        throw = frame + 1
        throw_type = None

        if throw % 2 == 0:  # Even throw, i.e., Throw 2
            pins_throw1_text = self.view.throw_inputs[frame - 1].text()
            if pins_throw1_text and pins_throw1_text.isdigit():
                pins_throw1 = int(pins_throw1_text)
            else:
                pins_throw1 = 0  # Default to 0 if it's not a valid integer

            if event.text() == '/':
                if throw % 2 == 1:  # First throw in the frame
                    self.view.error_label.setText(
                        "You cannot have thrown a spare on the first throw of a frame ;)")
                    return
                pins = 10 - pins_throw1
                throw_type = "spare"
            elif event.text().isdigit():
                pins = int(event.text())
                throw_type = "regular"
            elif event.text().lower() == 'x':
                pins = 10 - pins_throw1
                throw_type = "strike"

            else:
                self.view.error_label.setText("Invalid entry.")
                return

            total_pins = pins_throw1 + pins
            if total_pins > 10:
                self.view.error_label.setText("That math does not add up.")
                return
            else:
                self.view.error_label.setText("")

            # Calculate the score for the current frame
            frame_number = frame // 2
            score = self.view.controller.model.score(frame_number)
            self.view.update_score(frame_number, score + pins)

        elif key in (48, 49, 50, 51, 52, 53, 54, 55, 56, 57):
            throw_type = "regular"
            pins = int(event.text())

        elif event.text().lower() == 'x':
            throw_type = "strike"
            pins = 10

            if throw == 21:
                frame_number = frame // 2
                score = self.view.controller.model.score(frame_number)
                self.view.update_score(frame_number, score + pins)
            elif throw == 20:
                frame_number = frame // 2
                score = self.view.controller.model.score(frame_number)
                self.view.update_score(frame_number, score + pins)
            elif throw % 2 == 1 and throw != 19:
                next_frame = frame + 1
                next_input = self.view.throw_inputs[next_frame]
                if isinstance(next_input, BowlingLineEdit):
                    next_input.setFocus()

        else:
            self.view.error_label.setText("Invalid character.")
            return

        if throw_type:
            super().keyPressEvent(event)
            next_input = self.parent().focusNextChild()
            if isinstance(next_input, BowlingLineEdit):
                next_input.setFocus()

            self.view.controller.update_score(frame // 2, pins, throw_type)
