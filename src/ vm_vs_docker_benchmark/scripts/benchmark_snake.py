import requests
import time
import csv
import psutil
import os
import shutil

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
filepath = f"../results/{filename}"

# Guardar CSV
with open(filepath, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["latency", "cpu_percent", "memory_percent"])
    writer.writerows(results)

# 🔍 Calcular promedios
latencias = [r[0] for r in results]
cpus = [r[1] for r in results]
mems = [r[2] for r in results]

avg_latency = sum(latencias) / len(latencias)
avg_cpu = sum(cpus) / len(cpus)
avg_mem = sum(mems) / len(mems)

# 📦 Calcular tamaño en disco del entorno (donde está el proyecto)
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
total_size = 0
for dirpath, dirnames, filenames in os.walk(base_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if os.path.exists(fp):
            total_size += os.path.getsize(fp)
disk_mb = total_size / (1024 * 1024)

# 📋 Mostrar resumen
print("\n📊 RESUMEN DEL BENCHMARK")
print(f"📁 Entorno analizado: {base_path}")
print(f"🧠 RAM promedio durante ejecución: {avg_mem:.2f}%")
print(f"⚙️  CPU promedio bajo carga: {avg_cpu:.2f}%")
print(f"⏱️  Latencia promedio: {avg_latency*1000:.2f} ms")
print(f"💾 Espacio en disco usado por entorno: {disk_mb:.2f} MB")
print(f"✅ Resultados guardados en: {filepath}")
