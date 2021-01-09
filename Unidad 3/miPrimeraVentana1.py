# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import glfw

def main():
    #Inicializacion de la libreria
    if not glfw.init():
        return
    #Crecion de ventaana
    window = glfw.create_window(640,480,"Mi Primera Ventana",None,None)
    
    if not window:
        glfw.terminate()
        return
    #Configuracion como ventana principal
    glfw.make_context_current(window)
    
    #entra al bucle principal
    while not glfw.window_should_close(window):
        #dibujamos cualquier cosa
        
        #Esta funcion traera adelante la pantalla auxiliar
        glfw.swap_buffers(window)
        
        #Verifica que los eventos se ejecuten correctamente
        glfw.poll_events()
        
    glfw.terminate()
main()            
        
    