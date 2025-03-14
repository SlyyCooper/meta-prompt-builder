"""
Caption Creator Module

This module provides functionality to generate detailed system prompts
for language models based on user input.

Dependencies:
- meta_prompt.py: Contains the META_PROMPT template
"""

from openai import OpenAI
from ..prompts.default_meta_prompt import META_PROMPT

client = OpenAI()

def generate_prompt(meta_prompt: str, test_input: str = None):
    """
    Generate a detailed system prompt based on user input.
    
    Args:
        meta_prompt (str): The meta prompt to use for generation
        test_input (str, optional): The test input to use with the meta prompt
        
    Returns:
        str: The generated system prompt
    """
    # If no test input is provided, use the meta prompt as the task
    if test_input is None or test_input.strip() == "":
        task_content = "Task, Goal, or Current Prompt:\n" + meta_prompt
    else:
        task_content = "Task, Goal, or Current Prompt:\n" + test_input
    
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": meta_prompt,
            },
            {
                "role": "user",
                "content": task_content,
            },
        ],
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # If argument is provided, use it as the task or prompt
        task_or_prompt = sys.argv[1]
    else:
        # Otherwise, prompt the user for input
        print("Enter your task or prompt (press Ctrl+D or Ctrl+Z on a new line to finish):")
        task_or_prompt = sys.stdin.read().strip()
    
    if task_or_prompt:
        result = generate_prompt(META_PROMPT, task_or_prompt)
        print(result)
    else:
        print("No input provided. Exiting.")