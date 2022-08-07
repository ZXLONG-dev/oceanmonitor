from template.messagelistener import *
from template.ominous863023145463578644 import *
from template.prism863023145463578644 import *


def init_app():
  messagelistener_instance.add_observer("Ominous863023145463578644", Ominous863023145463578644())
  messagelistener_instance.add_observer("Prism863023145463578644", Prism863023145463578644())
