from inspect import isclass
from typing import Callable
import functools


class Container(object):
    def __init__(self):
        self.bindings = {}

    def bind(self, xtype: type, instance):
        self.bindings[xtype] = instance

    def resolve(self, xtype: type):
        if xtype in self.bindings:
            return self.bindings[xtype]
        raise ValueError('Can\'t find binding for type %s' % xtype)


def inject(*args, **kwargs) -> Callable:
    def wrapper(obj) -> Callable:
        inject_wrapper = create_func_wrapper(obj, args, kwargs)
        if isclass(obj):
            inject_wrapper = create_cls_wrapper(obj, args, kwargs)
        setattr(inject_wrapper, '__injected__', True)
        return inject_wrapper
    return wrapper


def create_cls_wrapper(cls, args, kwargs):
    @functools.wraps(cls, updated=())
    class ClsInjection(cls):
        def __init__(self, container: Container):
            (deps, kwdeps) = resolve_dependencies(container, args, kwargs)
            cls.__init__(self, *deps, **kwdeps)
    return ClsInjection


def create_func_wrapper(func, args, kwargs):
    @functools.wraps(func)
    def wrapper_func(container: Container):
        (deps, kwdeps) = resolve_dependencies(container, args, kwargs)
        return func(*deps, **kwdeps)
    return wrapper_func


def resolve_dependencies(container: Container, reqs=(), kwreqs={}) -> tuple:
    deps = [container.resolve(req) for req in reqs]
    kwdeps = {}
    for key, req in kwreqs.items():
        kwdeps[key] = container.resolve(req)
    return (deps, kwdeps)


def default_container() -> Container:
    from .. import Scheduler
    from ..i3wrapper import i3Wrapper
    container = Container()
    container.bind(Scheduler, Scheduler())
    container.bind(i3Wrapper, i3Wrapper())
    return container
