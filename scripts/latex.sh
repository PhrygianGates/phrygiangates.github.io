#!/bin/bash

# Check if argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <markdown_file>"
    exit 1
fi

# Check if file exists
if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found"
    exit 1
fi

# Use Perl to convert double backslashes back to single ones
perl -i -pe 's/\\\\(\(|\)|\[|\])/\\$1/g' "$1"

# Check if perl command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Failed to process file"
    exit 1
fi