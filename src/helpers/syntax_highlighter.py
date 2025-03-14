"""
Syntax Highlighter Component

This file contains the PromptSyntaxHighlighter class, which provides syntax highlighting
for meta prompts in the editor, highlighting specific syntax elements like angle brackets,
square brackets, markdown headers, and bullet points.

Dependencies:
- PyQt6
"""

from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont


class PromptSyntaxHighlighter(QSyntaxHighlighter):
    """
    Syntax highlighter for meta prompts that highlights specific syntax elements:
    - Text inside angle brackets <...> (vibrant blue)
    - Text inside square brackets [...] (vibrant orange)
    - Markdown headers starting with # (rich red)
    - Bullet points starting with - (vibrant green)
    """
    
    def __init__(self, document):
        """
        Initialize the syntax highlighter with highlighting rules.
        
        Args:
            document (QTextDocument): The document to apply highlighting to
        """
        super().__init__(document)
        self._highlighting_rules = []
        
        # Format for text inside angle brackets <...> (vibrant blue)
        angle_bracket_format = QTextCharFormat()
        angle_bracket_format.setForeground(QColor("#0077FF"))  # Vibrant blue
        angle_bracket_format.setFontWeight(QFont.Weight.Bold)
        self._highlighting_rules.append((
            QRegularExpression("<[^>]*>"),
            angle_bracket_format
        ))
        
        # Format for text inside square brackets [...] (vibrant orange)
        square_bracket_format = QTextCharFormat()
        square_bracket_format.setForeground(QColor("#FF9500"))  # Vibrant orange
        square_bracket_format.setFontWeight(QFont.Weight.Bold)
        self._highlighting_rules.append((
            QRegularExpression("\\[[^\\]]*\\]"),
            square_bracket_format
        ))
        
        # Format for markdown headers (rich red)
        header_format = QTextCharFormat()
        header_format.setForeground(QColor("#E02020"))  # Rich red
        header_format.setFontWeight(QFont.Weight.Bold)
        header_format.setFontPointSize(14)  # Larger font for headers
        self._highlighting_rules.append((
            QRegularExpression("^#+ .*$"),
            header_format
        ))
        
        # Format for bullet points (vibrant green)
        bullet_format = QTextCharFormat()
        bullet_format.setForeground(QColor("#00B050"))  # Vibrant green
        bullet_format.setFontWeight(QFont.Weight.Bold)
        self._highlighting_rules.append((
            QRegularExpression("^- .*$"),
            bullet_format
        ))
    
    def highlightBlock(self, text):
        """
        Apply highlighting rules to the given block of text.
        
        Args:
            text (str): The text block to highlight
        """
        for pattern, format in self._highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
