#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

# has to be done before importing anything that depends on httpx
# https://github.com/open-telemetry/opentelemetry-python-contrib/issues/1742
HTTPXClientInstrumentor().instrument()

from opentelemetry import trace, metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk._logs import LoggerProvider
from opentelemetry._logs import set_logger_provider
from opentelemetry._events import set_event_logger_provider
from opentelemetry.sdk._logs.export import SimpleLogRecordProcessor
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

from events import MyEventLoggerProvider

def configure_tracing() -> TracerProvider:
    provider = TracerProvider()
    provider.add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))
    trace.set_tracer_provider(provider)
    return provider

def configure_metrics() -> MeterProvider:
    reader = PrometheusMetricReader()
    provider = MeterProvider(metric_readers=[reader, PeriodicExportingMetricReader(OTLPMetricExporter())])
    metrics.set_meter_provider(provider)
    return provider

def configure_logging():
    provider = LoggerProvider()
    provider.add_log_record_processor(SimpleLogRecordProcessor(OTLPLogExporter()))
    event_provider = MyEventLoggerProvider(provider)
    set_logger_provider(provider)
    set_event_logger_provider(event_provider)
    return (provider, event_provider)

def main():
    configure_tracing()
    configure_metrics()
    configure_logging()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat.settings")
    DjangoInstrumentor().instrument()
    OpenAIInstrumentor().instrument()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
