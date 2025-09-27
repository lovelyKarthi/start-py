"""Requests with retry and backoff (simple)"""
import requests, time

def get_with_retry(url, retries=3):
    for i in range(retries):
        try:
            r = requests.get(url, timeout=2)
            r.raise_for_status()
            return r.text
        except Exception as e:
            print('attempt', i+1, 'failed', e)
            time.sleep(0.5*(i+1))
    raise RuntimeError('failed')

if __name__ == '__main__':
    print('example: (will fail if offline)')
    # print(get_with_retry('https://httpbin.org/get'))
