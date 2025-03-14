"""
Reasoning Parser Module

This module provides functionality to parse out the <reasoning>...</reasoning> 
section from the output of the meta prompt.

Dependencies:
- re: For regular expression matching
"""

import re


def extract_reasoning(text):
    """
    Extract the reasoning section from the text.
    
    Args:
        text (str): The text to extract reasoning from
        
    Returns:
        tuple: (reasoning_text, remaining_text)
            - reasoning_text (str): The extracted reasoning text, or empty string if not found
            - remaining_text (str): The text with the reasoning section removed
    """
    if not text:
        return "", ""
    
    # Pattern to match <reasoning>...</reasoning> with any content in between
    # Using non-greedy matching with .*? to handle nested tags properly
    pattern = r'<reasoning>(.*?)</reasoning>'
    
    # Search for the pattern
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        reasoning_text = match.group(1).strip()
        
        # Remove the reasoning section from the original text
        remaining_text = re.sub(pattern, '', text, count=1, flags=re.DOTALL).strip()
        
        return reasoning_text, remaining_text
    
    # If no reasoning section found, return empty string for reasoning and original text
    return "", text


def has_reasoning(text):
    """
    Check if the text contains a reasoning section.
    
    Args:
        text (str): The text to check
        
    Returns:
        bool: True if the text contains a reasoning section, False otherwise
    """
    if not text:
        return False
    
    pattern = r'<reasoning>.*?</reasoning>'
    return bool(re.search(pattern, text, re.DOTALL))