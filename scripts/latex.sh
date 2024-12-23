#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <markdown_file>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found"
    exit 1
fi

sed -i 's/\\(/\\\\(/g; s/\\)/\\\\)/g; s/\\\[/\\\\\[/g; s/\\\]/\\\\\]/g' "$1"