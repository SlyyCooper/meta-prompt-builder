"""
Comparison View Component

This file contains the ComparisonView widget, which provides a side-by-side layout
for comparing two meta prompts and their outputs.

Dependencies:
- PyQt6
- src.ui.prompt_editor: Contains the PromptEditor widget
- src.ui.output_display: Contains the OutputDisplay widget
- src.ui.reasoning_display: Contains the ReasoningDisplay widget
- src.ui.prompt_input: Contains the PromptInput widget
- src.service.caption_creator: Contains the generate_prompt function
- src.helpers.reasoning_parser: Contains the reasoning parsing functions
- src.helpers.ui_styles: Contains common UI styles
"""

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, 
    QPushButton, QSplitter, QLabel,
    QFrame, QTabWidget, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from .prompt_editor import PromptEditor
from .output_display import OutputDisplay
from .reasoning_display import ReasoningDisplay
from .prompt_input import PromptInput
from ..service.caption_creator import generate_prompt
from ..helpers.reasoning_parser import extract_reasoning
from ..helpers.ui_styles import STYLES, COLORS, FONTS, LAYOUT


class ComparisonView(QWidget):
    """
    Widget for side-by-side comparison of meta prompts and their outputs.
    """
    
    def __init__(self, parent=None):
        """
        Initialize the comparison view.
        
        Args:
            parent (QWidget): Parent widget
        """
        super().__init__(parent)
        self._init_ui()
        
    def _init_ui(self):
        """Set up the UI components"""
        # Main layout - remove outer margins completely
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # No margins
        main_layout.setSpacing(0)  # No spacing between components
        
        # Create a splitter for vertically resizable areas
        self.v_splitter = QSplitter(Qt.Orientation.Vertical)
        self.v_splitter.setChildrenCollapsible(False)
        self.v_splitter.setStyleSheet(STYLES["splitter"])
        self.v_splitter.setHandleWidth(4)  # Slightly wider handle for easier resizing
        
        # Top area - Prompt editors
        prompt_area = QWidget()
        prompt_layout = QHBoxLayout(prompt_area)
        prompt_layout.setContentsMargins(1, 1, 1, 1)  # Minimal margins
        prompt_layout.setSpacing(1)  # Minimal spacing
        
        # Create prompt editors
        self.prompt_editor_left = PromptEditor("Meta Prompt A")
        self.prompt_editor_right = PromptEditor("Meta Prompt B")
        
        # Create a horizontal splitter for the prompt editors
        h_splitter_top = QSplitter(Qt.Orientation.Horizontal)
        h_splitter_top.setChildrenCollapsible(False)
        h_splitter_top.setStyleSheet(STYLES["splitter"])
        h_splitter_top.setHandleWidth(4)  # Slightly wider handle for easier resizing
        h_splitter_top.addWidget(self.prompt_editor_left)
        h_splitter_top.addWidget(self.prompt_editor_right)
        h_splitter_top.setSizes([500, 500])  # Equal initial sizes
        
        # Add splitter to layout
        prompt_layout.addWidget(h_splitter_top)
        
        # Bottom area - Output and reasoning displays
        output_area = QWidget()
        output_layout = QHBoxLayout(output_area)
        output_layout.setContentsMargins(1, 1, 1, 1)  # Minimal margins
        output_layout.setSpacing(1)  # Minimal spacing
        
        # Create a horizontal splitter for the output displays
        h_splitter_bottom = QSplitter(Qt.Orientation.Horizontal)
        h_splitter_bottom.setChildrenCollapsible(False)
        h_splitter_bottom.setStyleSheet(STYLES["splitter"])
        h_splitter_bottom.setHandleWidth(4)  # Slightly wider handle for easier resizing
        
        # Left side output and reasoning - more compact
        left_output_container = QWidget()
        left_output_layout = QVBoxLayout(left_output_container)
        left_output_layout.setContentsMargins(1, 1, 1, 1)  # Minimal margins
        
        # Create tab widget for output and reasoning on left side - more compact
        self.left_tabs = QTabWidget()
        self.left_tabs.setStyleSheet(STYLES["tab_widget"])
        self.left_tabs.setTabPosition(QTabWidget.TabPosition.South)  # Move tabs to bottom for more editor space
        
        # Create output and reasoning displays for left side
        self.output_display_left = OutputDisplay("Output A")
        self.reasoning_display_left = ReasoningDisplay("Reasoning A")
        
        # Add displays to tabs - Output tab first (default)
        self.left_tabs.addTab(self.output_display_left, "Output")
        self.left_tabs.addTab(self.reasoning_display_left, "Reasoning")
        
        left_output_layout.addWidget(self.left_tabs)
        
        # Right side output and reasoning - more compact
        right_output_container = QWidget()
        right_output_layout = QVBoxLayout(right_output_container)
        right_output_layout.setContentsMargins(1, 1, 1, 1)  # Minimal margins
        
        # Create tab widget for output and reasoning on right side - more compact
        self.right_tabs = QTabWidget()
        self.right_tabs.setStyleSheet(STYLES["tab_widget"]) 
        self.right_tabs.setTabPosition(QTabWidget.TabPosition.South)  # Move tabs to bottom for more editor space
        
        # Create output and reasoning displays for right side
        self.output_display_right = OutputDisplay("Output B")
        self.reasoning_display_right = ReasoningDisplay("Reasoning B")
        
        # Add displays to tabs - Output tab first (default)
        self.right_tabs.addTab(self.output_display_right, "Output")
        self.right_tabs.addTab(self.reasoning_display_right, "Reasoning")
        
        right_output_layout.addWidget(self.right_tabs)
        
        # Add containers to splitter
        h_splitter_bottom.addWidget(left_output_container)
        h_splitter_bottom.addWidget(right_output_container)
        h_splitter_bottom.setSizes([500, 500])  # Equal initial sizes
        
        # Add splitter to layout
        output_layout.addWidget(h_splitter_bottom)
        
        # Add the main areas to the splitter
        self.v_splitter.addWidget(prompt_area)
        self.v_splitter.addWidget(output_area)
        
        # Set initial sizes (75% prompts, 25% output) - make editors much more dominant
        self.v_splitter.setSizes([750, 250])
        
        # Add the splitter to the main layout
        main_layout.addWidget(self.v_splitter)
        
        # Bottom section - Test input area (ultra compact)
        test_input_container = QFrame()
        test_input_container.setFrameShape(QFrame.Shape.StyledPanel)
        test_input_container.setStyleSheet(STYLES["control_container"])
        test_input_container.setFixedHeight(30)  # Set a fixed height to prevent expansion
        test_input_layout = QVBoxLayout(test_input_container)
        test_input_layout.setContentsMargins(0, 0, 0, 0)  # No margins
        test_input_layout.setSpacing(0)  # No spacing
        
        # Create prompt input with ultra compact style
        self.prompt_input = PromptInput(compact=True)
        test_input_layout.addWidget(self.prompt_input)
        
        # Add test input to main layout with minimum size policy
        main_layout.addWidget(test_input_container, 0)  # 0 stretch factor to prevent expansion
        
        # Control area with generate buttons - more compact
        control_area = QFrame()
        control_area.setFrameShape(QFrame.Shape.StyledPanel)
        control_area.setStyleSheet(STYLES["control_container"])
        control_area.setMaximumHeight(40)  # Limit height for more editor space
        control_layout = QHBoxLayout(control_area)
        control_layout.setContentsMargins(LAYOUT["padding_small"], LAYOUT["padding_tiny"], 
                                         LAYOUT["padding_small"], LAYOUT["padding_tiny"])
        
        # Generate buttons with improved styling
        self.generate_left_button = QPushButton("Generate A")  # Shorter label
        self.generate_left_button.setStyleSheet(STYLES["action_button"])
        self.generate_left_button.clicked.connect(self._generate_left)
        
        self.generate_right_button = QPushButton("Generate B")  # Shorter label
        self.generate_right_button.setStyleSheet(STYLES["action_button"])
        self.generate_right_button.clicked.connect(self._generate_right)
        
        self.generate_both_button = QPushButton("Generate Both")  # Shorter label
        self.generate_both_button.setStyleSheet(STYLES["primary_button"])
        self.generate_both_button.setFont(QFont(FONTS["sans"], FONTS["size_small"], QFont.Weight.Bold))
        self.generate_both_button.clicked.connect(self._generate_both)
        
        # Add buttons to layout
        control_layout.addWidget(self.generate_left_button)
        control_layout.addWidget(self.generate_right_button)
        control_layout.addStretch()
        control_layout.addWidget(self.generate_both_button)
        
        # Add control area to main layout
        main_layout.addWidget(control_area)
    
    def _generate_left(self):
        """Generate output for the left prompt"""
        prompt = self.prompt_editor_left.get_prompt()
        test_input = self.prompt_input.get_input()
        full_output = generate_prompt(prompt, test_input)
        
        # Extract reasoning if present
        reasoning, output = extract_reasoning(full_output)
        
        # Set output and reasoning
        self.output_display_left.set_output(output)
        self.reasoning_display_left.set_reasoning(reasoning)
        
        # Always show the output tab first, regardless of reasoning presence
        self.left_tabs.setCurrentWidget(self.output_display_left)
    
    def _generate_right(self):
        """Generate output for the right prompt"""
        prompt = self.prompt_editor_right.get_prompt()
        test_input = self.prompt_input.get_input()
        full_output = generate_prompt(prompt, test_input)
        
        # Extract reasoning if present
        reasoning, output = extract_reasoning(full_output)
        
        # Set output and reasoning
        self.output_display_right.set_output(output)
        self.reasoning_display_right.set_reasoning(reasoning)
        
        # Always show the output tab first, regardless of reasoning presence
        self.right_tabs.setCurrentWidget(self.output_display_right)
    
    def _generate_both(self):
        """Generate output for both prompts"""
        self._generate_left()
        self._generate_right() 