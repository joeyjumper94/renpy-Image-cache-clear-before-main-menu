from modloader import modinfo, modast
from modloader.modclass import Mod, loadable_mod

import renpy.display.im as im

#hook opcode gives an arguement to the function that we need to discard
def renpy_display_im_cache_clear(arg):
    im.cache.clear()

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("cache clear", "v1.0", "joeyjumper94")

    def mod_load(self):
        modast.hook_opcode(modast.find_label("mainmenu"),renpy_display_im_cache_clear)

    def mod_complete(self):
        pass
