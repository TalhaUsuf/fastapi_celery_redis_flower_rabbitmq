import concurrent.futures
import requests
import json
import time

def make_post_request(i):
    url = 'http://localhost:8022/users'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "username": f"user{i}",
        "email": f"user{i}@example.com",
        "password": "1234"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return i, response.json()
    except requests.RequestException as e:
        return i, f"Request failed: {str(e)}"

def print_result(future):
    i, result = future.result()
    if isinstance(result, dict):
        print(f"Request {i} received: {json.dumps(result, indent=2)}")
    else:
        print(f"Request {i}: {result}")

def main():
    num_requests = 1000
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(make_post_request, i) for i in range(num_requests)]
        for future in concurrent.futures.as_completed(futures):
            print_result(future)

    end_time = time.time()
    print(f"\nCompleted {num_requests} requests in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()