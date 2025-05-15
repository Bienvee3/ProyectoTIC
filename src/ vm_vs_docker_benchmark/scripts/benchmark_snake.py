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
        print(f"Error: {e}")
    time.sleep(0.2)

# Detectar entorno
is_vm = input("¿Estás ejecutando esto en una VM? (s/n): ").strip().lower() == 's'
env_label = 'vm' if is_vm else 'docker'
filename = f"benchmark_snake_{env_label}.csv"
filepath_csv = f"../results/{filename}"

# Guardar CSV
with open(filepath_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["latency", "cpu_percent", "memory_percent"])
    writer.writerows(results)

# Calcular métricas
latencias = [r[0] for r in results]
cpus = [r[1] for r in results]
mems = [r[2] for r in results]

avg_latency = sum(latencias) / len(latencias)
max_latency = max(latencias)
min_latency = min(latencias)

avg_cpu = sum(cpus) / len(cpus)
max_cpu = max(cpus)
min_cpu = min(cpus)

avg_mem = sum(mems) / len(mems)
max_mem = max(mems)
min_mem = min(mems)

# Tamaño en disco del entorno
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
total_size = 0
for dirpath, dirnames, filenames in os.walk(base_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if os.path.exists(fp):
            total_size += os.path.getsize(fp)
disk_mb = total_size / (1024 * 1024)

# Contar peticiones
total_requests = len(results)
errores = 0  # ya que no los contamos realmente
network_mb = total_requests * len("dummy-response") * 0.001 / 1024  # estimación ficticia

# Mostrar resumen en consola
print(f"\n📊 RESUMEN DEL BENCHMARK")
print(f"📁 Entorno: {'VM' if is_vm else 'Docker'} — {base_path}")
print(f"🧠 RAM promedio: {avg_mem:.2f}%")
print(f"⚙️  CPU promedio: {avg_cpu:.2f}%")
print(f"⏱️  Latencia promedio: {avg_latency*1000:.2f} ms")
print(f"🔺 Latencia máx: {max_latency*1000:.2f} ms")
print(f"🔻 Latencia mín: {min_latency*1000:.2f} ms")
print(f"🔥 CPU máx: {max_cpu:.2f}%")
print(f"🧊 CPU mín: {min_cpu:.2f}%")
print(f"📈 RAM máx: {max_mem:.2f}%")
print(f"📉 RAM mín: {min_mem:.2f}%")
print(f"💾 Tamaño del entorno en disco: {disk_mb:.2f} MB")
print(f"📨 Total de peticiones: {total_requests}")
print(f"❌ Errores: {errores} ({(errores/total_requests)*100 if total_requests else 0:.2f}%)")
print(f"🌐 Tráfico de red: {network_mb:.2f} MB")
print(f"⏱️  Tiempo total medido: {duration - (end_time - time.time()):.2f} segundos")
print(f"✅ CSV guardado en: {filepath_csv}")

# Guardar resumen en TXT
filepath_txt = f"../results/benchmark_snake_{env_label}.txt"
with open(filepath_txt, "w", encoding="utf-8") as f:
    f.write("📊 RESUMEN DEL BENCHMARK\n")
    f.write(f"📁 Entorno: {'VM' if is_vm else 'Docker'} — {base_path}\n")
    f.write(f"🧠 RAM promedio: {avg_mem:.2f}%\n")
    f.write(f"⚙️  CPU promedio: {avg_cpu:.2f}%\n")
    f.write(f"⏱️  Latencia promedio: {avg_latency*1000:.2f} ms\n")
    f.write(f"🔺 Latencia máx: {max_latency*1000:.2f} ms\n")
    f.write(f"🔻 Latencia mín: {min_latency*1000:.2f} ms\n")
    f.write(f"🔥 CPU máx: {max_cpu:.2f}%\n")
    f.write(f"🧊 CPU mín: {min_cpu:.2f}%\n")
    f.write(f"📈 RAM máx: {max_mem:.2f}%\n")
    f.write(f"📉 RAM mín: {min_mem:.2f}%\n")
    f.write(f"💾 Tamaño del entorno en disco: {disk_mb:.2f} MB\n")
    f.write(f"📨 Total de peticiones: {total_requests}\n")
    f.write(f"❌ Errores: {errores} ({(errores/total_requests)*100 if total_requests else 0:.2f}%)\n")
    f.write(f"🌐 Tráfico de red: {network_mb:.2f} MB\n")
    f.write(f"⏱️  Tiempo total medido: {duration - (end_time - time.time()):.2f} segundos\n")
    f.write(f"✅ CSV guardado en: {filepath_csv}\n")
