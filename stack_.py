from typing import Any, Optional


class Stack:

    def __init__(self):
        self.__elements = []

    #agrega un elemento a la cima de la pila como .append
    def push(self, value: Any) -> None:
        self.__elements.append(value)

    #elimina el elemento de la cima de la pila como .pop
    def pop(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )
    
    #muestra el tamaño de la pila como len
    def size(self) -> int:
        return len(self.__elements)
    
    #permite ver el elemento de la cima de la pila sin eliminarlo
    def on_top(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )
    #muestra la pila completa
    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())

    #hace una copia de la pila
    def copy(self) -> 'Stack':
        new_stack = Stack()
        for element in self.__elements:
            new_stack.push(element)
        return new_stack
    
    def sEmpty(self):
        return self.on_top() is None