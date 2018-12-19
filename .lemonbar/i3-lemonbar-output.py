#!/usr/bin/env python3
from i3lemonbar import BlocksConverter, BarRenderer, Scheduler
from i3lemonbar.containers import default_container
from i3lemonbar.i3wrapper import i3Wrapper

import sys

CONFIG_MODULE = 'i3-lemonbar-config'


def main(stdout=sys.stdout, stderr=sys.stderr):
    config = __import__(CONFIG_MODULE)
    container = default_container(stdout, stderr)
    converter = BlocksConverter(container, config.SEPARATOR)
    bar_renderer = BarRenderer(
        converter.to_renderer(config.LEFT_BLOCKS),
        converter.to_renderer(config.CENTER_BLOCKS),
        converter.to_renderer(config.RIGHT_BLOCKS),
    )
    container.resolve(i3Wrapper).connect()
    container.resolve(Scheduler).start(bar_renderer)


if __name__ == '__main__':
    main()
