import sys
import random
import json
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QGroupBox, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QProcess, QTimer
from PyQt5.QtMultimedia import QSound

# ...
questions_cryptography = {
    "1": {
        "question": "What is cryptography primarily used for in information security?",
        "options": {
            "A": "Speeding up data transfer",
            "B": "Making data unreadable to unauthorized users",
            "C": "Storing data",
            "D": "Deleting data",
        },
        "answer": "B",
    },
    "2": {
        "question": "What does 'AES' stand for in the context of encryption algorithms?",
        "options": {
            "A": "Advanced Encryption Standard",
            "B": "Automated Encryption System",
            "C": "Asymmetric Encryption Standard",
            "D": "Authorized Encryption Service",
        },
        "answer": "A",
    },
    "3": {
        "question": "Which type of cryptography uses the same key for both encryption and decryption?",
        "options": {
            "A": "Asymmetric cryptography",
            "B": "Symmetric cryptography",
            "C": "Hash functions",
            "D": "Public key infrastructure",
        },
        "answer": "B",
    },
    "4": {
        "question": "What is the main purpose of a digital signature in cybersecurity?",
        "options": {
            "A": "To enhance the appearance of digital documents",
            "B": "To verify the authenticity and integrity of a message",
            "C": "To encrypt email messages",
            "D": "To provide a decorative element in emails",
        },
        "answer": "B",
    },
    "5": {
        "question": "What does 'RSA' stand for, a common encryption and decryption algorithm?",
        "options": {
            "A": "Rivest, Shamir, and Adleman",
            "B": "Rapid Secure Access",
            "C": "Random Symmetric Algorithm",
            "D": "Reliable Security Application",
        },
        "answer": "A",
    },
    "6": {
        "question": "What is the primary function of the 'hash function' in cryptography?",
        "options": {
            "A": "To create a unique digital fingerprint of data",
            "B": "To encrypt large documents",
            "C": "To generate public and private keys",
            "D": "To recover lost data",
        },
        "answer": "A",
    },
    "7": {
        "question": "Which type of cryptographic algorithm involves a pair of keys – a public key and a private key?",
        "options": {
            "A": "Symmetric key cryptography",
            "B": "Asymmetric key cryptography",
            "C": "Hash cryptography",
            "D": "Quantum cryptography",
        },
        "answer": "B",
    },
    "8": {
        "question": "What is a common use of encryption in everyday internet use?",
        "options": {
            "A": "Verifying the user's age",
            "B": "Securing data transmitted over the internet",
            "C": "Increasing download speeds",
            "D": "Reducing the size of transmitted data",
        },
        "answer": "B",
    },
    "9": {
        "question": "What does 'SSL' stand for, a protocol for securing connections between networked computers?",
        "options": {
            "A": "Secure Socket Layer",
            "B": "Socket Security Layer",
            "C": "Secure System Login",
            "D": "System Socket Layer",
        },
        "answer": "A",
    },
    "10": {
        "question": "What is the term for the process of converting plaintext into ciphertext?",
        "options": {
            "A": "Decryption",
            "B": "Translation",
            "C": "Encryption",
            "D": "Compression",
        },
        "answer": "C",
    },
    "11": {
        "question": "What is meant by 'plaintext' in cryptography?",
        "options": {
            "A": "The original readable text or data that is fed into an algorithm",
            "B": "The encrypted version of a text",
            "C": "A special type of encoded script",
            "D": "The output of a decryption process",
        },
        "answer": "A",
    },
    "12": {
        "question": "What type of attack involves attempting every possible key on encrypted data until an intelligible translation is obtained?",
        "options": {
            "A": "Phishing attack",
            "B": "Denial of service attack",
            "C": "Brute force attack",
            "D": "Spoofing attack",
        },
        "answer": "C",
    },
    "13": {
        "question": "Which protocol uses encryption to secure the transmission of data over the internet?",
        "options": {
            "A": "HTTP",
            "B": "HTTPS",
            "C": "FTP",
            "D": "SMTP",
        },
        "answer": "B",
    },
    "14": {
        "question": "What does 'PGP' stand for, used for encrypting and decrypting communications?",
        "options": {
            "A": "Private Guarded Protection",
            "B": "Pretty Good Privacy",
            "C": "Protected Gateway Protocol",
            "D": "Public General Privacy",
        },
        "answer": "B",
    },
    "15": {
        "question": "Which concept in cryptography ensures that a message has not been altered?",
        "options": {
            "A": "Authentication",
            "B": "Confidentiality",
            "C": "Integrity",
            "D": "Non-repudiation",
        },
        "answer": "C",
    },
    "16": {
        "question": "What does the term 'non-repudiation' mean in the context of digital communications?",
        "options": {
            "A": "The process of making a system fail-safe",
            "B": "Ensuring that a user cannot deny the authenticity of their signature on a message",
            "C": "Confirming the sender's identity",
            "D": "Protecting private communications",
        },
        "answer": "B",
    },
    "17": {
        "question": "What is 'quantum cryptography' primarily focused on?",
        "options": {
            "A": "Using traditional algorithms for encryption",
            "B": "Using quantum mechanical properties to secure data",
            "C": "Improving the speed of cryptographic algorithms",
            "D": "Developing new hashing techniques",
        },
        "answer": "B",
    },
    "18": {
        "question": "What role does 'key distribution' play in secure communications?",
        "options": {
            "A": "It ensures that all parties have the correct hardware for communication",
            "B": "It involves sharing keys in a secure manner to facilitate encrypted communication",
            "C": "It decreases the security of transmitted data",
            "D": "It refers to the distribution of keyloggers in a network",
        },
        "answer": "B",
    },
    "19": {
        "question": "What is 'steganography' used for in the field of data security?",
        "options": {
            "A": "Encrypting text into ciphertext",
            "B": "Concealing the existence of data within another file or message",
            "C": "Creating secure communication channels",
            "D": "Improving the efficiency of encryption algorithms",
        },
        "answer": "B",
    },
    "20": {
        "question": "Which technology is considered a fundamental building block for secure cryptographic systems and digital signatures?",
        "options": {
            "A": "Public key infrastructure",
            "B": "Symmetric key encryption",
            "C": "Quantum computing",
            "D": "Blockchain technology",
        },
        "answer": "A",
    },
    "21": {
        "question": "What does 'Ciphertext' refer to in cryptography?",
        "options": {
            "A": "The decrypted form of a message",
            "B": "The encrypted form of a message",
            "C": "A specific type of cryptographic key",
            "D": "The algorithm used for encrypting data",
        },
        "answer": "B",
    },
    "22": {
        "question": "What type of cryptographic keys are used in a public key infrastructure?",
        "options": {
            "A": "One key for both encryption and decryption",
            "B": "Different keys for encryption and decryption shared privately",
            "C": "Different keys for encryption and decryption, one of which is public",
            "D": "A single key that changes with every session",
        },
        "answer": "C",
    },
    "23": {
        "question": "What is the primary advantage of using asymmetric cryptography over symmetric cryptography?",
        "options": {
            "A": "It requires less computational power",
            "B": "It is faster in processing large amounts of data",
            "C": "It does not require the secure exchange of a key",
            "D": "It uses simpler algorithms",
        },
        "answer": "C",
    },
    "24": {
        "question": "In the context of digital security, what does 'salting' refer to?",
        "options": {
            "A": "Adding random data to a password before hashing",
            "B": "Scanning a network for vulnerabilities",
            "C": "Filtering out unwanted data packets",
            "D": "Encrypting internet traffic",
        },
        "answer": "A",
    },
    "25": {
        "question": "Which cryptographic method is used to ensure that a message has come from a legitimate source?",
        "options": {
            "A": "Encryption",
            "B": "Decryption",
            "C": "Digital signature",
            "D": "Public key",
        },
        "answer": "C",
    },
    "26": {
        "question": "What is a 'cryptographic hash function'?",
        "options": {
            "A": "A function that recovers lost data",
            "B": "A function that encrypts and decrypts data",
            "C": "A function that provides a fixed-size hash value from variable-sized input data",
            "D": "A function used to generate keys",
        },
        "answer": "C",
    },
    "27": {
        "question": "What does the process of 'decryption' involve in cryptography?",
        "options": {
            "A": "Converting ciphertext back into plaintext",
            "B": "Converting plaintext into ciphertext",
            "C": "Verifying the authenticity of a message",
            "D": "Generating cryptographic keys",
        },
        "answer": "A",
    },
    "28": {
        "question": "What is the purpose of 'elliptic curve cryptography' in secure communications?",
        "options": {
            "A": "To provide a faster and more efficient method of encryption",
            "B": "To facilitate secure multi-party computation",
            "C": "To ensure that encrypted data can be read without a key",
            "D": "To decrease the security of data to allow for easier access",
        },
        "answer": "A",
    },
    "29": {
        "question": "What is meant by the 'Diffie-Hellman' algorithm in cryptography?",
        "options": {
            "A": "A method for secure key exchange over an insecure channel",
            "B": "A type of encryption algorithm for large files",
            "C": "A hashing function used for password security",
            "D": "An algorithm for compressing encrypted data",
        },
        "answer": "A",
    },
    "30": {
        "question": "Which aspect of data does 'confidentiality' protect in cryptography?",
        "options": {
            "A": "Ensuring that data is correct and unaltered",
            "B": "Ensuring that data can be accessed anytime",
            "C": "Preventing unauthorized access to data",
            "D": "Verifying the identity of users accessing data",
        },
        "answer": "C",
    },
}


class QuizWindow(QMainWindow):
    def __init__(self, questions):
        super().__init__()
        self.questions = random.sample(list(questions.values()), 10)  # Select 10 random questions
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
        process.start("python", ["level_form.py"])  # Placeholder for actual function
        self.hide()

    def update_timer(self):
        current_time = int(self.timer_label.text())
        if current_time > 0:
            self.timer_label.setText(str(current_time - 1))
        else:
            QMessageBox.information(self, 'Time Out', QMessageBox.Ok)
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
            "level": "Cryptography",
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
    window = QuizWindow(questions_cryptography)  # Pass the dictionary of questions here
    window.show()
    sys.exit(app.exec_())
