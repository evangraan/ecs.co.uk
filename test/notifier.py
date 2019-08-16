class TestNotifier:
    notifications = []

    def notify(self, message):
        self.notifications.append(message)

    def wasNotified(self, message):
        for entry in self.notifications:
            if entry == message:
                return True
        return False

    def clear(self):
        notifications = []
