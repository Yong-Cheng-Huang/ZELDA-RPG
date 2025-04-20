# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0}

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'  # Light blue for water
UI_BG_COLOR = '#5c7447'   # Olive green for UI background
UI_BORDER_COLOR = '#3b4a2e'  # Dark green for UI borders
TEXT_COLOR = '#FFFFFF'    # White for text

# ui colors
HEALTH_COLOR = '#E63946'  # Red for health bar
ENERGY_COLOR = '#457b9d'  # Blue for energy bar
UI_BORDER_COLOR_ACTIVE = '#F4A261'  # Light orange for active UI borders

# upgrade menu
TEXT_COLOR_SELECTED = '#FFFFFF'  # Dark green for selected text
BAR_COLOR = '#FFFFFF'  # White for upgrade bar
BAR_COLOR_SELECTED = '#FFFFFF'  # Olive green for selected upgrade bar
# Light orange for selected upgrade background
UPGRADE_BG_COLOR_SELECTED = '#F4A261'


# weapons
weapon_data = {
    'sword': {'cooldown': 10, 'damage': 15, 'graphic': 'graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 100, 'damage': 30, 'graphic': 'graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 10, 'damage': 20, 'graphic': 'graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 5, 'damage': 8, 'graphic': 'graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 10, 'damage': 10, 'graphic': 'graphics/weapons/sai/full.png'}}

# magic
magic_data = {
    'flame': {'strength': 20, 'cost': 30, 'graphic': 'graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 30, 'graphic': 'graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'score': 5, 'attack_type': 'slash', 'attack_sound': 'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'score': 20,  'attack_type': 'claw',  'attack_sound': 'audio/attack/claw.wav', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'score': 15,  'attack_type': 'thunder', 'attack_sound': 'audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'score': 5, 'attack_type': 'leaf_attack', 'attack_sound': 'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
