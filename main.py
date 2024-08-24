from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = {'/', '*', '-', '+'}
        self.last_was_operator = False
        self.expression = ""

        layout = GridLayout(cols=4)
        self.result = TextInput(font_size=32, readonly=True, halign='right', size_hint_y=None, height=100)
        layout.add_widget(self.result)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('.', '0', '=', '+'),
            ('C',)
        ]

        for row in buttons:
            h_layout = GridLayout(cols=4)
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        text = instance.text

        if text == 'C':
            self.result.text = ''
            self.expression = ''
        elif text == '=':
            try:
                self.result.text = str(eval(self.expression))
            except Exception as e:
                self.result.text = 'Error'
            self.expression = ''
        else:
            if text in self.operators:
                if self.last_was_operator:
                    return
                self.expression += ' ' + text + ' '
            else:
                self.expression += text
            self.result.text = self.expression
            self.last_was_operator = text in self.operators

if __name__ == '_main_':
    CalculatorApp().run()