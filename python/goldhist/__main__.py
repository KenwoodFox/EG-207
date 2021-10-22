# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import logging
import coloredlogs

from goldhist import GoldHist


if __name__ == '__main__':
    # Setup logging
    logger = logging.getLogger(__name__)
    coloredlogs.install(
        fmt='%(asctime)s,%(msecs)03d %(hostname)s %(levelname)s %(message)s',
        level=logging.DEBUG,
        logger=logger)

    logger.info("Program Started.")

    # Make app
    app = GoldHist(logger)

    try:
        app.run()
    except KeyboardInterrupt:
        app.close()
        quit()
