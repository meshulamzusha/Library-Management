class Logger:
    @staticmethod
    def log_action(action_type: str, **details) -> None:
        print(f'{action_type};{details['user_id']};{details['isbn']}')