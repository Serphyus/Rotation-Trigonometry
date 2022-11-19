import os
import sys
from pathlib import Path
from contextlib import suppress

import core
from gui import Gui
from model import Model
from generators import Generators


def main(path: str, model: Model) -> None:
    gui = Gui(Path(path, '../assets'))

    while not gui.terminated:
        rotation = gui.get_rotation()

        if rotation is None:
            continue

        if rotation != [0, 0, 0]:
            rotation_matrix = core.create_matrix(rotation)
            model.rotate(rotation_matrix)
        
        gui.render_model(model)
        gui.render_info()
        
        gui.update_display()


if __name__ == '__main__':
    abs_path = Path(__file__).resolve().parent

    model = None
    while model is None:
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
    
    main(abs_path, model)