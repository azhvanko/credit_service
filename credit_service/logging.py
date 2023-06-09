import typing as t

import structlog


def get_logging_config(debug: bool) -> dict[str, t.Any]:
    json_params = {
        'ensure_ascii': False,
        'sort_keys': True,
    }
    if debug:
        json_params['indent'] = 2

    def add_app_context(_, __, event_dict: dict[str, t.Any]) -> dict[str, t.Any]:
        # remove processors meta
        event_dict.pop('_from_structlog')
        event_dict.pop('_record')

        frame, _ = structlog._frames._find_first_app_frame_and_name(['logging', __name__])  # noqa
        event_dict['file'] = frame.f_code.co_filename
        event_dict['line'] = frame.f_lineno
        event_dict['function'] = frame.f_code.co_name

        return event_dict

    if debug:
        dev_processors = [
            structlog.processors.ExceptionPrettyPrinter(),
        ]
    else:
        dev_processors = []

    processors = [
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt='iso'),
        add_app_context,
        *dev_processors,
        structlog.processors.JSONRenderer(**json_params),
    ]

    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': structlog.stdlib.ProcessorFormatter,
                'processors': processors,
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'json',
                'stream': 'ext://sys.stdout',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['console', ],
                'level': 'INFO',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['console', ],
                'level': 'DEBUG' if debug else 'INFO',
                'propagate': False,
            },
            '': {
                'handlers': ['console', ],
                'level': 'DEBUG' if debug else 'INFO',
                'propagate': False,
            },
        },
    }
