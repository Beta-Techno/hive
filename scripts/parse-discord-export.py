#!/usr/bin/env python3

"""
Temporary script to parse Discord export data
This will be removed once we connect to the Discord API
"""

import re
import json
from pathlib import Path

def parse_discord_export(file_path):
    """Parse Discord export file and return structured messages"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines and process
    lines = content.split('\n')
    messages = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Skip standalone "Image" entries
        if line == "Image":
            i += 1
            continue
        
        # Check for regular user message format: [8:41 PM]nickbg: message
        user_message_match = re.match(r'^\[([^\]]+)\]([^:]+):\s*(.*)$', line)
        if user_message_match:
            timestamp = user_message_match.group(1)
            username = user_message_match.group(2).strip()
            content = user_message_match.group(3).strip()
            
            # Check for multiline content
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r'^\[', lines[i]) and not re.match(r'^[0-9]', lines[i]):
                next_line = lines[i].strip()
                # Skip OP lines and timestamps
                if next_line != "OP" and not re.match(r'^\[?[0-9]', next_line):
                    content += " " + next_line
                i += 1
            
            # Convert username to user ID
            user_id = username.lower().replace(' ', '-')
            
            messages.append({
                'id': len(messages) + 1,
                'authorId': user_id,
                'content': content,
                'timestamp': timestamp,
                'reactions': []
            })
            continue
        
        # Look for timestamp pattern: [8:41 PM] or 8:41 PM] (missing bracket)
        timestamp_match = re.match(r'^\[?([^\]]+)\]$', line)
        if timestamp_match:
            timestamp = timestamp_match.group(1)
            
            # Check if next line is "OP"
            if i + 1 < len(lines) and lines[i + 1].strip() == 'OP':
                # This is an OP message, skip to the actual message
                i += 2
                if i < len(lines):
                    message_line = lines[i].strip()
                    # Parse: " Sato: message content"
                    message_match = re.match(r'^\s*([^:]+):\s*(.*)$', message_line)
                    if message_match:
                        username = message_match.group(1).strip()
                        content = message_match.group(2).strip()
                        
                        # Check for multiline content after OP messages
                        i += 1
                        while i < len(lines) and lines[i].strip() and not re.match(r'^\[', lines[i]) and not re.match(r'^[0-9]', lines[i]):
                            next_line = lines[i].strip()
                            # Skip OP lines and timestamps
                            if next_line != "OP" and not re.match(r'^\[?[0-9]', next_line):
                                content += " " + next_line
                            i += 1
                        
                        # Convert username to user ID
                        user_id = username.lower().replace(' ', '-')
                        
                        messages.append({
                            'id': len(messages) + 1,
                            'authorId': user_id,
                            'content': content,
                            'timestamp': timestamp,
                            'reactions': []
                        })
            else:
                # This might be a regular user message on next line
                if i + 1 < len(lines):
                    message_line = lines[i + 1].strip()
                    # Parse: "nickbg: message content"
                    message_match = re.match(r'^([^:]+):\s*(.*)$', message_line)
                    if message_match:
                        username = message_match.group(1).strip()
                        content = message_match.group(2).strip()
                        
                        # Check for multiline content
                        i += 2
                        while i < len(lines) and lines[i].strip() and not re.match(r'^\[', lines[i]) and not re.match(r'^[0-9]', lines[i]):
                            next_line = lines[i].strip()
                            # Skip OP lines and timestamps
                            if next_line != "OP" and not re.match(r'^\[?[0-9]', next_line):
                                content += " " + next_line
                            i += 1
                        
                        # Convert username to user ID
                        user_id = username.lower().replace(' ', '-')
                        
                        messages.append({
                            'id': len(messages) + 1,
                            'authorId': user_id,
                            'content': content,
                            'timestamp': timestamp,
                            'reactions': []
                        })
                    else:
                        i += 1
                else:
                    i += 1
        else:
            i += 1
    
    return messages

def convert_to_channel_format(messages):
    """Convert messages to our channel JSON format"""
    return {
        'messages': [
            {
                'id': str(msg['id']),
                'authorId': msg['authorId'],
                'content': msg['content'],
                'timestamp': msg['timestamp'],
                'reactions': msg['reactions']
            }
            for msg in messages
        ]
    }

def main():
    # Parse the Discord export
    messages = parse_discord_export('import.txt')
    
    # Convert to our format
    channel_data = convert_to_channel_format(messages)
    
    # Write to output file
    output_path = Path('src/data/channels/parsed-discord.json')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(channel_data, f, indent=2, ensure_ascii=False)
    
    print(f"Parsed {len(messages)} messages")
    print(f"Output written to: {output_path}")
    
    # Show some stats
    user_counts = {}
    for msg in messages:
        user_counts[msg['authorId']] = user_counts.get(msg['authorId'], 0) + 1
    
    print("\nUser message counts:")
    for user, count in sorted(user_counts.items()):
        print(f"  {user}: {count} messages")

if __name__ == '__main__':
    main()
