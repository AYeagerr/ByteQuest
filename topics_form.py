import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QSpacerItem,
    QSizePolicy,
    QHBoxLayout,
)
from PyQt5.QtGui import QFont, QMovie
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QProcess
from PyQt5.QtMultimedia import QSound


class MainWindow(QMainWindow):
    # This class inherits from QMainWindow, which is a type of top-level window with a title bar and a border.
    def __init__(self):
        # This is the constructor for the class. It initializes the new instance of the class and calls the constructor of the superclass (QMainWindow).
        super().__init__()

        # Set the title and initial size of the window
        self.setWindowTitle("Cyber Security Quiz")
        self.setGeometry(100, 100, 600, 400)  # x, y, width, height

        # Central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Adding top spacer for padding before the GIF
        self.top_spacer = QSpacerItem(
            20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed
        )  # Adjust height for desired space
        self.layout.addItem(self.top_spacer)

        # GIF at the top
        self.gif_label = QLabel(self)
        self.movie = QMovie("Penetration.gif")  # Adjust path to your GIF file
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        # Set a solid background color for the QLabel displaying the GIF
        self.gif_label.setStyleSheet("background-color: #00000000;")
        # Set fixed size for the GIF display 
        self.gif_label.setFixedSize(734, 390)  # Width x Height in pixels
        self.layout.addWidget(self.gif_label)
        self.gif_label.setAlignment(Qt.AlignCenter)
        # Add the program name label
        self.program_name_label = QLabel("Select a topic")
        self.program_name_label.setAlignment(Qt.AlignCenter)
        self.program_name_label.setStyleSheet(
            """
        QLabel {
          color: white;
          font-size: 24px;
          font-weight: bold;
          padding: 20px;
          background-color:transparent;
        }
        """
        )
        # Set font for the program name
        program_name_font = QFont("Press Start 2P", 24, QFont.Bold)
        self.program_name_label.setFont(program_name_font)

        # Add the program name label to the layout after the GIF
        self.layout.addWidget(self.program_name_label)

        # Set size policy to expand both horizontally and vertically
        self.gif_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add spacer to push buttons to the bottom
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(self.spacer)

        # Gradient background
        self.central_widget.setStyleSheet(
            """
            QWidget {
               background-color: #002F40;
            }
            """
        )

        # Pixelated font
        font = QFont(
            "Press Start 2P"
        )
        font.setPointSize(10)

        # Buttons with depth styling
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
        back_button_style = """
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
                background-color: #F7424B;
                color:white;
                border-style: inset;
            }
        """

        # Sound effects
        self.click_sound = QSound("Assets/Sounds/gta-click.wav")
        self.hover_sound = QSound("Assets/Sounds/gta-hover.wav")

        self.top_layout = QHBoxLayout()
        self.back_button = QPushButton("Back")
        self.back_button.setFont(QFont("Press Start 2P", 10))
        self.top_layout.addWidget(self.back_button)
        self.back_button.setStyleSheet(back_button_style)

        # Buttons
        self.easy_button = QPushButton("Cyberattacks")
        self.easy_button.setFont(font)
        self.easy_button.setStyleSheet(button_style)

        self.med_button = QPushButton("Computer Malwares")
        self.med_button.setFont(font)
        self.med_button.setStyleSheet(button_style)

        self.hard_button = QPushButton("Cryptography")
        self.hard_button.setFont(font)
        self.hard_button.setStyleSheet(button_style)

        # Adding buttons to layout
        self.layout.addWidget(self.easy_button)
        self.layout.addWidget(self.med_button)
        self.layout.addWidget(self.hard_button)
        self.layout.addWidget(self.back_button)

        # Set layout alignment to center both vertically and horizontally
        self.layout.setAlignment(Qt.AlignCenter)

        # Set layout to central widget
        self.central_widget.setLayout(self.layout)

        # Connect buttons to functions
        self.easy_button.clicked.connect(self.easybtn)
        self.med_button.clicked.connect(self.midbtn)
        self.hard_button.clicked.connect(self.hardbtn)
        self.back_button.clicked.connect(self.backtomain)

        self.easy_button.clicked.connect(self.click_sound.play)  # Connect click sound
        self.easy_button.enterEvent = (
            lambda event, b=self.easy_button: self.play_hover_sound(event, b)
        )
        self.med_button.clicked.connect(self.click_sound.play)  # Connect click sound
        self.med_button.enterEvent = (
            lambda event, b=self.med_button: self.play_hover_sound(event, b)
        )
        self.hard_button.clicked.connect(self.click_sound.play)  # Connect click sound
        self.hard_button.enterEvent = (
            lambda event, b=self.hard_button: self.play_hover_sound(event, b)
        )
        self.back_button.clicked.connect(self.click_sound.play)  # Connect click sound
        self.back_button.enterEvent = (
            lambda event, b=self.back_button: self.play_hover_sound(event, b)
        )

    def play_hover_sound(self, event, button):
        self.hover_sound.play()
        return super(QPushButton, button).enterEvent(event)

    def backtomain(self):
        print("Quiz Started!") 
        process = QProcess(self)
        process.start("python", ["main_menu.py"])
        self.hide()

    def easybtn(self):
        print("Quiz Started!") 
        process = QProcess(self)
        process.start(
            "python", ["cyberattacks.py"]
        ) 
        self.hide()

    def midbtn(self):
        print("Quiz Started!") 
        process = QProcess(self)
        process.start("python", ["computer_malwares.py"]) 
        self.hide()

    def hardbtn(self):
        print("Quiz Started!") 
        process = QProcess(self)
        process.start(
            "python", ["cryptography.py"]
        ) 
        self.hide()

    def view_scores(self):
        print("Viewing Scores") 


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
