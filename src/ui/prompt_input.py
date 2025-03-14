"""
Prompt Input Component

This file contains the PromptInput widget, which provides a text area for entering
test input that can be used with the meta prompts.

Dependencies:
- PyQt6
- src.helpers.ui_styles: Contains common UI styles
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPlainTextEdit, 
    QLabel, QHBoxLayout, QPushButton,
    QFrame, QSizePolicy, QGridLayout,
    QToolButton
)
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QFont
from ..helpers.ui_styles import STYLES, COLORS, FONTS, LAYOUT


class PromptInput(QWidget):
    """
    Widget for entering test input to be used with meta prompts.
    
    Signals:
        input_changed: Emitted when the input text changes
    """
    
    input_changed = pyqtSignal(str)
    
    def __init__(self, compact=False, parent=None):
        """
        Initialize the prompt input.
        
        Args:
            compact (bool): Whether to use compact mode
            parent (QWidget): Parent widget
        """
        super().__init__(parent)
        self.compact = compact
        self._init_ui()
        
    def _init_ui(self):
        """Set up the UI components"""
        # Ultra compact layout - single row with all elements
        if self.compact:
            # Use grid layout for ultra compact mode
            layout = QHBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)  # Zero margins
            layout.setSpacing(1)  # Minimal spacing
            
            # Compact label
            title_label = QLabel("Test:")
            title_label.setStyleSheet(f"font-size: {FONTS['size_small']}px; font-weight: 500; color: {COLORS['text_primary']};")
            title_label.setFixedWidth(30)  # Just enough for the word "Test:"
            layout.addWidget(title_label)
            
            # Text editor with minimal height
            self.text_editor = QPlainTextEdit()
            self.text_editor.setPlaceholderText("Enter test input here...")
            self.text_editor.textChanged.connect(self._on_text_changed)
            self.text_editor.setMaximumHeight(24)  # Even smaller height
            self.text_editor.setMinimumHeight(24)  # Fixed height
            
            # Set font and styling for editor
            editor_font = QFont(FONTS["monospace"], FONTS["size_small"])
            editor_font.setStyleHint(QFont.StyleHint.Monospace)
            self.text_editor.setFont(editor_font)
            
            # Set editor styling for ultra compact mode
            self.text_editor.setStyleSheet(f"""
                QPlainTextEdit {{
                    background-color: {COLORS["background"]};
                    border: 1px solid {COLORS["border"]};
                    border-radius: 2px;
                    padding: 1px 2px;
                    selection-background-color: {COLORS["selection"]};
                }}
            """)
            
            layout.addWidget(self.text_editor, 1)  # Give text editor stretch priority
            
            # Action buttons as tool buttons to save space
            self.clear_button = QToolButton()
            self.clear_button.setText("×")  # × symbol for clear
            self.clear_button.setToolTip("Clear input")
            self.clear_button.setFixedSize(18, 18)  # Smaller square button
            self.clear_button.setStyleSheet(f"""
                QToolButton {{
                    background-color: transparent;
                    border: none;
                    color: {COLORS['text_secondary']};
                    font-size: {FONTS['size_normal']}px;
                }}
                QToolButton:hover {{
                    color: {COLORS['accent']};
                }}
            """)
            self.clear_button.clicked.connect(self._clear_input)
            
            self.example_button = QToolButton()
            self.example_button.setText("≡")  # ≡ symbol for example
            self.example_button.setToolTip("Load example")
            self.example_button.setFixedSize(18, 18)  # Smaller square button
            self.example_button.setStyleSheet(f"""
                QToolButton {{
                    background-color: transparent;
                    border: none;
                    color: {COLORS['text_secondary']};
                    font-size: {FONTS['size_normal']}px;
                }}
                QToolButton:hover {{
                    color: {COLORS['accent']};
                }}
            """)
            self.example_button.clicked.connect(self._load_example)
            
            # Add buttons to layout
            layout.addWidget(self.clear_button)
            layout.addWidget(self.example_button)
        
        else:
            # Standard mode - still more compact than original
            layout = QVBoxLayout(self)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            
            # Compact header
            header = QWidget()
            header.setFixedHeight(28)
            header.setStyleSheet(f"background-color: {COLORS['panel_bg']}; border: 1px solid {COLORS['border']}; border-bottom: none;")
            
            header_layout = QHBoxLayout(header)
            header_layout.setContentsMargins(5, 0, 5, 0)
            
            # Title label
            title_label = QLabel("Test Input")
            title_label.setStyleSheet(f"font-weight: 600; font-size: {FONTS['size_small']}px; color: {COLORS['text_primary']};")
            
            # Action buttons in header
            self.clear_button = QToolButton()
            self.clear_button.setText("Clear")
            self.clear_button.setToolTip("Clear input")
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
            """)
            self.clear_button.clicked.connect(self._clear_input)
            
            self.example_button = QToolButton()
            self.example_button.setText("Load Example")
            self.example_button.setToolTip("Load an example input")
            self.example_button.setStyleSheet(f"""
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
            self.example_button.clicked.connect(self._load_example)
            
            header_layout.addWidget(title_label)
            header_layout.addStretch()
            header_layout.addWidget(self.clear_button)
            header_layout.addWidget(self.example_button)
            
            # Text editor
            self.text_editor = QPlainTextEdit()
            self.text_editor.setPlaceholderText("Enter test input here to use with the meta prompts...")
            self.text_editor.textChanged.connect(self._on_text_changed)
            
            # Set font and styling for editor
            editor_font = QFont(FONTS["monospace"], FONTS["size_normal"])
            editor_font.setStyleHint(QFont.StyleHint.Monospace)
            self.text_editor.setFont(editor_font)
            
            # Set editor styling
            self.text_editor.setStyleSheet(f"""
                QPlainTextEdit {{
                    background-color: {COLORS["background"]};
                    border: 1px solid {COLORS["border"]};
                    border-top: none;
                    padding: 4px;
                    selection-background-color: {COLORS["selection"]};
                }}
            """)
            
            # Make the editor expand to fill available space
            self.text_editor.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            
            # Add widgets to layout
            layout.addWidget(header)
            layout.addWidget(self.text_editor, 1)
        
    def get_input(self):
        """
        Get the current input text.
        
        Returns:
            str: The current input text
        """
        return self.text_editor.toPlainText()
    
    def set_input(self, text):
        """
        Set the input text.
        
        Args:
            text (str): The text to set
        """
        self.text_editor.setPlainText(text)
    
    def _clear_input(self):
        """Clear the input text"""
        self.text_editor.clear()
    
    def _load_example(self):
        """Load an example input"""
        example_text = """Create a system prompt for an AI assistant that helps users write effective emails.

The assistant should:
1. Help users craft professional emails with clear subject lines
2. Suggest appropriate greetings and closings based on the context
3. Provide templates for common email types (request, follow-up, introduction)
4. Offer guidance on tone and formality based on the recipient
5. Help with proofreading and suggesting improvements

The assistant should be friendly, helpful, and focus on making email writing easier and more effective."""
        self.set_input(example_text)
    
    def _on_text_changed(self):
        """Handle text changes and emit signal"""
        self.input_changed.emit(self.get_input())
