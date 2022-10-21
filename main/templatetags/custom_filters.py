from django.template.defaulttags import register


@register.filter
def gold_range(stars):
    int_stars = int(stars)
    return range(int_stars)


@register.filter
def grey_range(stars):
    int_stars = 5 - int(stars)
    return range(int_stars)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)