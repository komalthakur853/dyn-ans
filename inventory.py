#!/usr/bin/env python

import json

inventory = {
    "ubuntu_hosts": {
        "hosts": ["10.1.3.51", "10.1.3.23", "10.1.3.138"]
    }
}

print(json.dumps(inventory))
