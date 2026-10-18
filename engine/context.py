class ContextManager:
    def __init__(self):
        self.history = []

    def update(self, user_input, response):
        self.history.append({
            "user": user_input,
            "assistant": response
        })

        if len(self.history) > 10:
            self.history.pop(0)

    def get_context(self):
        return self.history
