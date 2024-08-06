#!/usr/bin/env python3

import json

def main():
    inventory = {
        "all": {
            "hosts": ["10.1.3.51", "10.1.3.23", "10.1.3.138"]
        }
    }
    print(json.dumps(inventory))

if __name__ == "__main__":
    main()
