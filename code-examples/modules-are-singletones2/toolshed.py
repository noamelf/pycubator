import logging

tools = {
    'screw': 5,
    'hammer': 0
}


def check_tool_exist(tool):
    have_tool = tools.get(tool)
    if not have_tool:
        logging.error('There are no {}'.format(tool))
        raise RuntimeError()

