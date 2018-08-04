
def norm(im, **kw):
    return (im-im.min(**kw))/(im.max(**kw)-im.min(**kw))
