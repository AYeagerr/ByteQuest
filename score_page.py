import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QScrollArea, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
from PyQt5.QtMultimedia import QSound

class ScoreHistoryWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Score History')
        self.setGeometry(100, 100, 600, 400)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Display the scores
        self.display_scores()
        
        # Add and configure the back button
        self.add_back_button()
        
        # Gradient background
        self.central_widget.setStyleSheet(
            """
            QWidget {
                background-color: #002F40;
                color: white;
            }
            """
        )

    def add_back_button(self):
        # Back Button
        self.back_button = QPushButton("Back")
        self.back_button.setFont(QFont('Press Start 2P', 14))
        self.layout.addWidget(self.back_button)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                border-style: outset;
                border-width: 2px;
                border-radius: 10px;
                border-color: white;
                font: bold 14px;
                min-width: 10em;
                text-align:center;
                padding:10px;
            }
            QPushButton:hover {
                background-color: white;
                color:black;
                border-color:black;
                border-style: inset;
            }
            QPushButton:pressed {
                background-color: #FFD500;
                color:black;
                border-style: inset;
            }
        """)
        # Sound effects
        self.click_sound = QSound("Assets/Sounds/gta-click.wav")
        self.hover_sound = QSound("Assets/Sounds/gta-hover.wav")
        # Connect the button's click event to the backtomain method
        self.back_button.enterEvent = lambda event, b=self.back_button: self.play_hover_sound(event, b)
        self.back_button.clicked.connect(self.click_sound.play)
        self.back_button.clicked.connect(self.backtomain)
    def play_hover_sound(self, event, button):
        self.hover_sound.play()
        return super(QPushButton, button).enterEvent(event)

    def backtomain(self):
        process = QProcess(self)
        process.start("python", ["main_menu.py"])  # Placeholder for actual function
        self.hide()

    def display_scores(self):
        # Score History Title
        score_history_label = QLabel("Score History")
        score_history_label.setAlignment(Qt.AlignCenter)
        score_history_label.setFont(QFont('Press Start 2P', 24))
        self.layout.addWidget(score_history_label)
        score_history_label.setStyleSheet("background-color:transparent; color:white;")
        
        # Create a scrollable area for scores
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        score_widget = QWidget()
        score_layout = QVBoxLayout()

        # Read and display scores from JSON file
        try:
            with open('scores.json', 'r') as file:
                score_data = json.load(file)
                for entry in score_data:
                    score_label = QLabel(f"Score: {entry['score']} on {entry['date']} at {entry['level']}")
                    score_label.setAlignment(Qt.AlignCenter)
                    score_label.setFont(QFont('Press Start 2P', 14))
                    score_layout.addWidget(score_label)
                    score_label.setStyleSheet("background-color:transparent; color:#FFD500;")
        except FileNotFoundError:
            error_label = QLabel("Score history not available.")
            error_label.setAlignment(Qt.AlignCenter)
            error_label.setFont(QFont('Press Start 2P', 14))
            score_layout.addWidget(error_label)
            error_label.setStyleSheet("background-color:transparent; color:white;")
        except json.JSONDecodeError:
            error_label = QLabel("No score data found.")
            error_label.setAlignment(Qt.AlignCenter)
            error_label.setFont(QFont('Press Start 2P', 14))
            score_layout.addWidget(error_label)
            error_label.setStyleSheet("background-color:transparent; color:white;")

        score_widget.setLayout(score_layout)
        scroll.setWidget(score_widget)
        self.layout.addWidget(scroll)
        scroll.setStyleSheet("background-color:transparent;")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    score_history_window = ScoreHistoryWindow()
    score_history_window.show()
    sys.exit(app.exec_())