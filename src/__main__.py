import os
import sys
from contextlib import suppress

import core
from gui import Gui
from model import Model
from generators import Generators


def main(path: str, model: Model) -> None:
    gui = Gui(os.path.join(path, '../assets'))

    while True:
        rotation = gui.get_rotation()

        if rotation != [0, 0, 0]:
            old_vertices = model.get_vertices()
            rotation_matrix = core.create_matrix(rotation)
            
            new_vertices = core.rotate_vertices(old_vertices, rotation_matrix)
            model.set_vertices(new_vertices)
        
        gui.render_model(model)
        gui.render_info()
        
        gui.update_display()


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))

    while True:
        with suppress(IndexError, ValueError):
            if sys.platform == 'win32':
                os.system('cls')
            else:
                os.system('clear')

            print('Available Models:')

            for index, model_name in enumerate(Generators.__all__):
                print(f'{index+1:<{2}} : {model_name}')

            choice = int(input('\n> '))
            model = Model(*getattr(Generators, Generators.__all__[choice-1])())
            
            break
    
    main(path, model)