from utils.types.t_colors import RGB
from utils.types.t_utils import ICON
from utils.types.t_vectors import SVEC2

from enum import Enum


class _ICONS(Enum):

    NOICON = ICON('static/icons/Noicon.png')
    CONSOLE = ICON('static/icons/Console.png')
    FILEMANAGER = ICON('static/icons/Floder.png')
    OBSERVER = ICON('static/icons/Observer.png')

class _COLOR_BALANCE(Enum):
    BACKGROUND = RGB(30, 29, 29)
    ON_BACKGROUND = RGB(234, 234, 234)
    SURFACE = RGB(52, 49, 42)
    PRIMARY = RGB(127, 105, 85)
    SECONDARY = RGB(218, 192, 156)

class STYLES(Enum):
    
    FONT_SIZE = 12
    FONT = 'Arial'
    ICONS = _ICONS
    COLOR_BALANCE = _COLOR_BALANCE