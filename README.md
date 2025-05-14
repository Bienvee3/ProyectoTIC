# 🐍 Proyecto de Benchmark: VM vs Docker con un servidor Snake

Este proyecto evalúa y compara el rendimiento entre una máquina virtual (VirtualBox) y un contenedor Docker ejecutando un servidor Snake desarrollado en Flask y con una interfaz web interactiva.

## 📁 Estructura actual del proyecto

``` cpp
.
├── README.md
├── enunciadoProyecto.md
└── src/
    ├── install.ipynb
    └── vm_vs_docker_benchmark/
        ├── requirements.txt
        ├── .gitignore
        ├── results/
        │   ├── benchmark_snake_vm.csv
        │   ├── benchmark_snake_docker.csv
        │   ├── benchmark_vm.png
        │   └── benchmark_docker.png
        ├── notebooks/
        │   ├── vm_vs_docker_comparison.ipynb
        │   └── vm_vs_docker_comparison.png
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
Ahí podrás jugar una versión del juego Snake directamente desde el navegador despues de ejecutarlo en la terminal.

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

---

## 📁 Estructura de los Resultados / Análisis

Este proyecto compara el rendimiento de una misma carga de trabajo (`benchmark_snake`) ejecutada tanto en una máquina virtual (VM) como en un contenedor Docker.

```cpp
├── results/
│ ├── benchmark_snake_vm.csv
│ └── benchmark_snake_docker.csv
│ └── benchmark_docker.png
│ └── benchmark_vm.png
├── notebooks/
│ └── vm_vs_docker_comparison.ipynb
│ └── vm_vs_docker_comparison.png
```


- `results/`: contiene los archivos CSV con los resultados de los benchmarks.
- `notebooks/`: incluye notebooks de análisis y gráficos comparativos.

---

## 📊 Comparativa de Rendimiento: VM vs Docker

Se ejecutó un benchmark de 60 segundos sobre un juego Snake en Flask, midiendo el rendimiento del entorno bajo carga desde dos contextos distintos:

<table>
  <tr>
    <td align="center"><strong>🖥️ Virtual Machine</strong></td>
    <td align="center"><strong>🐳 Docker</strong></td>
  </tr>
  <tr>
    <td><img src="src/ vm_vs_docker_benchmark/results/benchmark_vm.png" width="400"/></td>
    <td><img src="src/ vm_vs_docker_benchmark/results/benchmark_docker.png" width="400"/></td>
  </tr>
</table>

🔬 Los resultados muestran que ambos entornos tienen un comportamiento muy similar, aunque la VM tuvo una leve mayor carga de CPU.


## 📓 Análisis en notebooks

En el notebook `notebooks/vm_vs_docker_comparison.ipynb` se realiza una comparación del uso de CPU entre la ejecución en VM y en Docker.

A partir de los datos de `results/`, se genera la siguiente gráfica:

<p align="center">
  <img src="src/ vm_vs_docker_benchmark/notebooks/vm_vs_docker_comparison.png" alt="Comparación de CPU: VM vs Docker" width="600"/>
</p>

---

### 🔍 Interpretación

- **VM CPU** (línea azul): presenta una mayor variabilidad y consumo promedio más alto de CPU.
- **Docker CPU** (línea naranja): es más eficiente, con menor uso de CPU bajo la misma carga.

Esto indica que **Docker es más liviano** para esta tarea, reduciendo el uso de recursos del sistema en comparación con una VM tradicional. Sin embargo, los resultados pueden variar según el contexto y carga específica.

---

### ✅ Logros del proyecto

- [x] Juego Snake funcional con Flask
- [x] Automatización en VM y Docker
- [x] Benchmark comparativo con gráficos
- [x] Análisis visual en notebooks