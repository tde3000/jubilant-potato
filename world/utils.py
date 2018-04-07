def search_tags(tags):
    # Using sets for intersect and performance
    # http://blog.michelemattioni.me/2015/01/10/list-intersection-in-python-lets-do-it-quickly/
    tag = tags.pop(0)
    objects = set(search_tag(tag))

    for tag in tags:
        objects = objects.intersection(set(search_tag(tag)))

    return list(objects)


def search_tag(tag):
    from evennia import search_tag as search_base

    # If list/tuple we need to also search category
    if not isinstance(tag, basestring):
        objects = search_base(tag[0], tag[1])
    # Else it's just a string
    else:
        objects = search_base(tag)

    return objects

