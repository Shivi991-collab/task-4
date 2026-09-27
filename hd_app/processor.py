import sys
import json
import os
from datetime import datetime

def process_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    result = {
        "processed_at": datetime.now().isoformat(),
        "item_count": len(data),
        "items": data
    }

    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"Processed {len(data)} items from {input_file}")
    print(f"Output written to {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python processor.py <input_file> <output_file>")
        sys.exit(1)
    process_data(sys.argv[1], sys.argv[2])