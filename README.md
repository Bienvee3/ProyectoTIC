# 📊 Proyecto de Evaluación Comparativa de Rendimiento: VM vs Docker

Este proyecto compara el uso de recursos y las métricas de rendimiento entre una máquina virtual completa (VirtualBox) y un contenedor Docker. El objetivo es identificar diferencias clave en eficiencia, rendimiento y adecuación según el contexto.

---

## 📚 Estructura Sugerida de Presentación del Proyecto

1. **Introducción**  
   ¿Qué son las máquinas virtuales y los contenedores? Explicación de conceptos clave.

2. **Configuración del Entorno de Prueba**  
   - Especificaciones del host (CPU, RAM, SO)  
   - Sistema operativo de la máquina virtual  
   - Imagen base de Docker utilizada

3. **Métricas y Herramientas Utilizadas**  
   - Qué se medirá y con qué herramientas

4. **Resultados**  
   - Tablas comparativas  
   - Gráficos de barras, líneas o gráficos de radar (araña)

5. **Análisis**  
   - Fortalezas y debilidades de cada enfoque

6. **Conclusión**  
   - Recomendaciones sobre cuándo usar VM o Docker

---

## ✅ Métricas de Comparación Sugeridas

### 🔧 1. Uso de Recursos
- **CPU**: Uso en reposo y bajo carga  
- **Memoria RAM**: Consumo al ejecutar la misma aplicación  
- **Espacio en disco**: Instalación base + aplicación + dependencias  
**Herramientas:** `htop`, `top`, `docker stats`, `VBoxManage metrics`, `vmstat`

---

### ⚡ 2. Tiempo de Arranque / Inicio
- Tiempo requerido para iniciar una VM vs iniciar un contenedor Docker  
**Herramientas:** `systemd-analyze`, scripts `time`, diferencias de `date`

---

### 🚀 3. Pruebas de Rendimiento
- **CPU**: `sysbench`, `stress-ng`, `Geekbench`  
- **Disco (E/S)**: `fio`, `dd if=/dev/zero of=testfile bs=1G count=1 oflag=dsync`  
- **Red**: `iperf3` (dentro y desde el host)

---

### 📦 4. Caso de Prueba de Aplicación
Ejemplo: un servidor MySQL o una app Node.js  
- Tiempo de implementación  
- Rendimiento (solicitudes por segundo)  
- Latencia  
- Consumo de recursos bajo carga

---

### 🔒 5. Aislamiento y Seguridad
Evaluación cualitativa:  
- Las VM ofrecen mejor aislamiento (núcleo separado)  
- Docker es más eficiente pero menos aislado (comparte el kernel)  
- Mencionar medidas de seguridad como `AppArmor`, `SELinux`

---

### ♻️ 6. Portabilidad y Flexibilidad
Evaluación cualitativa:  
- Facilidad para exportar/importar imágenes  
- Soporte multiplataforma (Windows/macOS/Linux)  
- Integración con flujos DevOps (CI/CD)

---

## 🧪 Contribuciones
¡Se aceptan ideas, mejoras o pruebas adicionales! Puedes abrir un issue o hacer un pull request.

---

## 📄 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
