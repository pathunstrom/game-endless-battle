"""
A tiny rogue-like shooter based on Destiny's Deep Dive activity.
"""

import os
import sys

try:
    from importlib import metadata as importlib_metadata
except ImportError:
    # Backwards compatibility - importlib.metadata was added in Python 3.8
    import importlib_metadata

import ppb
import pathunstrom_splash

import endlessbattle.shared as shared


class EndlessBattle(ppb.Scene):
    background_color = 16, 35, 35

    def __init__(self, **props):
        super().__init__(**props)

        self.add(ppb.Sprite(
            image=ppb.Text("Endless Battle", font=shared.title_font, color=(145, 24, 24)),
            size=2
        ))

    def on_key_pressed(self, event, signal):
        signal(ppb.events.ReplaceScene(pathunstrom_splash.Splash(next_scene=EndlessBattle)))


def main():
    # Linux desktop environments use app's .desktop file to integrate the app
    # to their application menus. The .desktop file of this app will include
    # StartupWMClass key, set to app's formal name, which helps associate
    # app's windows to its menu item.
    #
    # For association to work any windows of the app must have WMCLASS
    # property set to match the value set in app's desktop file. For PPB this
    # is set using environment variable.

    # Find the name of the module that was used to start the app
    app_module = sys.modules['__main__'].__package__
    # Retrieve the app's metadata
    metadata = importlib_metadata.metadata(app_module)

    os.environ['SDL_VIDEO_X11_WMCLASS'] = metadata['Formal-Name']

    ppb.run(
        starting_scene=pathunstrom_splash.Splash,
        scene_kwargs={"next_scene": EndlessBattle},
        title=metadata['Formal-Name'],
    )
