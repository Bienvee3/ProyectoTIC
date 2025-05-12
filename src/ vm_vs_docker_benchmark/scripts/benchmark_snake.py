import requests
import time
import csv
import psutil

url = "http://localhost:5000/snake"
duration = 60  # segundos
end_time = time.time() + duration

results = []

print("⏳ Running benchmark for 60 seconds...")
while time.time() < end_time:
    start = time.time()
    try:
        r = requests.get(url)
        latency = time.time() - start
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
        results.append([latency, cpu, mem])
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(0.2)

# Detect environment
is_vm = input("Is this running in a VM? (y/n): ").strip().lower() == 'y'
filename = f"benchmark_snake_{'vm' if is_vm else 'docker'}.csv"

with open(f"../results/{filename}", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["latency", "cpu_percent", "memory_percent"])
    writer.writerows(results)

print(f"✅ Benchmark complete! Results saved to results/{filename}")
