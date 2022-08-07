from message.message_factory import *
from message.template.ominous863023145463578644 import *
from message.template.prism863023145463578644 import *


def init_app():
  messagefactory_instance.add_observer("Ominous863023145463578644", Ominous863023145463578644())
  messagefactory_instance.add_observer("Prism863023145463578644", Prism863023145463578644())
