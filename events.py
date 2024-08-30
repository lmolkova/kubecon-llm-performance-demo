from time import time_ns
from typing import Optional

from opentelemetry._events import Attributes, EventLoggerProvider, EventLogger, Event, get_event_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, Logger, LogRecord
from opentelemetry._logs import SeverityNumber
from opentelemetry.trace import get_current_span

class MyEventLoggerProvider(EventLoggerProvider):
    def __init__(self, logger_provider: LoggerProvider):
        self._logger_provider = logger_provider

    def get_event_logger(
        self,
        name: str,
        version: Optional[str] = None,
        schema_url: Optional[str] = None,
        attributes: Optional[Attributes] = None,
    ) -> EventLogger:
        return MyEventLogger(self._logger_provider, name, version, schema_url, attributes)

class MyEventLogger(EventLogger):
    def __init__(
        self,
        logger_provider: LoggerProvider,
        name: str,
        version: Optional[str] = None,
        schema_url: Optional[str] = None,
        attributes: Optional[Attributes] = None,
    ):
        super().__init__(
            name=name,
            version=version,
            schema_url=schema_url,
            attributes=attributes,
        )
        self._logger: Logger = logger_provider.get_logger(name, version, schema_url, attributes)

    @property
    def _event_logger(self) -> EventLogger:
        return self._logger

    def emit(self, event: Event) -> None:
        log_record = LogRecord(
                timestamp=event.timestamp or time_ns(),
                observed_timestamp=event.observed_timestamp or time_ns(),
                trace_id=event.trace_id or get_current_span().get_span_context().trace_id,
                span_id=event.span_id or get_current_span().get_span_context().span_id,
                trace_flags=event.trace_flags or get_current_span().get_span_context().trace_flags,
                severity_text=event.severity_text,
                severity_number=event.severity_number or SeverityNumber.UNSPECIFIED,
                body=event.body,
                resource=self._logger.resource,
                attributes=event.attributes
            )
        self._logger.emit(log_record)