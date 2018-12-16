"""Util functions used by Netdisco."""
from collections import defaultdict
from typing import Any, Dict, List, Optional  # noqa: F401


# Taken from http://stackoverflow.com/a/10077069
# pylint: disable=invalid-name
def etree_to_dict(t):
    """Convert an ETree object to a dict."""
    # strip namespace
    tag_name = t.tag[t.tag.find("}")+1:]

    d = {
        tag_name: {} if t.attrib else None
    }  # type: Dict[str, Optional[Dict[str, Any]]]
    children = list(t)
    if children:
        dd = defaultdict(list)  # type: Dict[str, List]
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {tag_name: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    dt = d[tag_name]
    if t.attrib:
        assert dt is not None
        dt.update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                assert dt is not None
                dt['#text'] = text
        else:
            d[tag_name] = text
    return d
