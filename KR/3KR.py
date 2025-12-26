class HTMLReportMixin:
    def get_html(self):
        return f"<ul>{''.join(f'<li>{e}</li>' for e in self.events)}</ul>"
class EventLogger(HTMLReportMixin):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.events = []
        return cls._instance
    def add_event(self, text):
        self.events.append(text)
logger1 = EventLogger()
logger1.add_event("Запуск системы")
logger2 = EventLogger()
logger2.add_event("Ошибка подключения")
print(logger1 is logger2)
print(logger1.get_html())