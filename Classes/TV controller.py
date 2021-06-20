# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last
# channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
# exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.
channels = ["BBC", "Discovery", "TV1000"]


class TVController:
    actual_channel = 0

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[len(channels)-1]

    def turn_channel(self, a):
        try:
            if int(a) > len(channels):
                print("There is no channel with this number")
            else:
                return self.channels[int(a) - 1]
        except ValueError:
            print("Write a number")

    def next_channel(self):
        TVController.actual_channel += 1
        if TVController.actual_channel == len(self.channels):
            TVController.actual_channel = 0
        return self.channels[TVController.actual_channel]

    def previos_channel(self):
        TVController.actual_channel -= 1
        if TVController.actual_channel == self.channels[0]:
            TVController.actual_channel = len(channels) - 1
        return self.channels[TVController.actual_channel]

    def current_channel(self):
        return self.channels[TVController.actual_channel]

    def is_exist(self, exist_channel):
        exist_channel = str(exist_channel)
        if exist_channel.isdigit():
            if int(exist_channel) > len(self.channels):
                return print("Channel doesnt exist")
            else:
                return print("Channel exist in the list")
        else:
            if exist_channel not in self.channels:
                return print("Channel doesnt exist")
            else:
                return print("Channel exist in the list")
# vertaye none


my_controller = TVController(channels)
# print(my_controller.first_channel())
# print(my_controller.last_channel())
# print(my_controller.turn_channel(2))
# print(my_controller.next_channel())
# print(my_controller.previos_channel())
# print(my_controller.current_channel())
print(my_controller.is_exist("BBC"))
