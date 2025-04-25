class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes all variables to False and minimum values.
        The following functions will not work unless the power to the tv is on by calling power()
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        method that turns the tv on/off
        :return: tv status
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        method that toggled volume mute on/off. if muted, volume is set to 0
        :return: mute statue
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        method to increase tv channel
        :return: current channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        method to decrease tv channel
        :return: current channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                 self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        """
        method to increase tv volume
        :return: current tv volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        method to decrease tv volume
        :return: current tv volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        method to return the tv status
        :return: tv status
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
