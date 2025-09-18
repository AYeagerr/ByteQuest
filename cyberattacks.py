import sys
import random
import json
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QGroupBox, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QProcess, QTimer
from PyQt5.QtMultimedia import QSound



# ...
questions_cyberattacks = {
    "1": {
        "question": "What does 'HTTP' stand for in the context of web communication?",
        "options": {
            "A": "HyperText Transfer Product",
            "B": "HyperText Transfer Protocol",
            "C": "HyperText Transfer Process",
            "D": "HyperText Transfer Password",
        },
        "answer": "B",
    },
    "2": {
        "question": "What is the primary function of a firewall in cybersecurity?",
        "options": {
            "A": "Speeding up the network",
            "B": "Monitoring network traffic",
            "C": "Protecting the network from unauthorized access",
            "D": "Storing extra data",
        },
        "answer": "C",
    },
    "3": {
        "question": "What is the recommended action if you receive an email from an unknown sender with an attachment?",
        "options": {
            "A": "Open the attachment immediately",
            "B": "Forward the email to your friends",
            "C": "Delete the email",
            "D": "Download the attachment",
        },
        "answer": "C",
    },
    "4": {
        "question": "What is a common indicator of a phishing attempt in cybersecurity?",
        "options": {
            "A": "An email from a friend",
            "B": "An email that requests sensitive information",
            "C": "A regularly formatted website URL",
            "D": "An email that provides accurate personal information",
        },
        "answer": "B",
    },
    "5": {
        "question": "What does 'VPN' stand for in the context of secure internet access?",
        "options": {
            "A": "Virtual Private Network",
            "B": "Virus Protection Needed",
            "C": "Very Personal Note",
            "D": "Virtual Public Network",
        },
        "answer": "A",
    },
    "6": {
        "question": "Which of the following is considered a strong password in cybersecurity?",
        "options": {
            "A": "123456",
            "B": "password123",
            "C": "yourbirthdate",
            "D": "A!s7@D$",
        },
        "answer": "D",
    },
    "7": {
        "question": "What is the purpose of two-factor authentication in enhancing security?",
        "options": {
            "A": "To make the login process simpler",
            "B": "To decrease security",
            "C": "To provide an extra layer of security",
            "D": "To track user activities",
        },
        "answer": "C",
    },
    "8": {
        "question": "Which activity could increase your risk of falling victim to a cyber attack?",
        "options": {
            "A": "Updating your software regularly",
            "B": "Using strong passwords",
            "C": "Clicking on links in unsolicited emails",
            "D": "Using antivirus software",
        },
        "answer": "C",
    },
    "9": {
        "question": "What is a 'Trojan Horse' in the context of computer security?",
        "options": {
            "A": "A type of antivirus software",
            "B": "A secure operating system",
            "C": "A malware that disguises itself as legitimate software",
            "D": "A firewall feature",
        },
        "answer": "C",
    },
    "10": {
        "question": "Which type of cyber attack involves overwhelming a service with excessive traffic?",
        "options": {
            "A": "Phishing",
            "B": "Ransomware",
            "C": "SQL Injection",
            "D": "DDoS (Distributed Denial of Service)",
        },
        "answer": "D",
    },
    "11": {
        "question": "What is recommended to enhance the security of your online accounts?",
        "options": {
            "A": "Use the same password for all accounts",
            "B": "Share your passwords with trusted friends",
            "C": "Use complex and unique passwords",
            "D": "Write down your passwords and keep them next to your computer",
        },
        "answer": "C",
    },
    "12": {
        "question": "What is the purpose of encryption in cybersecurity?",
        "options": {
            "A": "To speed up data transfer",
            "B": "To make data unreadable to unauthorized users",
            "C": "To delete data",
            "D": "To increase data storage",
        },
        "answer": "B",
    },
    "13": {
        "question": "Which of these is identified as a type of malware?",
        "options": {
            "A": "Email",
            "B": "Firewall",
            "C": "Spyware",
            "D": "VPN",
        },
        "answer": "C",
    },
    "14": {
        "question": "What action should be taken if your computer becomes infected with a virus?",
        "options": {
            "A": "Keep using it to see if the virus goes away",
            "B": "Unplug the internet",
            "C": "Run antivirus software",
            "D": "Sell the computer",
        },
        "answer": "C",
    },
    "15": {
        "question": "Which method is effective in securing data sent over the internet?",
        "options": {
            "A": "Using plain text",
            "B": "Using HTTPS",
            "C": "Sharing passwords",
            "D": "Opening email attachments",
        },
        "answer": "B",
    },
    "16": {
        "question": "What does the term 'backdoor' refer to in the context of computer security?",
        "options": {
            "A": "A secret pathway out of a building",
            "B": "A secondary route to a network",
            "C": "A method of bypassing normal authentication to access a system",
            "D": "A feature in video games",
        },
        "answer": "C",
    },
    "17": {
        "question": "What is the main objective of social engineering in cybersecurity?",
        "options": {
            "A": "To construct social networks",
            "B": "To manipulate individuals into providing confidential information",
            "C": "To build physical infrastructure",
            "D": "To program social media algorithms",
        },
        "answer": "B",
    },
    "18": {
        "question": "Which of the following is NOT considered a safe practice for internet usage?",
        "options": {
            "A": "Using public Wi-Fi to make financial transactions",
            "B": "Regularly updating your software",
            "C": "Avoiding the sharing of personal information online",
            "D": "Using multi-factor authentication",
        },
        "answer": "A",
    },
    "19": {
        "question": "What is the primary function of CAPTCHA tests on websites?",
        "options": {
            "A": "To enhance the website's design",
            "B": "To advertise products",
            "C": "To verify that the user is human",
            "D": "To collect user data for marketing",
        },
        "answer": "C",
    },
    "20": {
        "question": "Which of these examples represents a strong password?",
        "options": {"A": "password", "B": "12345678", "C": "letmein", "D": "Xq3#p!5^"},
        "answer": "D",
    },
    "21": {
        "question": "What type of cyber threat involves holding data hostage for a ransom?",
        "options": {
            "A": "Trojan horse",
            "B": "Virus",
            "C": "Ransomware",
            "D": "Phishing",
        },
        "answer": "C",
    },
    "22": {
        "question": "Which action can help protect your email account from hackers?",
        "options": {
            "A": "Using the same password for every account",
            "B": "Checking your email on public computers",
            "C": "Sharing your email password on social media",
            "D": "Changing your password regularly",
        },
        "answer": "D",
    },
    "23": {
        "question": "What is 'spoofing' in the context of cybersecurity?",
        "options": {
            "A": "A comedy technique",
            "B": "Creating fake versions of websites to trick users",
            "C": "A method of singing",
            "D": "A type of computer hardware",
        },
        "answer": "B",
    },
    "24": {
        "question": "What should you do if you suspect a link in an email might be malicious?",
        "options": {
            "A": "Click it to see what happens",
            "B": "Ignore the email",
            "C": "Report the email as spam",
            "D": "Forward the email to your contacts",
        },
        "answer": "C",
    },
    "25": {
        "question": "Which of these practices is considered unsafe when browsing the internet?",
        "options": {
            "A": "Using updated antivirus software",
            "B": "Clicking on pop-up advertisements",
            "C": "Visiting HTTPS websites",
            "D": "Avoiding downloads from unknown sources",
        },
        "answer": "B",
    },
    "26": {
        "question": "What is the purpose of a 'security patch' in cybersecurity?",
        "options": {
            "A": "To decorate a uniform",
            "B": "To fix security vulnerabilities in software",
            "C": "To patch holes in physical security systems",
            "D": "To update user interfaces",
        },
        "answer": "B",
    },
    "27": {
        "question": "Which of the following is a sign that a website is secure?",
        "options": {
            "A": "The URL starts with 'http://'",
            "B": "The URL starts with 'https://'",
            "C": "The site has numerous pop-up ads",
            "D": "The website asks for your social security number",
        },
        "answer": "B",
    },
    "28": {
        "question": "What does 'IoT' stand for in the context of cybersecurity risks?",
        "options": {
            "A": "Internet of Things",
            "B": "Intranet of Things",
            "C": "Internet of Thieves",
            "D": "Institute of Technology",
        },
        "answer": "A",
    },
    "29": {
        "question": "Which of the following is NOT recommended for securing your home Wi-Fi network?",
        "options": {
            "A": "Using WEP encryption",
            "B": "Changing the default router password",
            "C": "Disabling network name broadcasting",
            "D": "Enabling WPA2 or WPA3 encryption",
        },
        "answer": "A",
    },
    "30": {
        "question": "What type of attack involves intercepting communication between two parties without their knowledge?",
        "options": {
            "A": "Man-in-the-middle attack",
            "B": "Phishing attack",
            "C": "Virus attack",
            "D": "Trojan attack",
        },
        "answer": "A",
    },
}

