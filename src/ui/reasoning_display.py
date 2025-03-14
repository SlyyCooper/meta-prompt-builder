"""
Reasoning Display Component

This file contains the ReasoningDisplay widget, which provides a read-only text area 
for displaying the reasoning section extracted from the meta prompt outputs.

Dependencies:
- PyQt6
- src.helpers.ui_styles: Contains common UI styles
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, 
    QLabel, QHBoxLayout, QPushButton,
    QFrame, QSizePolicy, QToolButton
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication, QFont
from ..helpers.ui_styles import STYLES, COLORS, FONTS, LAYOUT


class ReasoningDisplay(QWidget):
    """Widget for displaying reasoning text in a read-only format"""
    
    def __init__(self, title="Reasoning Analysis", parent=None):
        """
        Initialize the reasoning display.
        
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
        self.clear_button.setToolTip("Clear reasoning")
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
        self.clear_button.clicked.connect(self._clear_reasoning)
        self.clear_button.setEnabled(False)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.copy_button)
        header_layout.addWidget(self.clear_button)
        
        # Reasoning display with improved styling
        self.reasoning_text = QTextEdit()
        self.reasoning_text.setReadOnly(True)
        self.reasoning_text.setPlaceholderText("Reasoning analysis will appear here...")
        
        # Set font for reasoning
        reasoning_font = QFont(FONTS["monospace"], FONTS["size_normal"])
        reasoning_font.setStyleHint(QFont.StyleHint.Monospace)
        self.reasoning_text.setFont(reasoning_font)
        
        # Set line spacing
        document = self.reasoning_text.document()
        document.setDefaultStyleSheet("p, li { line-height: 1.4; }")  # Slightly tighter line spacing
        
        # Set reasoning styling with tight padding for more content area
        self.reasoning_text.setStyleSheet(f"""
            QTextEdit {{
                background-color: {COLORS["background"]};
                border: 1px solid {COLORS["border"]};
                border-top: none;
                padding: 4px;
                selection-background-color: {COLORS["selection"]};
            }}
        """)
        
        # Make the reasoning expand to fill available space
        self.reasoning_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # Add widgets to main layout
        layout.addWidget(header)
        layout.addWidget(self.reasoning_text, 1)  # Give the reasoning text a stretch factor of 1
        
    def set_reasoning(self, text):
        """
        Set the reasoning text.
        
        Args:
            text (str): The text to display
        """
        self.reasoning_text.setPlainText(text)
        self.copy_button.setEnabled(bool(text))
        self.clear_button.setEnabled(bool(text))
        
    def get_reasoning(self):
        """
        Get the current reasoning text.
        
        Returns:
            str: The current reasoning text
        """
        return self.reasoning_text.toPlainText()
    
    def _copy_to_clipboard(self):
        """Copy the reasoning text to the clipboard"""
        clipboard = self.reasoning_text.document().toPlainText()
        if clipboard:
            # Use PyQt's clipboard
            QGuiApplication.clipboard().setText(clipboard)
    
    def _clear_reasoning(self):
        """Clear the reasoning text"""
        self.reasoning_text.clear()
        self.copy_button.setEnabled(False)
        self.clear_button.setEnabled(False)