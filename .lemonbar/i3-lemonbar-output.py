#!/usr/bin/env python3
from i3lemonbar import BlocksConverter, BarRenderer, Scheduler
from i3lemonbar.containers import default_container

CONFIG_MODULE = 'i3-lemonbar-config'


def main():
    config = __import__(CONFIG_MODULE)
    container = default_container()
    converter = BlocksConverter(container, config.SEPARATOR)
    bar_renderer = BarRenderer(
        converter.to_renderer(config.LEFT_BLOCKS),
        converter.to_renderer(config.CENTER_BLOCKS),
        converter.to_renderer(config.RIGHT_BLOCKS),
    )
    container.resolve(Scheduler).start(bar_renderer)


if __name__ == '__main__':
    main()
