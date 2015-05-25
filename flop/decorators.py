from django.utils.decorators import classonlymethod
from django.utils.six import wraps


def view_decorator(fdec):
    """
    Change a function decorator into a view decorator.

    https://github.com/lqc/django/tree/cbvdecoration_ticket14512
    """
    def decorator(cls):
        if not hasattr(cls, "as_view"):
            raise TypeError("Only decorate subclasses of View, not mixins.")
        original = cls.as_view.im_func

        @wraps(original)
        def as_view(current, **initkwargs):
            return fdec(original(current, **initkwargs))
        cls.as_view = classonlymethod(as_view)
        return cls
    return decorator
