from .enemy import EnemiesManager
from .turret import TurretsManager
from .map import MapManager
from .game import GameManager


managers = {
    'enemy': EnemiesManager(),
    'turret': TurretsManager(),
    'map': MapManager(),
    'game': GameManager(),
}
