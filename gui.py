import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTextEdit
from malware_scanner import compile_yara_rules, scan_files, generate_report

class MalwareScannerApp(QWidget):
    def _init_(self):
        super()._init_()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.scan_button = QPushButton("Scan Directory")
        self.scan_button.clicked.connect(self.scan_directory)
        layout.addWidget(self.scan_button)

        self.report_text = QTextEdit(self)
        layout.addWidget(self.report_text)

        self.setLayout(layout)
        self.setWindowTitle('Malware Scanner')
        self.show()

    def scan_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory to Scan")
        if directory:
            yara_rules = compile_yara_rules()
            matches = scan_files(directory, yara_rules)
            generate_report(matches)
            with open("report.txt", "r") as report_file:
                self.report_text.setText(report_file.read())

if _name_ == "_main_":
    app = QApplication(sys.argv)
    ex = MalwareScannerApp()
    sys.exit(app.exec_())
