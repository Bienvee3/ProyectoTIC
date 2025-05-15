import requests
import time
import csv
import psutil
import os

url = "http://localhost:5000/snake"
duration = 60  # segundos
end_time = time.time() + duration

results = []
errors = 0

# 🔄 Medir red antes
net_start = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

print("⏳ Ejecutando benchmark por 60 segundos...")

while time.time() < end_time:
    start = time.time()
    try:
        r = requests.get(url)
        latency = time.time() - start
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
        results.append([latency, cpu, mem])
    except Exception as e:
        print(f"❌ Error: {e}")
        errors += 1
    time.sleep(0.2)

# 🔄 Medir red después
net_end = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
network_usage = (net_end - net_start) / (1024 * 1024)  # MB

# Detectar entorno
is_vm = input("¿Estás ejecutando esto en una VM? (s/n): ").strip().lower() == 's'
context = "vm" if is_vm else "docker"
filename_csv = f"benchmark_snake_{context}.csv"
filename_txt = f"benchmark_snake_{context}_resumen.txt"
results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results"))
os.makedirs(results_dir, exist_ok=True)

# Guardar CSV
filepath_csv = os.path.join(results_dir, filename_csv)
with open(filepath_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["latency", "cpu_percent", "memory_percent"])
    writer.writerows(results)

# 🔍 Calcular estadísticas
latencias = [r[0] for r in results]
cpus = [r[1] for r in results]
mems = [r[2] for r in results]

avg_latency = sum(latencias) / len(latencias) if latencias else 0
avg_cpu = sum(cpus) / len(cpus) if cpus else 0
avg_mem = sum(mems) / len(mems) if mems else 0

# 📦 Tamaño en disco del entorno del proyecto
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
total_size = 0
for dirpath, dirnames, filenames in os.walk(base_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if os.path.exists(fp):
            total_size += os.path.getsize(fp)
disk_mb = total_size / (1024 * 1024)

# 📋 Métricas adicionales
total_requests = len(results)
total_duration = sum(latencias) + total_requests * 0.2  # incluye sleeps
failures = errors
error_rate = (failures / (total_requests + failures)) * 100 if (total_requests + failures) > 0 else 0

# Mostrar en consola
print("\n📊 RESUMEN DEL BENCHMARK")
print(f"📁 Entorno: {context.upper()} — {base_path}")
print(f"🧠 RAM promedio: {avg_mem:.2f}%")
print(f"⚙️  CPU promedio: {avg_cpu:.2f}%")
print(f"⏱️  Latencia promedio: {avg_latency*1000:.2f} ms")
print(f"🔺 Latencia máx: {max(latencias)*1000:.2f} ms")
print(f"🔻 Latencia mín: {min(latencias)*1000:.2f} ms")
print(f"🔥 CPU máx: {max(cpus):.2f}%")
print(f"🧊 CPU mín: {min(cpus):.2f}%")
print(f"📈 RAM máx: {max(mems):.2f}%")
print(f"📉 RAM mín: {min(mems):.2f}%")
print(f"💾 Tamaño del entorno en disco: {disk_mb:.2f} MB")
print(f"📨 Total de peticiones: {total_requests}")
print(f"❌ Errores: {failures} ({error_rate:.2f}%)")
print(f"🌐 Tráfico de red: {network_usage:.2f} MB")
print(f"⏱️  Tiempo total medido: {total_duration:.2f} segundos")
print(f"✅ CSV guardado en: {filepath_csv}")

# Guardar resumen en TXT
filepath_txt = os.path.join(results_dir, filename_txt)
with open(filepath_txt, "w") as f:
    f.write("📊 RESUMEN DEL BENCHMARK\n")
    f.write(f"📁 Entorno: {context.upper()} — {base_path}\n")
    f.write(f"🧠 RAM promedio: {avg_mem:.2f}%\n")
    f.write(f"⚙️  CPU promedio: {avg_cpu:.2f}%\n")
    f.write(f"⏱️  Latencia promedio: {avg_latency*1000:.2f} ms\n")
    f.write(f"🔺 Latencia máx: {max(latencias)*1000:.2f} ms\n")
    f.write(f"🔻 Latencia mín: {min(latencias)*1000:.2f} ms\n")
    f.write(f"🔥 CPU máx: {max(cpus):.2f}%\n")
    f.write(f"🧊 CPU mín: {min(cpus):.2f}%\n")
    f.write(f"📈 RAM máx: {max(mems):.2f}%\n")
    f.write(f"📉 RAM mín: {min(mems):.2f}%\n")
    f.write(f"💾 Tamaño del entorno en disco: {disk_mb:.2f} MB\n")
    f.write(f"📨 Total de peticiones: {total_requests}\n")
    f.write(f"❌ Errores: {failures} ({error_rate:.2f}%)\n")
    f.write(f"🌐 Tráfico de red: {network_usage:.2f} MB\n")
    f.write(f"⏱️  Tiempo total medido: {total_duration:.2f} segundos\n")
    f.write(f"✅ CSV guardado en: {filepath_csv}\n")

print(f"📝 Resumen guardado en: {filepath_txt}")
