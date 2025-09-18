import sys
import json
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtGui import QFont, QMovie, QPixmap
from PyQt5.QtCore import Qt, QProcess
from PyQt5.QtMultimedia import QSound


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window (Name and Size)
        self.setWindowTitle("ByteQuest - Cyber Security Quiz Game")
        self.setGeometry(100, 100, 600, 400)

        # Central widget and layout
        self.central_widget = QWidget()
        # Center the widget created
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Spacer for padding above the GIF
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.layout.addItem(self.top_spacer)

        # Set up the GIF at the top
        self.gif_label = QLabel(self)
        self.movie = QMovie("Penetration.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        self.gif_label.setStyleSheet("background-color: #00000000;")
        self.gif_label.setFixedSize(734, 390)
        # Add the widget to the screen
        self.layout.addWidget(self.gif_label)
        self.gif_label.setAlignment(Qt.AlignCenter)

        # Label for displaying the program name with customized styling and font.
        self.program_name_label = QLabel("ByteQuest")
        self.program_name_label.setAlignment(Qt.AlignCenter)
        self.program_name_label.setStyleSheet(
            """
        QLabel {
            color: white;
            font-size: 24px;
            font-weight: bold;
            padding: 20px;
            background-color: transparent;
        }
        """
        )

        # Set font type ,style and size
        program_name_font = QFont("Press Start 2P", 24, QFont.Bold)
        self.program_name_label.setFont(program_name_font)
        # Add the widget to the screen
        self.layout.addWidget(self.program_name_label)

        # calls the load_scores() method of the MainWindow class. 
        # The method attempts to open and read a JSON file named 'scores.json' that contains score data.
        # returns the scores as a list of dictionaries or an empty list if the file doesn't exist or there's an error in reading it.
        self.scores = self.load_scores()
        highest_score = (
            # This uses the max() function to find the dictionary in the self.scores list with the highest value associated with the key 'score'.
            # The lambda function is used to tell max how to find the score within each dictionary.
            max(self.scores, key=lambda x: x["score"])
            if self.scores
            else None
            # This part checks if self.scores is not empty. If self.scores is empty (no scores were loaded), highest_score is set to None.
        )
        highest_score_text = (
            f"Highest Score: {highest_score['score']}"
            if highest_score
            else "Highest Score: Not Available"
        )
        
        

        # Score label styling and positioning
        self.score_label = QLabel(highest_score_text)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet(
            """
        QLabel {
            color: #F7424B;
            font-size: 15px;
            padding: 20px;
            background-color: transparent;
        }
        """
        )
        self.score_label.setFont(program_name_font)
        self.layout.addWidget(self.score_label)

        # Spacer to push buttons to the bottom
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(self.spacer)

        # Gradient background
        self.central_widget.setStyleSheet("QWidget { background-color: #002F40;  }")

        # Font for buttons
        font = QFont("Press Start 2P")
        font.setPointSize(10)
        # Button styling
        button_style = """
        QPushButton {
            background-color: #FFD500;
            color: black;
            border-style: outset;
            border-width: 3px;
            border-radius: 10px;
            border-color: black;
            font: bold 14px;
            min-width: 10em;
            text-align:center;
            padding:10px;
        }
        QPushButton:hover {
            background-color: white;
            color:black;
            border-style: inset;
        }
        QPushButton:pressed {
            background-color: #F7424B;
            color:white;
            border-style: inset;
        }
        """

        # Sound effects
        self.click_sound = QSound("Assets/Sounds/gta-click.wav")
        self.hover_sound = QSound("Assets/Sounds/gta-hover.wav")

        # Create buttons
        self.start_button = self.create_button("Start", font, button_style)
        self.score_button = self.create_button("Score History", font, button_style)
        self.exit_button = self.create_button("Exit", font, button_style)

        # Adding buttons to layout
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.score_button)
        self.layout.addWidget(self.exit_button)
        self.layout.setAlignment(Qt.AlignCenter)
        self.central_widget.setLayout(self.layout)

        # Connect buttons to functions
        self.start_button.clicked.connect(self.start_quiz)
        self.score_button.clicked.connect(self.view_scores)
        self.exit_button.clicked.connect(self.close)

    def load_scores(self):
        try:
            with open("scores.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def create_button(self, text, font, style):
        button = QPushButton(text)
        button.setFont(font)
        button.setStyleSheet(style)
        button.clicked.connect(self.click_sound.play)  # Connect click sound
        button.enterEvent = lambda event, b=button: self.play_hover_sound(event, b)
        return button

    def play_hover_sound(self, event, button):
        self.hover_sound.play()
        return super(QPushButton, button).enterEvent(event)

    def start_quiz(self):
        print("Quiz Started!")
        self.hide()
        process = QProcess(self)
        process.start("python", ["topics_form.py"])  # Moves to the level Selection page

    def view_scores(self):
        
        print("Viewing Scores")
        self.hide()
        process = QProcess(self)
        process.start("python", ["score_page.py"])  # Moves to the scores page


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
