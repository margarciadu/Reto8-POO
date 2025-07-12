#Reto 8 POO 

Este es un sistema básico de pedidos para un restaurante del reto 3. El menú está organizado por categorías (Bebidas, Aperitivos, Platos Fuertes) y permite al usuario hacer un pedido desde la consola.

## Características

- Los ítems del menú están representados con clases e herencia.
- El usuario puede seleccionar productos por número, ingresar cantidades y ver un resumen.
- Se aplican descuentos automáticos según el valor total del pedido.
- La clase `Order` es iterable gracias a una clase externa `OrderIterator`, lo que permite recorrer directamente los ítems del pedido.


## Estructura

Las clases principales son:

- `MenuItem`: clase base para todos los productos del menú.
- `Beverage`, `Appetizer`, `MainCourse`: subclases que heredan de `MenuItem`.
- `Order`: representa un pedido con varios ítems y cantidades.
- `OrderIterator`: permite iterar sobre los ítems del pedido.
