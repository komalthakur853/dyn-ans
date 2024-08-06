#!/usr/bin/env python3

import json

def inventory():
    return {
        "_meta": {
            "hostvars": {
                "ubuntu-1": {
                    "ansible_host": "10.1.3.51",
                    "ansible_user": "ubuntu"
                },
                "ubuntu-2": {
                    "ansible_host": "10.1.3.23",
                    "ansible_user": "ubuntu"
                },
                "ubuntu-3": {
                    "ansible_host": "10.1.3.138",
                    "ansible_user": "ubuntu"
                }
            }
        },
        "ubuntu": {
            "hosts": ["ubuntu-1", "ubuntu-2", "ubuntu-3"]
        }
    }

if __name__ == "__main__":
    inv = inventory()
    print(json.dumps(inv, indent=4))
