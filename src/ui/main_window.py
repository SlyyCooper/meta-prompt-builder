"""
Main Window Module

This file contains the MainWindow class, which serves as the primary window
for the Meta Prompt Playground application.

Dependencies:
- PyQt6
- src.ui.comparison_view: Contains the ComparisonView widget
- src.helpers.ui_styles: Contains common UI styles
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, 
    QStatusBar, QMenuBar, QMenu, QApplication,
    QToolBar, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QFont

import json
import os
import sys

from .comparison_view import ComparisonView
from ..helpers.ui_styles import STYLES, COLORS, FONTS, LAYOUT


class MainWindow(QMainWindow):
    """
    Main window for the Meta Prompt Playground application.
    """
    
    def __init__(self):
        """Initialize the main window"""
        super().__init__()
        self.setWindowTitle("Meta Prompt Playground")
        self.setMinimumSize(1200, 800)  # Slightly smaller minimum size
        
        # Apply application-wide style
        self._apply_global_style()
        
        # Set up central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Main layout - no margins for maximum space
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)  # No margins
        self.layout.setSpacing(0)  # No spacing
        
        # Create comparison view
        self.comparison_view = ComparisonView()
        self.layout.addWidget(self.comparison_view)
        
        # Set up status bar - more compact
        self.status_bar = QStatusBar()
        self.status_bar.setMaximumHeight(22)  # Smaller height
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        self.status_bar.setStyleSheet(f"""
            QStatusBar {{
                background-color: {COLORS["background_alt"]};
                color: {COLORS["text_secondary"]};
                border-top: 1px solid {COLORS["border"]};
                padding: 1px 8px;
                font-size: {FONTS["size_small"]}px;
            }}
        """)
        
        # Set up menus
        self._create_menus()
        
        # Set up toolbar - more compact
        self._create_toolbar()
    
    def _apply_global_style(self):
        """Apply global application style"""
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {COLORS["background"]};
            }}
            QWidget {{
                font-family: {FONTS["sans"]};
                font-size: {FONTS["size_normal"]}px;
                color: {COLORS["text_primary"]};
            }}
            QMenuBar {{
                background-color: {COLORS["background_alt"]};
                border-bottom: 1px solid {COLORS["border"]};
                padding: 0px;
                min-height: 22px;
                max-height: 22px;
            }}
            QMenuBar::item {{
                padding: 3px 8px;
                background-color: transparent;
                border-radius: {LAYOUT["border_radius_small"]}px;
                margin: 1px 2px;
            }}
            QMenuBar::item:selected {{
                background-color: {COLORS["secondary_button_hover"]};
            }}
            QMenu {{
                background-color: {COLORS["background"]};
                border: 1px solid {COLORS["border"]};
                border-radius: {LAYOUT["border_radius_small"]}px;
                padding: 2px 0px;
            }}
            QMenu::item {{
                padding: 4px 20px 4px 16px;
                border-radius: 0px;
            }}
            QMenu::item:selected {{
                background-color: {COLORS["secondary_button_hover"]};
            }}
            QMenu::separator {{
                height: 1px;
                background-color: {COLORS["border"]};
                margin: 2px 5px;
            }}
            QToolBar {{
                background-color: {COLORS["background_alt"]};
                border-bottom: 1px solid {COLORS["border"]};
                spacing: 4px;
                padding: 1px 4px;
                min-height: 28px;
                max-height: 28px;
            }}
            QToolButton {{
                background-color: transparent;
                border: 1px solid transparent;
                border-radius: {LAYOUT["border_radius_small"]}px;
                padding: 3px;
            }}
            QToolButton:hover {{
                background-color: {COLORS["secondary_button_hover"]};
                border: 1px solid {COLORS["border"]};
            }}
            QToolButton:pressed {{
                background-color: {COLORS["secondary_button_hover"]};
                border: 1px solid {COLORS["border"]};
            }}
            QToolBar::separator {{
                width: 1px;
                background-color: {COLORS["border"]};
                margin: 4px 1px;
            }}
            QScrollBar:vertical {{
                background-color: {COLORS["background"]};
                width: 12px;  /* Slimmer scrollbar */
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background-color: {COLORS["secondary_button_border"]};
                min-height: 20px;
                border-radius: 3px;
                margin: 2px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: {COLORS["secondary_button_hover"]};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
            QScrollBar:horizontal {{
                background-color: {COLORS["background"]};
                height: 12px;  /* Slimmer scrollbar */
                margin: 0px;
            }}
            QScrollBar::handle:horizontal {{
                background-color: {COLORS["secondary_button_border"]};
                min-width: 20px;
                border-radius: 3px;
                margin: 2px;
            }}
            QScrollBar::handle:horizontal:hover {{
                background-color: {COLORS["secondary_button_hover"]};
            }}
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
                width: 0px;
            }}
            QMessageBox {{
                background-color: {COLORS["background"]};
            }}
            QMessageBox QLabel {{
                font-size: {FONTS["size_normal"]}px;
                color: {COLORS["text_primary"]};
            }}
            QMessageBox QPushButton {{
                background-color: {COLORS["secondary_button_bg"]};
                color: {COLORS["secondary_button_text"]};
                border: 1px solid {COLORS["secondary_button_border"]};
                border-radius: {LAYOUT["border_radius_small"]}px;
                padding: 4px 10px;
                font-size: {FONTS["size_small"]}px;
                min-width: 70px;
            }}
            QMessageBox QPushButton:hover {{
                background-color: {COLORS["secondary_button_hover"]};
            }}
            QSplitter::handle {{
                width: 4px;
                height: 4px;
            }}
            QSplitter::handle:hover {{
                background-color: {COLORS["accent"]};
            }}
            /* Make sure text inputs are properly styled */
            QLineEdit, QTextEdit, QPlainTextEdit {{
                background-color: {COLORS["background"]};
                border: 1px solid {COLORS["border"]};
                border-radius: {LAYOUT["border_radius_small"]}px;
                padding: 4px;
                selection-background-color: {COLORS["selection"]};
            }}
        """)
    
    def _create_menus(self):
        """Create menu bar and menus"""
        # Menu bar - more compact
        menu_bar = QMenuBar()
        menu_bar.setMaximumHeight(22)  # Smaller height
        self.setMenuBar(menu_bar)
        
        # File menu
        file_menu = QMenu("&File", self)
        menu_bar.addMenu(file_menu)
        
        # File menu actions
        save_action = QAction("&Save Prompts", self)  # Shorter text
        save_action.setStatusTip("Save both prompts to a file")
        save_action.triggered.connect(self._save_prompts)
        file_menu.addAction(save_action)
        
        load_action = QAction("&Load Prompts", self)  # Shorter text
        load_action.setStatusTip("Load prompts from a file")
        load_action.triggered.connect(self._load_prompts)
        file_menu.addAction(load_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("E&xit", self)
        exit_action.setStatusTip("Exit the application")
        exit_action.triggered.connect(QApplication.instance().quit)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = QMenu("&Help", self)
        menu_bar.addMenu(help_menu)
        
        # Help menu actions
        about_action = QAction("&About", self)
        about_action.setStatusTip("About the application")
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)
    
    def _create_toolbar(self):
        """Create toolbar with common actions - more compact"""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))  # Smaller icons
        toolbar.setMovable(False)
        toolbar.setMaximumHeight(28)  # Limit height
        self.addToolBar(toolbar)
        
        # Generate both button
        generate_both_action = QAction("Generate Both", self)
        generate_both_action.setStatusTip("Generate output for both prompts")
        generate_both_action.triggered.connect(self.comparison_view._generate_both)
        toolbar.addAction(generate_both_action)
        
        toolbar.addSeparator()
        
        # Save button
        save_action = QAction("Save", self)
        save_action.setStatusTip("Save both prompts to a file")
        save_action.triggered.connect(self._save_prompts)
        toolbar.addAction(save_action)
        
        # Load button
        load_action = QAction("Load", self)
        load_action.setStatusTip("Load prompts from a file")
        load_action.triggered.connect(self._load_prompts)
        toolbar.addAction(load_action)
    
    def _save_prompts(self):
        """Save both prompts to a JSON file"""
        # Get prompts
        prompt_a = self.comparison_view.prompt_editor_left.get_prompt()
        prompt_b = self.comparison_view.prompt_editor_right.get_prompt()
        output_a = self.comparison_view.output_display_left.get_output()
        output_b = self.comparison_view.output_display_right.get_output()
        reasoning_a = self.comparison_view.reasoning_display_left.get_reasoning()
        reasoning_b = self.comparison_view.reasoning_display_right.get_reasoning()
        test_input = self.comparison_view.prompt_input.get_input()
        
        # Create data structure
        data = {
            "prompt_a": prompt_a,
            "prompt_b": prompt_b,
            "output_a": output_a,
            "output_b": output_b,
            "reasoning_a": reasoning_a,
            "reasoning_b": reasoning_b,
            "test_input": test_input
        }
        
        # Get save path
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Save Prompts", 
            os.path.join(os.getcwd(), "src/saved_prompts"),
            "JSON Files (*.json)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=4)
                self.status_bar.showMessage(f"Saved to {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Save Error", f"Error saving file: {str(e)}")
    
    def _load_prompts(self):
        """Load prompts from a JSON file"""
        # Get load path
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Load Prompts", 
            os.path.join(os.getcwd(), "src/saved_prompts"),
            "JSON Files (*.json)"
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                
                # Set prompts and outputs
                if "prompt_a" in data:
                    self.comparison_view.prompt_editor_left.set_prompt(data["prompt_a"])
                if "prompt_b" in data:
                    self.comparison_view.prompt_editor_right.set_prompt(data["prompt_b"])
                if "output_a" in data:
                    self.comparison_view.output_display_left.set_output(data["output_a"])
                if "output_b" in data:
                    self.comparison_view.output_display_right.set_output(data["output_b"])
                if "reasoning_a" in data:
                    self.comparison_view.reasoning_display_left.set_reasoning(data["reasoning_a"])
                    # Always set output tab as default, regardless of reasoning presence
                    self.comparison_view.left_tabs.setCurrentWidget(self.comparison_view.output_display_left)
                if "reasoning_b" in data:
                    self.comparison_view.reasoning_display_right.set_reasoning(data["reasoning_b"])
                    # Always set output tab as default, regardless of reasoning presence
                    self.comparison_view.right_tabs.setCurrentWidget(self.comparison_view.output_display_right)
                if "test_input" in data:
                    self.comparison_view.prompt_input.set_input(data["test_input"])
                
                self.status_bar.showMessage(f"Loaded from {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Load Error", f"Error loading file: {str(e)}")
    
    def _show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self,
            "About Meta Prompt Playground",
            "Meta Prompt Playground\n\n"
            "A tool for creating and comparing meta prompts in a side-by-side format.\n\n"
            "AgenAI © 2025"
        ) 