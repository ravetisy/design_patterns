def generate_webform(field_dict_list) -> str:
    generated_field_list = []
    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            generated_field_list.append(
                f'{field_dict["label"]}:<br><input type="text" name="{field_dict["name"]}"><br>'
            )
        elif field_dict["type"] == "checkbox":
            generated_field_list.append(
                '<label><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(
                    field_dict["id"],
                    field_dict["value"],
                    field_dict["label"]
                )
            )
    generated_fields = "\n".join(generated_field_list)
    return f'<form>{generated_fields}</form>'


def build_html_form(field_list) -> None:
    with open("form_file.html", 'w') as f:
        f.write(
            f'<html><body>{generate_webform(field_list)}</body></html>'
        )


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
