"""The if statements are still there, but at least now the code is a little
cleaner. These sprawling if statements will keep growing as we add more
field types to the form generator. Let’s try to better the situation by
using an object-oriented approach. We could use polymorphism to deal with
some specific fields and the issues we are having in generating them
"""


class HtmlField(object):
    def __init__(self, **kwargs):
        self.html = ""
        if kwargs['field_type'] == "text_field":
            self.html = HtmlField.construct_text_field(
                kwargs["label"],
                kwargs["field_name"]
            )
        elif kwargs['field_type'] == "checkbox":
            self.html = HtmlField.construct_checkbox(
                kwargs["field_id"],
                kwargs["value"], kwargs["label"]
            )

    @staticmethod
    def construct_text_field(label, field_name):
        return f'{label}:<br><input type="text" name="{field_name}"><br>'

    @staticmethod
    def construct_checkbox(field_id, value, label):
        return f'<label><input type="checkbox" ' \
               f'id="{field_id}" ' \
               f'value="{value}">' \
               f'{label}<br>'

    def __str__(self):
        return self.html


def generate_webform(field_dict_list) -> str:
    generated_field_list = []
    for field in field_dict_list:
        try:
            generated_field_list.append(str(HtmlField(**field)))
        except KeyError as e:
            print(f'invalid key for **kwargs: {e}')
    generated_fields = "\n".join(generated_field_list)
    return f'<form>{generated_fields}</form>'


def build_html_form(field_list):
    with open("form_file.html", 'w') as f:
        f.write(f'<html><body>{generate_webform(field_list)}</body></html>')


if __name__ == "__main__":
    field_list = [
        {
            "field_type": "text_field",
            "label": "Best text you have ever written",
            "field_name": "best_text"
        },
        {
            "field_type": "checkbox",
            "field_id": "check_it",
            "value": "1",
            "label": "Check for one",
        },
        {
            "field_type": "text_field",
            "label": "Another Text field",
            "field_name": "text_field2"
        }
    ]
    build_html_form(field_list)