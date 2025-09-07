#!/usr/bin/env python3
"""
Image Fetcher - A utility to download images from URLs
Implements Ubuntu principles: Community, Respect, Sharing, Practicality
"""

import os
import requests
from urllib.parse import urlparse, unquote
from pathlib import Path
import mimetypes
from datetime import datetime

def create_directory(directory_name):
    """Create directory if it doesn't exist"""
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"✓ Directory '{directory_name}' is ready")
        return True
    except OSError as e:
        print(f"✗ Error creating directory: {e}")
        return False

def extract_filename(url):
    """Extract filename from URL or generate one"""
    # Parse the URL to get the path
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)  # Handle URL encoded characters
    
    # Try to get filename from URL path
    if path and '/' in path:
        filename = path.split('/')[-1]
        if filename and '.' in filename:
            return filename
    
    # If no filename found in URL, generate one with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"image_{timestamp}.jpg"

def is_valid_image_url(url):
    """Check if the URL might point to an image"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff']
    return any(url.lower().endswith(ext) for ext in image_extensions)

def download_image(url, save_directory):
    """Download image from URL and save to directory"""
    try:
        # Send GET request with headers to mimic browser behavior
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0'
        }
        
        print(f"🌐 Connecting to {urlparse(url).netloc}...")
        response = requests.get(url, headers=headers, timeout=30, stream=True)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        # Check if content type is an image
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            print("⚠️  Warning: The URL doesn't seem to point to an image file")
            # Ask for confirmation to continue
            confirm = input("Do you want to continue anyway? (y/N): ").lower()
            if confirm != 'y':
                print("Download cancelled.")
                return False
        
        # Get filename
        content_disposition = response.headers.get('content-disposition', '')
        if 'filename=' in content_disposition:
            # Extract filename from content-disposition header
            filename = content_disposition.split('filename=')[-1].strip('"\'')
        else:
            # Try to get filename from URL or generate one
            filename = extract_filename(url)
            # Try to get extension from content type
            ext = mimetypes.guess_extension(content_type.split(';')[0])
            if ext and not filename.endswith(ext):
                if '.' in filename:
                    filename = filename.split('.')[0] + ext
                else:
                    filename += ext
        
        # Ensure filename is safe
        filename = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_', '.')).rstrip()
        if not filename:
            filename = f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Full path for saving
        save_path = os.path.join(save_directory, filename)
        
        # Check if file already exists
        counter = 1
        base_name, extension = os.path.splitext(save_path)
        while os.path.exists(save_path):
            save_path = f"{base_name}_{counter}{extension}"
            counter += 1
        
        # Download and save the image
        print(f"📥 Downloading: {filename}")
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        
        file_size = os.path.getsize(save_path)
        print(f"✅ Successfully saved: {filename} ({file_size} bytes)")
        print(f"📁 Location: {save_path}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
    except requests.exceptions.Timeout:
        print("❌ Request timed out")
    except requests.exceptions.TooManyRedirects:
        print("❌ Too many redirects")
    except IOError as e:
        print(f"❌ File system error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    
    return False

def main():
    """Main function"""
    print("=" * 50)
    print("🖼️  Image Fetcher - Ubuntu Principles Edition")
    print("=" * 50)
    print("Community: Connecting to the wider web")
    print("Respect:   Graceful error handling")
    print("Sharing:   Organized image collection")
    print("Practicality: Real-world utility")
    print("=" * 50)
    
    # Create directory for fetched images
    directory_name = "Fetched_Images"
    if not create_directory(directory_name):
        return
    
    while True:
        print("\n" + "-" * 30)
        try:
            # Get URL from user
            url = input("Enter image URL (or 'quit' to exit): ").strip()
            
            if url.lower() in ['quit', 'exit', 'q']:
                print("👋 Thank you for using Image Fetcher!")
                break
            
            if not url:
                print("⚠️  Please enter a valid URL")
                continue
            
            # Validate URL format
            if not url.startswith(('http://', 'https://')):
                print("⚠️  URL must start with http:// or https://")
                continue
            
            # Download the image
            download_image(url, directory_name)
            
        except KeyboardInterrupt:
            print("\n\n👋 Operation cancelled by user. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error in main loop: {e}")

if __name__ == "__main__":
    main()