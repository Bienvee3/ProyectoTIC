# 🐍 Proyecto de Benchmark: VM vs Docker con un servidor Snake

Este proyecto evalúa y compara el rendimiento entre una máquina virtual (VirtualBox) y un contenedor Docker ejecutando un servidor Snake desarrollado en Flask y con una interfaz web interactiva.

## 📁 Estructura actual del proyecto

``` cpp
vm_vs_docker_benchmark/
├── README.md
├── requirements.txt
├── .gitignore
├── explicacionProyecto.md
├── install.ipynb
├── results/
│   ├── benchmark_snake_vm.csv
│   └── benchmark_snake_docker.csv
├── notebooks/
│   └── vm_vs_docker_comparison.ipynb
├── scripts/
│   ├── benchmark_snake.py
│   ├── docker_setup.sh
│   ├── vm_setup.sh
│   ├── Dockerfile
│   └── web_snake_game/
│       ├── run_snake_server.py
│       ├── templates/
│       │   └── snake.html
│       └── static/
│           └── snake.js
```

## ✅ Librerías necesarias

El proyecto utiliza las siguientes librerías de Python:

``` bash
flask
requests
psutil
pandas
matplotlib
jupyter
```

## ⚙️ Requisitos

```
Python 3.8+

Docker

VirtualBox (con Linux guest si aplica)

pip
```

## 📦 Instalación de dependencias

Desde la raíz del proyecto:

``` bash
pip install -r requirements.txt
```

## 🚀 Ejecutar el servidor Snake

Para iniciar el servidor Snake con interfaz web:

```bash
cd vm_vs_docker_benchmark/scripts/web_snake_game
python run_snake_server.py
```

Esto abrirá un servidor Flask en http://localhost:5000/. Podrás acceder a la interfaz del juego desde un navegador en esa dirección.


## 🎮 Jugar Snake

Visita:

``` arduino
http://localhost:5000/play
```
Ahí podrás jugar una versión básica del juego Snake directamente desde el navegador.

## 📊 Benchmark y Análisis de Resultados

- Ejecutar Benchmarks

Asegúrate de que el servidor Snake esté corriendo. Luego, desde una nueva terminal:

```bash
cd vm_vs_docker_benchmark/scripts
python benchmark_snake.py
```
Este script realiza:

- 📈 Medición del uso de CPU y RAM

- ⏱ Tiempo de respuesta de la aplicación

Los resultados se guardan en:

`results/benchmark_snake_vm.csv` (si se corre en una VM)

`results/benchmark_snake_docker.csv` (si se corre en Docker)

- Visualizar resultados
  
Abre el notebook:

```bash
cd vm_vs_docker_benchmark/notebooks
jupyter notebook vm_vs_docker_comparison.ipynb
```

El notebook permite analizar los resultados con gráficos y estadísticas.

## 🧪 Automatización del entorno

Puedes usar los siguientes scripts para automatizar la instalación del entorno:

```bash
cd vm_vs_docker_benchmark/scripts
bash vm_setup.sh         # Configuración para VM
bash docker_setup.sh     # Configuración para Docker o WSL2
```

## 🗃️ Carpeta results/

Contiene los archivos CSV generados por los benchmarks. Cada archivo incluye:

- Latencia

- Porcentaje de uso de CPU

- Porcentaje de uso de memoria RAM