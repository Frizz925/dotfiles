from .blocks import Block, BlockRenderer
from inspect import isclass
from threading import Event
from typing import List

import sys


class Scheduler(object):
    def __init__(self, left_blocks=[], center_blocks=[], right_blocks=[]):
        self.left_renderer = self.init_renderer(left_blocks)
        self.center_renderer = self.init_renderer(center_blocks)
        self.right_renderer = self.init_renderer(right_blocks)
        self.event = Event()
        self.running = False

    def init_renderer(self, blocks: List):
        return BlockRenderer(self.delegate_blocks(blocks))

    def delegate_blocks(self, blocks: List):
        return list(map(self.delegate_renderer, blocks))

    def delegate_renderer(self, renderer):
        if isclass(renderer):
            # TODO: Create lightweight dependency injection
            renderer = renderer(self)
        if isinstance(renderer, Block):
            return renderer
        return Block(self, renderer=renderer)

    def start(self):
        self.running = True
        while self.running:
            self.run()
            self.sleep()

    def run(self):
        sys.stdout.write('%%{l} %s %%{l}' % self.left_renderer.render())
        sys.stdout.write('%%{c} %s %%{c}' % self.center_renderer.render())
        sys.stdout.write('%%{r} %s %%{r}' % self.right_renderer.render())
        sys.stdout.write('\n')
        sys.stdout.flush()

    def sleep(self):
        self.event.wait(1)
        self.event.clear()


__all__ = ['Block', 'BlockRenderer']
