def calculate_text_height(content: str, min_height: int = 30) -> int:
    """Calculate the height needed for text content in a textbox"""
    lines = content.split('\n')
    total_lines = 0
    
    for line in lines:
        if len(line) == 0:
            total_lines += 1  # Empty line
        else:
            # Rough estimate: 100 characters per line (more realistic for chat width)
            estimated_wrapped = max(1, (len(line) + 99) // 100)
            total_lines += estimated_wrapped
    
    # Calculate compact height: 18px per line + minimal padding
    content_height = max(min_height, total_lines * 18 + 12)  # Minimum 30px, 18px per line + 12px padding
    return content_height
