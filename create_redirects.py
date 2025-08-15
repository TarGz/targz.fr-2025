#!/usr/bin/env python3
import csv
import os
from urllib.parse import urlparse

def create_redirect_pages():
    """
    Create Jekyll redirect pages based on the migration CSV file.
    Uses jekyll-redirect-from plugin to handle redirects.
    """
    
    csv_file = "migration/redirect.csv"
    redirect_dir = "redirects"
    
    # Create redirects directory if it doesn't exist
    os.makedirs(redirect_dir, exist_ok=True)
    
    created_redirects = []
    
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                from_url = row.get('from', '').strip()
                to_url = row.get('to', '').strip()
                
                # Skip empty rows or header-like content
                if not from_url or not to_url or 'https://targz.fr/' not in from_url:
                    continue
                
                # Extract the path from the old URL
                parsed = urlparse(from_url)
                old_path = parsed.path.lstrip('/')  # Remove leading slash
                
                if not old_path:
                    continue
                
                # Create safe filename (replace special chars)
                safe_filename = old_path.replace('/', '-').replace(' ', '-')
                redirect_file = os.path.join(redirect_dir, f"{safe_filename}.html")
                
                # Create the redirect page content
                redirect_content = f"""---
layout: page
permalink: /{old_path}/
redirect_to: {to_url}
sitemap: false
---

<!-- Redirect page for {from_url} -> {to_url} -->
<script>
  window.location.href = "{to_url}";
</script>

<p>If you are not redirected automatically, <a href="{to_url}">click here</a>.</p>
"""
                
                # Write the redirect file
                with open(redirect_file, 'w', encoding='utf-8') as f:
                    f.write(redirect_content)
                
                created_redirects.append({
                    'from': from_url,
                    'to': to_url,
                    'file': redirect_file,
                    'path': f"/{old_path}/"
                })
                
                print(f"Created redirect: /{old_path}/ -> {to_url}")
    
    except FileNotFoundError:
        print(f"Error: Could not find {csv_file}")
        return []
    except Exception as e:
        print(f"Error processing CSV: {e}")
        return []
    
    print(f"\nCreated {len(created_redirects)} redirect pages in {redirect_dir}/")
    
    # Create a summary file
    summary_file = os.path.join(redirect_dir, "README.md")
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("# URL Redirects\n\n")
        f.write("This folder contains redirect pages for old targz.fr URLs.\n\n")
        f.write("| Old URL | New URL | File |\n")
        f.write("|---------|---------|------|\n")
        
        for redirect in created_redirects:
            f.write(f"| `{redirect['path']}` | `{redirect['to']}` | `{redirect['file']}` |\n")
    
    return created_redirects

if __name__ == "__main__":
    print("Creating redirect pages from migration CSV...")
    redirects = create_redirect_pages()
    print(f"Done! Created {len(redirects)} redirect pages.")