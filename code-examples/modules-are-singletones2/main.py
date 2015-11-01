import logging

import toolshed

logging.basicConfig(format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d]  %(message)s',
                    level=logging.DEBUG)

toolshed.check_tool_exist('hammer')


