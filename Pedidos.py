from abc import ABC, abstractmethod


# ==========================================
# 1. CLASE NODE (Node.py)
# ==========================================
class Node:

  def __init__(self, info: object, next_node=None):
    self.info = info
    self.next = next_node

  def get_info(self) -> object:
    return self.info

  def set_info(self, info: object):
    self.info = info

  def get_next(self):
    return self.next

  def set_next(self, next_node):
    self.next = next_node


# ==========================================
# 2. INTERFAZ QUEUEINTERFACE (Interfaz.py)
# ==========================================
class QueueInterface(ABC):

  @abstractmethod
  def size(self) -> int:
    """Returns the number of elements in Queue"""
    pass

  @abstractmethod
  def is_empty(self) -> bool:
    """Verifies if the Queue is empty.

    True if empty | False if not empty.
    """
    pass

  @abstractmethod
  def front(self) -> object:
    """Returns the first element in Queue.

    The element IS NOT REMOVED from Queue. Returns None if empty.
    """
    pass

  @abstractmethod
  def enqueue(self, info: object):
    """Adds a new element to the Queue."""
    pass

  @abstractmethod
  def dequeue(self) -> object:
    """Returns the first element in Queue.

    The element IS REMOVED from Queue. Returns None if empty.
    """
    pass


# ==========================================
# 3. CLASE ORDER (Orden.py)
# ==========================================
class Order:

  def __init__(self, qtty: int, customer: str):
    self.customer = customer
    self.qtty = qtty

  def print(self):
    print(f"     Cliente: {self.get_customer()}")
    print(f"     Cantidad: {self.get_qtty()}")
    print("     ------------")

  def get_qtty(self) -> int:
    return self.qtty

  def get_customer(self) -> str:
    return self.customer


# ==========================================
# 4. CLASE QUEUE / COLA (ColaOrden.py)
# ==========================================
class Queue(QueueInterface):

  def __init__(self):
    self.top = None
    self.tail = None
    self._count = 0

  def size(self) -> int:
    return self._count

  def is_empty(self) -> bool:
    return self.top is None

  def front(self) -> object:
    if self.is_empty():
      return None
    return self.top.get_info()

  def enqueue(self, info: object):
    new_node = Node(info)
    if self.is_empty():
      self.top = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node
    self._count += 1

  def dequeue(self) -> object:
    if self.is_empty():
      return None
    info = self.top.get_info()
    self.top = self.top.get_next()
    self._count -= 1
    if self.top is None:
      self.tail = None
    return info

  def print_info(self):
    print("********* Estado de la cola *********")
    print(f"    Tamaño: {self.size()}")

    node = self.top
    index = 1
    while node is not None:
      print(f"    ** Elemento {index}")
      node.get_info().print()
      node = node.get_next()
      index += 1

    print("******************************")

  def getNth(self, pos: int) -> object:
    if pos < 1 or pos > self.size():
      return None

    node = self.top
    current_pos = 1
    while node is not None:
      if current_pos == pos:
        return node.get_info()
      node = node.get_next()
      current_pos += 1

    return None


# ==========================================
# 5. CLASE TESTQUEUE Y MAIN (MainTest.py)
# ==========================================
class TestQueue:

  @staticmethod
  def main():
    print("=========================================")
    print("      GESTIÓN DE COLA DE PEDIDOS         ")
    print("=========================================")

    # 1. Crear la cola vacía
    queue = Queue()
    queue.print_info()

    # Bucle principal para que el programa no se cierre
    while True:
      print("\n--- MENÚ PRINCIPAL ---")
      print("1. Agregar pedidos")
      print("2. Ver estado de la cola")
      print("3. Buscar un elemento con getNth(pos)")
      print("4. Salir")

      opcion = input("Elige una opción (1-4): ")

      if opcion == "1":
        # Opción para agregar pedidos
        try:
          total_pedidos = int(
              input("¿Cuántos pedidos deseas agregar a la cola?: ")
          )
          for i in range(total_pedidos):
            print(f"\n--- Pedido {i + 1} de {total_pedidos} ---")
            cantidad = int(input("  Introduce la cantidad: "))
            cliente = input("  Introduce el nombre del cliente: ")

            nuevo_pedido = Order(cantidad, cliente)
            queue.enqueue(nuevo_pedido)
          print("\n¡Pedidos agregados con éxito!")
        except ValueError:
          print("❌ Error: Debes ingresar un número entero válido.")

      elif opcion == "2":
        # Opción para ver la cola
        print("\n")
        queue.print_info()

      elif opcion == "3":
        # Opción para buscar con getNth
        if queue.size() > 0:
          try:
            posicion = int(
                input(
                    f"¿Qué posición (elemento n de 1 a {queue.size()}) deseas"
                    " consultar?: "
                )
            )

            elemento_encontrado = queue.getNth(posicion)

            if elemento_encontrado is not None:
              print(f"\n✅ Elemento encontrado en la posición {posicion}:")
              elemento_encontrado.print()
            else:
              print(
                  f"\n⚠️ Posición {posicion} no válida. El método devolvió: null"
                  " (None)"
              )
          except ValueError:
            print("❌ Error: La posición debe ser un número entero.")
        else:
          print("\n⚠️ La cola está vacía, no hay elementos para consultar.")

      elif opcion == "4":
        print("\n¡Saliendo del programa. ¡Hasta luego!")
        break  # Rompe el bucle while y finaliza el programa

      else:
        print("\n❌ Opción no válida. Por favor, elige un número del 1 al 4.")


if __name__ == "__main__":
  TestQueue.main()