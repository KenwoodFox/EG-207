# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import logging
import coloredlogs

from serial.serialutil import SerialException
from goldplot import GoldPlotApp


if __name__ == '__main__':
    # Setup logging
    logging.basicConfig(level=logging.DEBUG)
    coloredlogs.install()

    # Make app
    app = GoldPlotApp()

    try:
        app.run()
    except KeyboardInterrupt:
        app.close()
        quit()
    except SerialException:
        logging.error("Could not find arduino, try with -d option?")
