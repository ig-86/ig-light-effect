"""Constants for İsmet Light Effect Card."""

DOMAIN = "ismet_light_effects"
VERSION = "1.0.0"
STORAGE_KEY = DOMAIN
STORAGE_VERSION = 1
SIGNAL_UPDATE = f"{DOMAIN}_update"
URL_BASE = "/ismet_light_effects"
URL_ICONS = "/ismet_light_effects_icons"
CARD_FILE = "ismet-light-effect-card.js"
ICON_DIR = "ismet_light_effects_icons"
MAX_ICON_BYTES = 512 * 1024
PANEL_URL = "ismet-light"
PANEL_ELEMENT = "ismet-light-effects-panel"
MAX_SETTINGS_BYTES = 256 * 1024
MAX_TABS_BYTES = 1024 * 1024

# the earlier "Ultimate Light Effect Card"; its data is taken over once on first start
OLD_STORAGE_KEY = "ultimate_light_effects"
OLD_ICON_DIR = "ultimate_light_effects_icons"
OLD_URL_ICONS = "/ultimate_light_effects_icons"