#
class QuizWindow(QMainWindow):
    def __init__(self, questions):
        super().__init__()
        self.questions = random.sample(list(questions.values()), 10)  # Select 10 random questions out of 30
        self.current_question_index = 0
        self.score = 0

        self.timer = QTimer(self)  # Initialize the timer right after the basic setup
        self.timer.setInterval(1000)  # Set timer to tick every 1000 milliseconds (1 second)
        self.timer.timeout.connect(self.update_timer)  # Connect timer signal to slot for updating UI

        self.initUI()  # Initialize the UI components

    def initUI(self):
        self.setWindowTitle('ByteQuest - Test Your Knowledge')
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setStyleSheet("QWidget {background-color: #002F40;}")

        # Timer label
        self.timer_label = QLabel("30")
        self.timer_label.setFont(QFont('Press Start 2P', 16))
        self.timer_label.setAlignment(Qt.AlignLeft)
        self.timer_label.setStyleSheet("color: red; margin-right: 20px;")
        self.layout.addWidget(self.timer_label)

        # Setup other UI components such as buttons, labels, etc.
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
        
        # Sound effects
        self.click_sound = QSound("Assets/Sounds/gta-click.wav")
        self.hover_sound = QSound("Assets/Sounds/gta-hover.wav")
        # Top layout for score and question counter



        self.top_layout = QHBoxLayout()
        self.question_counter_label = QLabel("Question 1/10")
        self.question_counter_label.setFont(QFont('Press Start 2P', 14))
        self.question_counter_label.setAlignment(Qt.AlignCenter)
        self.question_counter_label.setStyleSheet("""
                                                  color: white; margin-right: 20px;
                                                  """)
        self.top_layout.addWidget(self.question_counter_label, 1)

        self.score_label = QLabel("Score: 0")
        self.score_label.setFont(QFont('Press Start 2P', 10))
        self.score_label.setAlignment(Qt.AlignRight)
        self.score_label.setStyleSheet("background-color: #00000000; color:white;padding:0;")
        self.top_layout.addWidget(self.score_label)

        self.layout.addLayout(self.top_layout)

        self.options_group = QGroupBox()
        self.options_layout = QVBoxLayout()
        self.options_group.setLayout(self.options_layout)
        self.options_group.setStyleSheet("background-color:transparent;border:none;")



        # Question Text
        self.question_text = QLabel("Question will appear here")
        self.question_text.setFont(QFont('Press Start 2P', 10, QFont.Bold))
        self.question_text.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.question_text, 1)
        self.question_text.setStyleSheet("color: white; padding: 10px; background-color: transparent;")

        self.options_group = QGroupBox()
        self.options_layout = QVBoxLayout()
        self.options_group.setLayout(self.options_layout)
        self.options_group.setStyleSheet("background-color: transparent; border: none;")

        self.option_buttons = []
        for i in range(4):
            # Get Letters using ASCII , 65 -> A , 66 - > B .....
            button = QPushButton("Option {}".format(chr(65 + i)))
            button.setFont(QFont('Press Start 2P', 16))
            self.option_buttons.append(button)
            self.options_layout.addWidget(button)
            self.option_buttons[i].setStyleSheet(button_style)
            self.option_buttons[i].clicked.connect(self.click_sound.play)  # Connect click sound
            self.option_buttons[i].enterEvent = lambda event, b=self.option_buttons[i]: self.play_hover_sound(event, b)
            button.clicked.connect(self.check_answer)

        self.layout.addWidget(self.options_group)
        self.central_widget.setLayout(self.layout)
        self.display_question()
       
        

    def play_hover_sound(self, event, button):
        self.hover_sound.play()
        return super(QPushButton, button).enterEvent(event)
    def backtolevelspage(self):
        process = QProcess(self)
        process.start("python", ["main_menu.py"])  # Placeholder for actual function
        self.hide()

    def update_timer(self):
        current_time = int(self.timer_label.text())
        if current_time > 0:
            self.timer_label.setText(str(current_time - 1))
        else:
            QMessageBox.information(self, 'Time Out', 'Sorry, time is up for this question!', QMessageBox.Ok)
            self.next_question()

    def display_question(self):
        question = self.questions[self.current_question_index]
        self.question_text.setText(question['question'])
        self.question_counter_label.setText(f"Question {self.current_question_index+1}/{len(self.questions)}")
        for i, (key, option) in enumerate(question['options'].items()):
            self.option_buttons[i].setText(f"{key}. {option}")
            self.timer.start()
            self.timer_label.setText("30")  # Reset timer for new question

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            self.end_quiz()

    def check_answer(self):
        self.timer.stop()  # Stop the timer when a response is given
        clicked_button = self.sender()
        correct_answer = self.questions[self.current_question_index]['answer']
        selected_option = clicked_button.text().split('.')[0]

        if selected_option == correct_answer:
            self.score += 1
            self.score_label.setText(f"Score: {self.score}")
            QMessageBox.information(self, 'Correct!', 'You got it right!', QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Incorrect!', 'Oops, that was not correct.', QMessageBox.Ok)

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            QMessageBox.information(self, 'Quiz Finished', f'Your final score is {self.score}/{len(self.questions)}', QMessageBox.Ok)
            self.save_score()
            process = QProcess(self)
            process.start("python", ["main_menu.py"])
            self.hide()

    def end_quiz(self):
        QMessageBox.information(self, 'Quiz Finished', f'Your final score is {self.score}/{len(self.questions)}', QMessageBox.Ok)
        self.timer.stop()
        # Add functionality to save scores or return to a main menu as needed.

    # Additional methods such as saving scores or resetting the quiz can be added here.
    def save_score(self):
        score_record = {
            "score": self.score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level":"Cyber Attacks"
        }
        try:
            with open('scores.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        
        data.append(score_record)
        with open('scores.json', 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuizWindow(questions_cyberattacks)  # Pass the dictionary of questions here
    window.show()
    sys.exit(app.exec_())
