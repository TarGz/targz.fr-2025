#!/usr/bin/env python3
import os
import re
from pathlib import Path

posts_dir = Path("/Users/jterraz/Documents/GIT/targz.fr-2025/_posts")

def fix_post_title(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Skip if not portfolio
    if 'category: portfolio' not in content:
        return
    
    # Extract current frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return
        
    frontmatter = parts[1].strip()
    body = parts[2]
    
    # Find current title
    title_match = re.search(r'title: "([^"]+)"', frontmatter)
    if not title_match:
        return
        
    current_title = title_match.group(1)
    
    # Check if title was modified (contains " - Algorithmic")
    if " - Algorithmic Pen Plotted Art | Targz" in current_title:
        # Extract original title
        original_title = current_title.replace(" - Algorithmic Pen Plotted Art | Targz", "")
        
        # Replace the frontmatter
        new_frontmatter = re.sub(
            r'title: "([^"]+)"',
            f'title: "{original_title}"\nseo:\n  title: "{current_title}"',
            frontmatter
        )
        
        # Reconstruct content
        new_content = '---\n' + new_frontmatter + '\n---' + body
        
        # Write back
        with open(filepath, 'w') as f:
            f.write(new_content)
        
        print(f"Fixed: {original_title}")

# Process all markdown files
for filepath in posts_dir.glob("*.md"):
    try:
        fix_post_title(filepath)
    except Exception as e:
        print(f"Error processing {filepath.name}: {e}")

print("Done fixing titles!")