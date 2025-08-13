#!/usr/bin/env python3
"""
Script to help download exhibition images.
Since the Notion images are behind authentication, you'll need to:
1. Visit the page: https://targz.fr/untitled-24ca48ebf7d780878601e0ee28775ed2
2. Save the images manually or provide alternative images
"""

import os

# Create placeholder info for the required images
exhibition_images = [
    {
        "filename": "a-plot-in-the-wild-preview.jpeg",
        "description": "A Plot in the Wild 2025 - Global video art exhibition",
        "source": "Image showing the video art installation or promotional material"
    },
    {
        "filename": "grand-palais-preview.jpeg", 
        "description": "Grand Palais 2025 - Constructivism group exhibition",
        "source": "Image of the Grand Palais venue or exhibition setup"
    },
    {
        "filename": "behind-the-lines-preview.jpeg",
        "description": "Behind The Lines 2025 - Live installation at Lodève",
        "source": "Image of the transparent glass installation or pen plotter in action"
    },
    {
        "filename": "the-bitcoin-genesis-exhibition-preview.jpeg",
        "description": "The Bitcoin Genesis Exhibition 2022",
        "source": "Image of the Bitcoin Genesis artwork"
    },
    {
        "filename": "chunk-of-maze-preview.jpeg",
        "description": "Chunk of Maze 2022 - Algorithmic maze patterns",
        "source": "Image of the maze artwork"
    },
    {
        "filename": "blended-squares-exhibition-preview.jpeg",
        "description": "Blended Squares Exhibition 2021",
        "source": "Image from the Blended Squares series exhibition"
    },
    {
        "filename": "fill-the-blank-preview.jpeg",
        "description": "Fill The Blank 2018 - Interactive typography installation",
        "source": "Image of the interactive installation with Billund Mono Sans font"
    }
]

print("Exhibition images needed:")
print("-" * 50)
for img in exhibition_images:
    print(f"\nFilename: {img['filename']}")
    print(f"Description: {img['description']}")
    print(f"Source: {img['source']}")

print("\n" + "=" * 50)
print("Please add these images to: /assets/images/")
print("\nYou can:")
print("1. Use existing artwork images from your portfolio")
print("2. Download from the original page manually")
print("3. Create new preview images for each exhibition")

# For exhibitions that might use existing portfolio images:
suggestions = """
Suggested mappings from existing images:
- the-bitcoin-genesis-exhibition-preview.jpeg → Could use: the-bitcoin-genesis-preview.jpeg (if it exists)
- blended-squares-exhibition-preview.jpeg → Could use any blended-squares-n-XX-preview.jpeg
- chunk-of-maze-preview.jpeg → Create or find a maze pattern image
"""

print("\n" + suggestions)