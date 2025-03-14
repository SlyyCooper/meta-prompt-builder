"""
Prompt Editor Component

This file contains the PromptEditor widget, which provides a text editing area 
for modifying meta prompts with the ability to reset to default.

Dependencies:
- PyQt6
- src.prompts.default_meta_prompt: Contains the default meta prompt
- src.helpers.syntax_highlighter: Contains the syntax highlighter for the editor
- src.helpers.ui_styles: Contains common UI styles
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPlainTextEdit, 
    QPushButton, QLabel, QHBoxLayout,
    QSizePolicy, QFrame, QToolButton,
    QGridLayout
)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont, QColor, QPalette
from ..prompts.default_meta_prompt import META_PROMPT
from ..helpers.syntax_highlighter import PromptSyntaxHighlighter
from ..helpers.ui_styles import STYLES, COLORS, FONTS, LAYOUT


class PromptEditor(QWidget):
    """
    Widget for editing meta prompts with default text and reset functionality.
    
    Signals:
        prompt_changed: Emitted when the prompt text changes
    """
    
    prompt_changed = pyqtSignal(str)
    
    def __init__(self, title="Meta Prompt", parent=None):
        """
        Initialize the prompt editor with default text.
        
        Args:
            title (str): Title for the editor
            parent (QWidget): Parent widget
        """
        super().__init__(parent)
        self.title = title
        self._init_ui()
        
    def _init_ui(self):
        """Set up the UI components"""
        # Main layout - no margins for maximum space
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)  # No spacing between elements
        
        # Header with title and button in a more compact layout
        header = QWidget()
        header.setFixedHeight(28)  # Fixed compact height
        header.setStyleSheet(f"background-color: {COLORS['panel_bg']}; border: 1px solid {COLORS['border']}; border-bottom: none;")
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(5, 0, 5, 0)  # Minimal horizontal padding only
        
        # Title label with smaller font
        title_label = QLabel(self.title)
        title_label.setStyleSheet(f"font-weight: 600; font-size: {FONTS['size_small']}px; color: {COLORS['text_primary']};")
        
        # Reset button as a small tool button for less space usage
        self.reset_button = QToolButton()
        self.reset_button.setText("Reset")
        self.reset_button.setToolTip("Reset to default meta prompt")
        self.reset_button.setStyleSheet(f"""
            QToolButton {{
                background-color: transparent;
                border: none;
                color: {COLORS['text_secondary']};
                font-size: {FONTS['size_small']}px;
                padding: 2px 4px;
            }}
            QToolButton:hover {{
                color: {COLORS['accent']};
                text-decoration: underline;
            }}
        """)
        self.reset_button.clicked.connect(self._reset_to_default)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.reset_button)
        
        # Text editor with improved styling
        self.text_editor = QPlainTextEdit()
        self.text_editor.setPlainText(META_PROMPT)
        self.text_editor.textChanged.connect(self._on_text_changed)
        
        # Set font and styling for editor
        editor_font = QFont(FONTS["monospace"], FONTS["size_normal"])
        editor_font.setStyleHint(QFont.StyleHint.Monospace)
        self.text_editor.setFont(editor_font)
        
        # Set line spacing
        document = self.text_editor.document()
        document.setDefaultStyleSheet("p, li { line-height: 140%; }")
        
        # Set editor styling - maximize usable space
        self.text_editor.setStyleSheet(f"""
            QPlainTextEdit {{
                background-color: {COLORS["background"]};
                border: 1px solid {COLORS["border"]};
                border-top: none;
                border-bottom: none;
                padding: 4px;
                selection-background-color: {COLORS["selection"]};
            }}
        """)
        
        # Make the editor expand to fill all available space
        self.text_editor.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # Apply syntax highlighting
        self.highlighter = PromptSyntaxHighlighter(self.text_editor.document())
        
        # Add widgets to main layout
        layout.addWidget(header)
        layout.addWidget(self.text_editor, 1)  # Give the editor a stretch factor of 1
        
    def get_prompt(self):
        """
        Get the current prompt text.
        
        Returns:
            str: The current prompt text
        """
        return self.text_editor.toPlainText()
    
    def set_prompt(self, text):
        """
        Set the prompt text.
        
        Args:
            text (str): The text to set
        """
        self.text_editor.setPlainText(text)
    
    def _reset_to_default(self):
        """Reset the editor to the default meta prompt"""
        self.text_editor.setPlainText(META_PROMPT)
    
    def _on_text_changed(self):
        """Handle text changes and emit signal"""
        self.prompt_changed.emit(self.get_prompt()) 