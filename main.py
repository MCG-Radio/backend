import gbulb
from aiohttp import web

from mcg_radio.fake_display_controller import FakeDisplayController as DisplayController
#from mcg_radio.buttons_listener import ButtonsListener
from mcg_radio.playback_controller import PlaybackController
from mcg_radio.webapp import index

dc = DisplayController()
dc.setup()

pc = PlaybackController(dc)
pc.update_radios('radios.json')
pc.play(1)

# btl = ButtonsListener(pc)

# GLib and asyncio
gbulb.install()

# WebApp is used as loop.run_forever() bridge
app = web.Application()
app.router.add_get('/', index)
app['PlaybackController'] = pc
web.run_app(app, host='127.0.0.1', port=8080)
