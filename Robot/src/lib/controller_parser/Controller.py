
class Controller:

    joysticks = [None] * 4

    buttons = [None] * 16

    def read_input(self, input):

        for i in range(len(self.joysticks)):
            self.joysticks[i]=input[i]

        for i in range(len(self.buttons)):
            self.buttons[i]=input[i+4]



    def button_press(self):