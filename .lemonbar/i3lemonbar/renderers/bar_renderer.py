from .renderer import Renderer
from .blocks_renderer import BlocksRenderer


class BarRenderer(Renderer):
    def __init__(
        self,
        left_renderer: BlocksRenderer,
        middle_renderer: BlocksRenderer,
        right_renderer: BlocksRenderer
    ):
        self.left_renderer = left_renderer
        self.middle_renderer = middle_renderer
        self.right_renderer = right_renderer

    def render(self) -> str:
        bar_str = '%%{l} %s %%{l}' % self.left_renderer.render()
        bar_str += '%%{c} %s %%{c}' % self.middle_renderer.render()
        bar_str += '%%{r} %s %%{r}' % self.right_renderer.render()
        return bar_str
