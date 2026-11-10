# Trabajo Integrador – Arquitectura y Sistemas Operativos
## Virtualización con VMware Workstation

**Estudiante:** Oscar Hernán Leon Oyarzo
**Comisión:** 13 – Tecnicatura Universitaria en Programación a Distancia (UTN)
**Profesor:** Mauricio Gabriel Pasti · **Tutor:** Octavio Rolón Hernández

Configuración de una máquina virtual con **Ubuntu 24.04 LTS** en **VMware Workstation** (hipervisor de tipo 2) sobre Windows 10, actualización y personalización del sistema invitado y ejecución de un programa propio en **Python 3.12**.

## Video explicativo
https://youtu.be/nw5btoET2eU


## Documentación
Informe técnico en PDF (raíz del repositorio): [Leon_Oscar_AySO_TI_Virtualizacion.pdf](Leon_Oscar_AySO_TI_Virtualizacion.pdf)

## Contenido del repositorio
```
TPI_AySO_Virtualizacion/
├── Leon_Oscar_AySO_TI_Virtualizacion.pdf   → informe técnico
├── README.md
├── capturas/                               → evidencias de cada etapa (01 a 17)
└── codigo/                                 → programa en Python ejecutado en la VM
    ├── main.py
    └── paquete_funciones/
```

## Configuración de la máquina virtual
| Recurso | Valor |
|---|---|
| Hipervisor | VMware Workstation (tipo 2) sobre Windows 10 |
| Sistema invitado | Ubuntu 24.04 LTS |
| RAM | 2 GB |
| CPU | 2 núcleos |
| Disco | 30 GB (SCSI) |
| Red | NAT |

## Comandos utilizados en la VM
```bash
sudo apt update
sudo apt upgrade -y
python3 --version
sudo apt install git -y
git clone https://github.com/leonoscar991/Leon_Oscar_p1
cd Leon_Oscar_p1
ls
python3 main.py
```

## Cómo ejecutar el programa
Requiere Python 3 (sin librerías externas). Desde la carpeta `codigo`:
```bash
python3 main.py
```
El programa es un sistema de control de inventario de una ferretería (menú con 7 opciones). Repositorio original: https://github.com/leonoscar991/Leon_Oscar_p1
