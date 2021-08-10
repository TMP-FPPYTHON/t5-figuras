## **Calculadora con Funciones !!**

- Elabora un programa Python que ofrezca un menú repetitivo de opciones -en una función ``` main()```-, mediante el cual el usuario  pueda escoger calcular el área de las siguientes figuras geométricas: *triángulo*, *cuadrado*, *rectángulo* y *círculo*. 

- Una vez seleccionada la opción, el programa deberá  llamar a la función correspondiente (una por figura geométrica) la cual solicitará los datos necesarios y calculará e imprimirá el área correspondiente.

- Prueba con las siguientes figuras: :+1:

```python
Triángulo (b=10, h=15), Cuadrado(l=4), Rectángulo (l=20, h=3), Círculo(r=4.5)
```
## **Pruebas locales de la Calculadora !!**

## Configuración de pruebas con **pytest**

`nota:` para todo las pruebas puedes usar esta configuración:
### Setup command (optional)
```
pip3 install pytest
```

- ## Área del Círculo:
    ### Run command
    ```
    pytest testAreaCirculo.py
    ```

- ## Área del Cuadrado:
    ### Run command
    ```
    pytest testAreaCuadrado.py
    ```

- ## Área del Rectángulo:
    ### Run command
    ```
    pytest testAreaRectangulo.py
    ```
- ## Área del Triángulo:
    ### Run command
    ```
    pytest testAreaTriangulo.py
    ```