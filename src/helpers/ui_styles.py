"""
UI Styles Module

This file contains common UI styles and constants that can be reused across
the application to maintain a consistent look and feel.

Dependencies:
- None
"""

# Color palette (more modern and visually appealing)
COLORS = {
    # Main backgrounds
    "background": "#ffffff",
    "background_alt": "#f6f8fa",  # Lighter blue-gray
    "panel_bg": "#f2f5f9",        # Slightly blue tinted background
    
    # Borders and dividers
    "border": "#dde1e6",          # Subtle gray
    "divider": "#e6eaef",         # Very light gray with blue tint
    
    # Text colors
    "text_primary": "#24292e",    # Almost black
    "text_secondary": "#57606a",  # Medium gray
    "text_tertiary": "#6e7781",   # Lighter gray
    "text_placeholder": "#8c959f", # Very light gray
    
    # Accent colors
    "accent": "#0969da",          # GitHub blue
    "accent_light": "#ddf4ff",    # Light blue
    "accent_hover": "#0860c1",    # Darker blue
    
    # Button colors
    "primary_button_bg": "#0969da",  # GitHub blue
    "primary_button_hover": "#0860c1", # Darker blue
    "primary_button_text": "#ffffff",
    
    "secondary_button_bg": "#f6f8fa",  # Light gray
    "secondary_button_hover": "#eaeef2",
    "secondary_button_text": "#24292e",
    "secondary_button_border": "#d0d7de",
    
    # Functional colors
    "success": "#2da44e",         # Green
    "warning": "#d4a72c",         # Yellow
    "error": "#cf222e",           # Red
    "selection": "#d8e8f9",       # Light blue
    
    # Disabled states
    "disabled_bg": "#f6f8fa",
    "disabled_text": "#8c959f",
    "disabled_border": "#d0d7de",
}

# Font settings
FONTS = {
    "monospace": "SF Mono, Menlo, Monaco, Consolas, 'Liberation Mono', monospace",
    "sans": "SF Pro, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
    "size_normal": 13,   # Reduced from 14
    "size_small": 12,    # Reduced from 13
    "size_tiny": 11,     # Reduced from 12
    "size_title": 14,    # Reduced from 16
    "line_height": 1.5,  # Slightly reduced for more compact display
}

# Layout constants - SIGNIFICANTLY reduced for a more sleek UI
LAYOUT = {
    "margin": 0,         # No outer margins
    "spacing": 4,        # Reduced from 10
    "padding_tiny": 2,   # Reduced from 5
    "padding_small": 4,  # Reduced from 10
    "padding_normal": 6, # Reduced from 15
    "padding_large": 10, # Reduced from 20
    "border_radius": 4,  # Reduced from 8
    "border_radius_small": 3, # Reduced from 5
}

