# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import logging
import coloredlogs

from serial.serialutil import SerialException
from goldplot import GoldPlotApp


if __name__ == '__main__':
    # Setup logging
    logger = logging.getLogger(__name__)
    coloredlogs.install(
        fmt='%(asctime)s,%(msecs)03d %(hostname)s %(levelname)s %(message)s',
        level=logging.DEBUG,
        logger=logger)

    logger.info("Program Started.")

    # Make app
    app = GoldPlotApp(logger)

    try:
        app.run()
    except KeyboardInterrupt:
        app.close()
        quit()
    except SerialException:
        logging.error("Could not find arduino, try with -d option?")
