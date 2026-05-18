import sys
from PyQt6.QtWidgets import QApplication
from editor_window import CompilerWindow

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Compiler Project")
    app.setOrganizationName("StudentOrg")
    
    app.setStyle("Fusion")

    window = CompilerWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
