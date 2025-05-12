# 🐍 Proyecto de Benchmark: VM vs Docker con un servidor Snake

Este proyecto evalúa y compara el rendimiento entre una máquina virtual (VirtualBox) y un contenedor Docker ejecutando un servidor simple de juego Snake desarrollado en Flask.

---

## 📁 Estructura actual del proyecto
```
vm_vs_docker_benchmark/
├── README.md
├── requirements.txt
├── .gitignore
├── results/
│   ├── benchmark_snake_vm.csv
│   └── benchmark_snake_docker.csv
├── notebooks/
│   └── vm_vs_docker_comparison.ipynb
├── scripts/
│   ├── vm_setup.sh
│   ├── docker_setup.sh
│   └── Dockerfile
└── snake_server/
    └── snake_server.py
```
---

## ✅ Librerías necesarias

El proyecto utiliza las siguientes librerías:
```
flask
request
psutil
pandas
matplotlib
jupyter
```

---

## ⚙️ Requisitos

- Python 3.8+
- Docker
- VirtualBox (con Linux guest si aplica)
- pip

---

## 📦 Instalación de dependencias

Para comenzar, es necesario instalar todas las dependencias requeridas para el proyecto. Para hacerlo, sigue los siguientes pasos:

1. Abre una terminal.
2. Navega a la carpeta raíz del proyecto.
3. Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

    ```
    pip install -r requirements.txt
    ```

Esto instalará todas las dependencias necesarias para que el servidor y las herramientas de benchmark funcionen correctamente.

## Ejecución del Servidor Snake

El servidor Snake está ubicado en el archivo `snake_server.py`, dentro de la carpeta `vm_vs_docker_benchmark/snake_server/`. Sigue los siguientes pasos para ejecutar el servidor:

1. Navega a la carpeta donde se encuentra el archivo del servidor:

    ```
    cd vm_vs_docker_benchmark/snake_server
    ```

2. Ejecuta el servidor con el siguiente comando:

    ```
    python snake_server.py
    ```

Esto iniciará un servidor Flask en el puerto `5000`. El servidor estará en ejecución y podrás interactuar con él según sea necesario.

## Benchmark y Análisis de Resultados

Los resultados del benchmark, como el uso de CPU, RAM, y otros parámetros de rendimiento, se guardan en archivos CSV. Estos resultados se encuentran en la carpeta:

`vm_vs_docker_benchmark/results/`


Para visualizar y analizar estos resultados, se incluye un notebook de Jupyter en el proyecto. Sigue estos pasos para acceder al notebook y ver los análisis:

1. Navega a la carpeta donde se encuentra el notebook:

    ```
    cd vm_vs_docker_benchmark/notebooks/
    ```

2. Abre el notebook de Jupyter con el siguiente comando:

    ```
    jupyter notebook vm_vs_docker_comparison.ipynb
    ```

Este notebook contiene el código necesario para cargar y visualizar los resultados generados por el benchmark.

## Scripts de Configuración Automática

Para facilitar la instalación de las dependencias y la configuración del entorno, se incluyen scripts de configuración automática. Estos scripts permiten instalar las dependencias necesarias en una máquina virtual (VM) o un contenedor Docker.

Para utilizar el script de configuración, sigue estos pasos:

1. Navega a la carpeta `scripts`:

    ```
    cd scripts
    ```

2. Ejecuta el script de configuración con el siguiente comando:

    ```
    bash vm_setup.sh
    ```

Este script automatiza la instalación de todas las dependencias necesarias en tu entorno de trabajo (ya sea en una máquina virtual o Docker).

---

Con estos pasos, tendrás todo lo necesario para ejecutar el servidor Snake, realizar pruebas de benchmark y analiza