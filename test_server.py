#this is a python script that check 20 connection from the server 
!/usr/bin/env python3
"""
Test script for concurrent HTTP server
Makes multiple simultaneous connections to verify concurrent handling
"""

import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import re

SERVER_URL = "http://localhost:8080"
NUM_CONNECTIONS = 20

def make_request(request_num):
    """Make a single HTTP request and extract the process ID"""
    try:
        start_time = time.time()

        with urllib.request.urlopen(SERVER_URL, timeout=5) as response:
            html = response.read().decode('utf-8')
            elapsed = time.time() - start_time

            # Extract the process ID from the HTML response
            match = re.search(r'process:\s*<strong>(\d+)</strong>', html)
            pid = match.group(1) if match else "Unknown"

            return {
                'request_num': request_num,
                'pid': pid,
                'status': response.status,
                'elapsed': elapsed,
                'success': True
            }
4
    except urllib.error.URLError as e:
        return {
            'request_num': request_num,
            'pid': None,
            'status': None,
            'elapsed': 0,
            'success': False,
            'error': str(e)
        }
    except Exception as e:
        return {
            'request_num': request_num,
            'pid': None,
            'status': None,
            'elapsed': 0,
            'success': False,
            'error': str(e)
        }

def main():
    print(f"Testing concurrent server at {SERVER_URL}")
    print(f"Making {NUM_CONNECTIONS} simultaneous connections...\n")

    results = []
    start_total = time.time()

    # Use ThreadPoolExecutor to make concurrent requests
    with ThreadPoolExecutor(max_workers=NUM_CONNECTIONS) as executor:
        # Submit all requests at once
        futures = {executor.submit(make_request, i): i for i in range(1, NUM_CONNECTIONS + 1)}

        # Collect results as they complete
        for future in as_completed(futures):
            result = future.result()
            results.append(result)

            if result['success']:
                print(f"✓ Request {result['request_num']:2d}: PID {result['pid']:>6s} | "
                      f"{result['elapsed']:.3f}s | Status {result['status']}")
            else:
                print(f"✗ Request {result['request_num']:2d}: FAILED - {result['error']}")

    total_time = time.time() - start_total

    # Summary statistics
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]

    print(f"Total requests:     {NUM_CONNECTIONS}")
    print(f"Successful:         {len(successful)}")
    print(f"Failed:             {len(failed)}")
    print(f"Total time:         {total_time:.3f}s")

    if successful:
