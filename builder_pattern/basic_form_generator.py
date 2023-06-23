def generate_webform(field_list):
    generated_fields = "\n".join(
        map(
            lambda x: f'{x}:<br><input type="text" name="{x}"><br>',
            field_list
        )
    )
    return "<form>{fields}</form>".format(fields=generated_fields)


def build_html_form(fields):
    with open("form_file.html", 'w') as f:
        f.write(
        f'<html><body>{generate_webform(fields)}</body></html>'
        )


if __name__ == "__main__":
    fields = ["name", "age", "email", "telephone"]
    print(generate_webform(fields))
    build_html_form(fields=fields)
