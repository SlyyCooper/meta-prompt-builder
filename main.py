"""
Main entry point for the Meta Prompt Playground application.
This file serves as the primary interface for launching the application.

Dependencies:
- PyQt6
- src.ui.main_window: Contains the MainWindow class
"""

import sys
from PyQt6.QtWidgets import QApplication
from src.ui.main_window import MainWindow

def run_ui():
    """
    Run the PyQt6 user interface for the Meta Prompt Playground.
    """
    # PyQt6 handles high DPI scaling automatically
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

def run_cli():
    """
    Run the command-line interface for prompt generation.
    
    This is the legacy CLI mode, kept for backwards compatibility.
    """
    from src.service.caption_creator import generate_prompt
    
    if len(sys.argv) > 2:  # First arg is script name, second is --cli, third is the prompt
        # If argument is provided, use it as the task or prompt
        task_or_prompt = sys.argv[2]
    else:
        # Otherwise, prompt the user for input
        print("Enter your task or prompt (press Ctrl+D or Ctrl+Z on a new line to finish):")
        task_or_prompt = sys.stdin.read().strip()
    
    if task_or_prompt:
        result = generate_prompt(task_or_prompt)
        print(result)
    else:
        print("No input provided. Exiting.")

def main():
    """
    Main function that determines whether to run the UI or CLI version.
    
    If "--cli" is provided as the first argument, run in CLI mode.
    Otherwise, launch the UI.
    """
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_cli()
    else:
        run_ui()

if __name__ == "__main__":
    main()
