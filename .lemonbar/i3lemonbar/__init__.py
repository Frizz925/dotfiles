from .blocks import Block
from .renderers import BarRenderer, BlocksRenderer
from .containers import Container
from inspect import isclass
from threading import Event
from typing import List

import sys


class Scheduler(object):
    def __init__(self):
        self.event = Event()
        self.running = False

    def start(self, bar_renderer: BarRenderer):
        self.running = True
        while self.running:
            self.run(bar_renderer)
            self.sleep()

    def run(self, bar_renderer: BarRenderer):
        try:
            sys.stdout.write(bar_renderer.render())
        except Exception as e:
            sys.stderr.write(str(e))
            sys.stderr.flush()
        sys.stdout.write('\n')
        sys.stdout.flush()

    def sleep(self):
        self.event.wait(1)
        self.event.clear()


class BlocksConverter(object):
    def __init__(self, container: Container, separator='  '):
        self.container = container
        self.separator = separator

    def to_renderer(self, blocks: List) -> BlocksRenderer:
        blocks = self.delegate_blocks(blocks)
        return BlocksRenderer(blocks, self.separator)

    def delegate_blocks(self, blocks: List) -> List[Block]:
        return [self.delegate_block(block) for block in blocks]

    def delegate_block(self, block) -> Block:
        if isclass(block):
            if hasattr(block, '__injected__'):
                block = block(self.container)
            else:
                block = block()
        if callable(block):
            return Block(renderer=block)
        if isinstance(block, Block):
            return block
        raise TypeError('Unknown block type %s' % type(block))


__all__ = [
    'Block', 'BlocksRenderer', 'BarRenderer', 'Scheduler',
    'delegate_blocks', 'delegate_block'
]
