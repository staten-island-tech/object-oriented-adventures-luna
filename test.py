
#import battle.py from game_files and test it - TESTED   importing works :D
import sys
sys.path.append('/game_files')
from game_files import star_system
star_system.star.pull_one("exa")
