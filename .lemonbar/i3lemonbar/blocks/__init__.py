class Block(object):
    def __init__(self, renderer=None):
        self.renderer = renderer

    def should_update(self) -> bool:
        return True

    def render(self) -> str:
        if isinstance(self.renderer, str):
            return self.renderer
        if callable(self.renderer):
            return self.renderer()
        return ''
