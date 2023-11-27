### Script utilizado para separar audios en intervalo de 1 min

1. Creamos un entorno virtual de python
python3 -m venv venv

2. Activamos el entorno virtual que acabamos de crear
source venv/bin/activate

3. Instalamos la biblioteca que necesitamos:
pip install pydub

### Forma de uso:
Creamos una carpeta por cada Audio
En la sub-carpeta "original" depositamos el audio en mp3
Reemplazamos la ruta donde se encuentra el audio en mp3
Reemplazamos la ruta en la que se van a exportar los cortes de los audios.