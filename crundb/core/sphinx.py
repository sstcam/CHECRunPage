import jinja2


def simple_tbl(data: list, col_keys: list) -> str:
    """Generates a simple rst table

    Args:
        data (list): table data each element is a dict with col_keys and values
        col_keys (list): The columns of the table

    Returns:
        str: The table formated for rst
    """
    tmpl = """{% for key,l in keys.items() -%}
{{'='*l }}{{' '}}
{%- endfor %}
{#-#}
{% for key,l in keys.items() -%}
{{key}}{{' '*(l - (key|length)+1)}}
{%- endfor %}
{#-#}
{% for key,l in keys.items() -%}
{{'='*l }}{{' '}}
{%- endfor -%}
{#-#}
{%- for row in data %}
{% for col,l in zip(row.values(),keys.values()) -%}
{{col}}{{' '*(l - (col|length)+1)}}
{%- endfor %}
{%- endfor %}
{% for key,l in keys.items() -%}
{{'='*l }}{{' '}}
{%- endfor %}
    """
    widths = {key: len(key) for key in col_keys}
    for row in data:
        for key in col_keys:
            widths[key] = max((widths[key], len(row[key])))
    t = jinja2.Template(tmpl)
    return t.render(keys=widths, data=data, zip=zip)


def get_toc_tmpl() -> str:
    """Summary

    Returns:
        str: Description
    """
    return """.. toctree::
{%- for section in sections %}
    {{section}}
{%- endfor %}
{%- for directive, arg in directives.items() %}
    :{{directive}}: {{arg}}
{%- endfor %}
"""


def toc(sections: list, **kwargs) -> str:
    """Summary

    Args:
        sections (list): Description
        **kwargs: Description

    Returns:
        str: Description
    """
    tmpl = get_toc_tmpl()
    t = jinja2.Template(tmpl)
    return t.render(sections=sections, directives=kwargs)
