def generate_webform(text_field_list=[], checkbox_field_list=[]):
    generated_fields = "\n".join(
        map(
            lambda x: f'{x}:<br><input type="text" name="{x}"><br>',
            text_field_list
        )
    )
    generated_fields += "\n".join(
        map(
            lambda x: f'<label><input type="checkbox" id="{x}" value="{x}">'
                      f'{x}<br>',
            checkbox_field_list
            )
        )
    return f'<form>{generated_fields}</form>'


def build_html_form(text_field_list=[], checkbox_field_list=[]):
    with open("form_file.html", 'w') as f:
        f.write(
            "<html><body>{}</body></html>".format(
                generate_webform(
                    text_field_list=text_field_list,
                    checkbox_field_list=checkbox_field_list
                )
            )
        )


if __name__ == "__main__":
    text_fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ["awesome", "bad"]
    build_html_form(
        text_field_list=text_fields,
        checkbox_field_list=checkbox_fields
    )

"""
There are clear issues with this approach, the first of which is the fact that we cannot
deal with fields that have different defaults or options or in fact any information beyond a
simple label or field name. We are now going to extend the functionality of the formgenerator
function so we can cater for a large number of field types, each with its own
settings. We also have the issue that there is no way to interleave different types of fields. To
show you how this would work, we are ripping out the named parameters and replacing
them with a list of dictionaries. please see the NEXT FILE 
html_dictionary_generator.
"""