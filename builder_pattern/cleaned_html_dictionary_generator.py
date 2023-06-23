def generate_webform(field_dict_list) -> str:
    generated_field_list = []
    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            field_html = generate_text_field(field_dict)
        elif field_dict["type"] == "checkbox":
            field_html = generate_checkbox(field_dict)
        generated_field_list.append(field_html)

    generated_fields = "\n".join(generated_field_list)
    return "<form>{fields}</form>".format(fields=generated_fields)


def generate_text_field(text_field_dict):
    return f'{text_field_dict["label"]}:<br><input ' \
           f'type="text" name="{text_field_dict["name"]}"><br>'


def generate_checkbox(checkbox_dict):
    return f'<label><input type="checkbox" ' \
           f'id="{checkbox_dict["id"]}" ' \
           f'value="{checkbox_dict["value"]}"> ' \
           f'{checkbox_dict["label"]}<br>'


def build_html_form(field_list):
    with open("form_file.html", 'w') as f:
        f.write(f'<html><body>{generate_webform(field_list)}</body></html>')


if __name__ == "__main__":
    field_list = [
        {
            "type": "text_field",
            "label": "Best text you have ever written",
            "name": "best_text"
        },
        {
            "type": "checkbox",
            "id": "check_it",
            "value": "1",
            "label": "Check for one",
        },
        {
            "type": "text_field",
            "label": "Another Text field",
            "name": "text_field2"
        }
    ]

    build_html_form(field_list)

"""Stacking loops and conditional statements inside and on top of each other 
quickly becomes unreadable and unmaintainable. Let’s clean up the code a 
bit. We are going to take the meat of each field’s generation code and place 
that into a separate function that takes the dictionary and returns a 
snippet of HTML code that represents that field. The key in this step is to 
clean up the code without changing any of the functionality, input, 
or output of the main function. """