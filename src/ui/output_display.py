"""
Output Display Component

This file contains the OutputDisplay widget, which provides a read-only text area 
for displaying generated outputs from meta prompts.

Dependencies:
- PyQt6
- src.helpers.syntax_highlighter: Contains the syntax highlighter for the display
- src.helpers.ui_styles: Contains common UI styles
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, 
    QLabel, QHBoxLayout, QPushButton,
    QFrame, QSizePolicy, QToolButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication, QFont
from ..helpers.syntax_highlighter import PromptSyntaxHighlighter
from ..helpers.ui_styles import STYLES, COLORS, FONTS, LAYOUT


class OutputDisplay(QWidget):
    """Widget for displaying generated output text in a read-only format"""
    
    def __init__(self, title="Generated Output", parent=None):
        """
        Initialize the output display.
        
        Args:
            title (str): Title for the display
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
        
        # Compact header with title and action buttons
        header = QWidget()
        header.setFixedHeight(28)  # Fixed compact height
        header.setStyleSheet(f"background-color: {COLORS['panel_bg']}; border: 1px solid {COLORS['border']}; border-bottom: none;")
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(5, 0, 5, 0)  # Minimal horizontal padding only
        
        # Title label with smaller font
        title_label = QLabel(self.title)
        title_label.setStyleSheet(f"font-weight: 600; font-size: {FONTS['size_small']}px; color: {COLORS['text_primary']};")
        
        # Action buttons in the header - more compact
        self.copy_button = QToolButton()
        self.copy_button.setText("Copy")
        self.copy_button.setToolTip("Copy to clipboard")
        self.copy_button.setStyleSheet(f"""
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
            QToolButton:disabled {{
                color: {COLORS['disabled_text']};
            }}
        """)
        self.copy_button.clicked.connect(self._copy_to_clipboard)
        self.copy_button.setEnabled(False)
        
        self.clear_button = QToolButton()
        self.clear_button.setText("Clear")
        self.clear_button.setToolTip("Clear output")
        self.clear_button.setStyleSheet(f"""
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
            QToolButton:disabled {{
                color: {COLORS['disabled_text']};
            }}
        """)
        self.clear_button.clicked.connect(self._clear_output)
        self.clear_button.setEnabled(False)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.copy_button)
        header_layout.addWidget(self.clear_button)
        
        # Output display with improved styling
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText("Generated output will appear here...")
        
        # Set font for output - slightly smaller than before
        output_font = QFont(FONTS["monospace"], FONTS["size_normal"])
        output_font.setStyleHint(QFont.StyleHint.Monospace)
        self.output_text.setFont(output_font)
        
        # Set line spacing
        document = self.output_text.document()
        document.setDefaultStyleSheet("p, li { line-height: 1.4; }")  # Slightly tighter line spacing
        
        # Set output styling with tight padding for more content area
        self.output_text.setStyleSheet(f"""
            QTextEdit {{
                background-color: {COLORS["background"]};
                border: 1px solid {COLORS["border"]};
                border-top: none;
                padding: 4px;
                selection-background-color: {COLORS["selection"]};
            }}
        """)
        
        # Make the output expand to fill available space
        self.output_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # Apply syntax highlighting
        self.highlighter = PromptSyntaxHighlighter(self.output_text.document())
        
        # Add widgets to main layout
        layout.addWidget(header)
        layout.addWidget(self.output_text, 1)  # Give the output text a stretch factor of 1
        
    def set_output(self, text):
        """
        Set the output text.
        
        Args:
            text (str): The text to display
        """
        self.output_text.setPlainText(text)
        self.copy_button.setEnabled(bool(text))
        self.clear_button.setEnabled(bool(text))
        
    def get_output(self):
        """
        Get the current output text.
        
        Returns:
            str: The current output text
        """
        return self.output_text.toPlainText()
    
    def _copy_to_clipboard(self):
        """Copy the output text to the clipboard"""
        clipboard = self.output_text.document().toPlainText()
        if clipboard:
            # Use PyQt's clipboard
            QGuiApplication.clipboard().setText(clipboard)
    
    def _clear_output(self):
        """Clear the output text"""
        self.output_text.clear()
        self.copy_button.setEnabled(False)
        self.clear_button.setEnabled(False) 