# Common styles - updated for more compact appearance
STYLES = {
    # Standard containers
    "title_container": f"""
        QFrame {{
            background-color: {COLORS["panel_bg"]};
            border-top-left-radius: {LAYOUT["border_radius"]}px;
            border-top-right-radius: {LAYOUT["border_radius"]}px;
            border: 1px solid {COLORS["border"]};
            border-bottom: none;
        }}
    """,
    
    "title_label": f"""
        font-weight: 600;
        font-size: {FONTS["size_title"]}px;
        color: {COLORS["text_primary"]};
        padding: 2px 0;
    """,
    
    "content_area": f"""
        background-color: {COLORS["background"]};
        border: 1px solid {COLORS["border"]};
        border-top: none;
        border-bottom: none;
        padding: {LAYOUT["padding_small"]}px;
        selection-background-color: {COLORS["selection"]};
        line-height: {FONTS["line_height"]};
        font-size: {FONTS["size_normal"]}px;
    """,
    
    "button_container": f"""
        QFrame {{
            background-color: {COLORS["background_alt"]};
            border-bottom-left-radius: {LAYOUT["border_radius"]}px;
            border-bottom-right-radius: {LAYOUT["border_radius"]}px;
            border: 1px solid {COLORS["border"]};
            border-top: none;
        }}
    """,
    
    # Compact container styles for input area
    "compact_title_container": f"""
        QFrame {{
            background-color: {COLORS["panel_bg"]};
            border-top-left-radius: {LAYOUT["border_radius"]}px;
            border-top-right-radius: {LAYOUT["border_radius"]}px;
            border: 1px solid {COLORS["border"]};
            border-bottom: none;
            padding: 1px;
        }}
    """,
    
    "compact_title_label": f"""
        font-weight: 600;
        font-size: {FONTS["size_small"]}px;
        color: {COLORS["text_primary"]};
        padding: 1px 0;
    """,
    
    "compact_content_area": f"""
        background-color: {COLORS["background"]};
        border: 1px solid {COLORS["border"]};
        border-top: none;
        border-bottom: none;
        padding: 2px;
        selection-background-color: {COLORS["selection"]};
        line-height: 1.3;
    """,
    
    "compact_button_container": f"""
        QFrame {{
            background-color: {COLORS["background_alt"]};
            border-bottom-left-radius: {LAYOUT["border_radius"]}px;
            border-bottom-right-radius: {LAYOUT["border_radius"]}px;
            border: 1px solid {COLORS["border"]};
            border-top: none;
            padding: 1px;
        }}
    """,
    
    # Special containers
    "panel_container": f"""
        QFrame {{
            background-color: {COLORS["panel_bg"]};
            border-radius: {LAYOUT["border_radius"]}px;
            border: 1px solid {COLORS["border"]};
            margin-top: {LAYOUT["padding_tiny"]}px;
            margin-bottom: {LAYOUT["padding_tiny"]}px;
        }}
    """,
    
    "control_container": f"""
        QFrame {{
            background-color: {COLORS["panel_bg"]};
            border-radius: {LAYOUT["border_radius"]}px;
            border: 1px solid {COLORS["border"]};
            margin: 0;
            padding: 0;
        }}
    """,
    
    # Button styles
    "button": f"""
        QPushButton {{
            background-color: {COLORS["secondary_button_bg"]};
            color: {COLORS["secondary_button_text"]};
            border: 1px solid {COLORS["secondary_button_border"]};
            border-radius: {LAYOUT["border_radius_small"]}px;
            padding: 4px 8px;
            font-size: {FONTS["size_small"]}px;
            font-weight: 500;
        }}
        QPushButton:hover {{
            background-color: {COLORS["secondary_button_hover"]};
        }}
        QPushButton:pressed {{
            background-color: {COLORS["secondary_button_hover"]};
            border-color: {COLORS["border"]};
        }}
        QPushButton:disabled {{
            background-color: {COLORS["disabled_bg"]};
            color: {COLORS["disabled_text"]};
            border-color: {COLORS["disabled_border"]};
        }}
    """,
    
    "secondary_button": f"""
        QPushButton {{
            background-color: {COLORS["secondary_button_bg"]};
            color: {COLORS["secondary_button_text"]};
            border: 1px solid {COLORS["secondary_button_border"]};
            border-radius: {LAYOUT["border_radius_small"]}px;
            padding: 2px 6px;
            font-size: {FONTS["size_small"]}px;
        }}
        QPushButton:hover {{
            background-color: {COLORS["secondary_button_hover"]};
        }}
        QPushButton:pressed {{
            background-color: {COLORS["secondary_button_hover"]};
            border-color: {COLORS["border"]};
        }}
        QPushButton:disabled {{
            background-color: {COLORS["disabled_bg"]};
            color: {COLORS["disabled_text"]};
            border-color: {COLORS["disabled_border"]};
        }}
    """,
    
    "action_button": f"""
        QPushButton {{
            background-color: {COLORS["secondary_button_bg"]};
            color: {COLORS["secondary_button_text"]};
            border: 1px solid {COLORS["secondary_button_border"]};
            border-radius: {LAYOUT["border_radius_small"]}px;
            padding: 4px 10px;
            font-size: {FONTS["size_normal"]}px;
            font-weight: 500;
        }}
        QPushButton:hover {{
            background-color: {COLORS["secondary_button_hover"]};
        }}
        QPushButton:pressed {{
            background-color: {COLORS["secondary_button_hover"]};
            border-color: {COLORS["border"]};
        }}
        QPushButton:disabled {{
            background-color: {COLORS["disabled_bg"]};
            color: {COLORS["disabled_text"]};
            border-color: {COLORS["disabled_border"]};
        }}
    """,
    
    "primary_button": f"""
        QPushButton {{
            background-color: {COLORS["primary_button_bg"]};
            color: {COLORS["primary_button_text"]};
            border: 1px solid {COLORS["primary_button_bg"]};
            border-radius: {LAYOUT["border_radius_small"]}px;
            padding: 4px 10px;
            font-size: {FONTS["size_normal"]}px;
            font-weight: 500;
        }}
        QPushButton:hover {{
            background-color: {COLORS["primary_button_hover"]};
            border-color: {COLORS["primary_button_hover"]};
        }}
        QPushButton:pressed {{
            background-color: {COLORS["primary_button_hover"]};
            border-color: {COLORS["primary_button_hover"]};
        }}
        QPushButton:disabled {{
            background-color: {COLORS["disabled_bg"]};
            color: {COLORS["disabled_text"]};
            border-color: {COLORS["disabled_border"]};
        }}
    """,
    
    # Tab styling - more compact
    "tab_widget": f"""
        QTabWidget::pane {{
            border: 1px solid {COLORS["border"]};
            border-radius: {LAYOUT["border_radius"]}px;
            top: -1px;
        }}
        QTabBar::tab {{
            background-color: {COLORS["background_alt"]};
            border: 1px solid {COLORS["border"]};
            border-bottom: none;
            border-top-left-radius: {LAYOUT["border_radius_small"]}px;
            border-top-right-radius: {LAYOUT["border_radius_small"]}px;
            padding: 4px 10px;
            margin-right: 1px;
            color: {COLORS["text_secondary"]};
            font-weight: 500;
            font-size: {FONTS["size_small"]}px;
        }}
        QTabBar::tab:selected {{
            background-color: {COLORS["background"]};
            color: {COLORS["text_primary"]};
            border-bottom: 2px solid {COLORS["accent"]};
        }}
        QTabBar::tab:hover:!selected {{
            background-color: {COLORS["secondary_button_hover"]};
        }}
    """,
    
    # Splitter styling with more visible handles to facilitate resizing
    "splitter": f"""
        QSplitter::handle {{
            background-color: {COLORS["divider"]};
        }}
        QSplitter::handle:horizontal {{
            width: 2px;
            margin: 1px;
        }}
        QSplitter::handle:vertical {{
            height: 2px;
            margin: 1px;
        }}
        QSplitter::handle:hover {{
            background-color: {COLORS["accent"]};
        }}
    """,
}

def get_editor_font():
    """
    Returns a properly configured monospace font for text editors.
    
    Returns:
        str: CSS font-family string for editor components
    """
    return f"font-family: {FONTS['monospace']}; font-size: {FONTS['size_normal']}px; line-height: {FONTS['line_height']};" 