keywords = ['25%', 'RS', '마진', '공급가', '손님 카톡 주문링크', '가이드 B2B', '가이드 수수료', '비밀']

def scan(path):
    print(f"=== {path} ===")
    with open(path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            for k in keywords:
                if k in line:
                    print(f"L{i+1}: [{k}] {line.strip()[:120].encode('ascii', errors='replace').decode('ascii')}")

scan('templates/base.html')
scan('templates/index.html')
scan('templates/order_tracking.html')
