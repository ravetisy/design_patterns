"""In the builder pattern, the two main players are the Builder and the
Director. The Builder is an abstract class that knows how to build all the
components of the final object. In our case, the Builder class will know how
to build each of the field types. It can assemble the various parts into a
complete form object. The Director controls the process of building. There
is an instance (or instances) of Builder that the Director uses to build the
webform. The output from the Director is a fully initialized object—the
webform, in our example. The Director implements the set of instructions for
setting up a webform from the fields it contains. This set of instructions
is independent of the types of the individual fields passed to the director.
"""

from abc import ABC, abstractmethod, ABCMeta


class Director(metaclass=ABCMeta):
    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, field_list):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


class Builder(metaclass=ABCMeta):

    def __init__(self, constructed_object):
        self.constructed_object = constructed_object


class Product:

    def __init__(self):
        pass

    def __repr__(self):
        pass


class AbstractFormBuilder(metaclass=ABCMeta):
    def __init__(self):
        self.constructed_object = None

    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_checkbox(self, checkbox_dict):
        pass

    @abstractmethod
    def add_button(self, button_dict):
        pass


class HtmlForm(object):

    def __init__(self):
        self.field_list = []

    def __repr__(self):
        html_txt = f'<form>{"".join(self.field_list)}</form>'
        return html_txt


class HtmlFormBuilder(AbstractFormBuilder):

    def __init__(self):
        super().__init__()
        self.constructed_object = HtmlForm()

    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            f'{field_dict["label"]}:<br><input type="text" name='
            f'"{field_dict["field_name"]}"><br>'
        )

    def add_checkbox(self, checkbox_dict):
        self.constructed_object.field_list.append(
            f'<label><input type="checkbox" '
            f'id="{checkbox_dict["field_id"]}" '
            f'value="{checkbox_dict["value"]}"> '
            f'{checkbox_dict["label"]}<br>'
        )

    def add_button(self, button_dict):
        self.constructed_object.field_list.append(
            f'<button type="button">{button_dict["text"]}</button>'
        )


class FormDirector(Director):
    def __init__(self):
        Director.__init__(self)

    def construct(self, field_list):
        for field in field_list:
            if field['field_type'] == 'text_field':
                self._builder.add_text_field(field)
            elif field['field_type'] == 'checkbox':
                self._builder.add_checkbox(field)
            elif field['field_type'] == 'button':
                self._builder.add_button(field)


if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)
    field_list = [
        {
            "field_type": "text_field",
            "label": "Best text you have ever written",
            "field_name": "Field One"
        },
        {
            "field_type": "checkbox",
            "field_id": "check_it",
            "value": "1",
            "label": "Check for on",
        },
        {
            "field_type": "text_field",
            "label": "Another Text field",
            "field_name": "Field One"
        },
        {
            "field_type": "button",
            "text": "DONE"
        }
    ]

    director.construct(field_list)
    with open("form_file.html", 'w') as f:
        f.write(
            f'<html><body>{director.get_constructed_object()}</body></html>'
        )


class ConcreteBuilder(Builder):
    pass


class ConcreteDirector(Director):
    pass
