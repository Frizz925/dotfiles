from .renderer import Renderer
from ..blocks import Block
from inspect import isclass
from typing import List

import codecs


class BlocksRenderer(Renderer):
    def __init__(self, blocks: List[Block], separator='  '):
        self.blocks = blocks
        self.separator = separator
        self.render_map = {}

    def render(self) -> str:
        separator = self.render_separator()
        blocks = map(self.render_block, self.blocks)
        blocks = filter(None, blocks)
        return separator.join(blocks)

    def render_separator(self) -> str:
        return self.separator

    def render_block(self, block: Block) -> str:
        if block in self.render_map and not block.should_update():
            return self.render_map[block]
        rendered = block.render()
        self.render_map[block] = rendered
        return rendered

    def block_to_str(self, block) -> str:
        if isclass(block):
            block = block()
        if callable(block):
            return block()
        if isinstance(block, Block):
            return block.render()
        if isinstance(block, str):
            return block
        if isinstance(block, bytes):
            return codecs.decode(block, 'utf-8')
        raise TypeError('Unknown block type of %s' % type(block))
