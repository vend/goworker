package vetrics

import "github.com/rcrowley/go-metrics"

type MetricsService struct {
	underlyingRegistry metrics.Registry
}

func (s *MetricsService) Timer(name string) Timer {
	underlying := metrics.NewTimer()
	s.underlyingRegistry.Register(name, underlying)
	return WrappedTimer{
		underlying: underlying,
	}
}

func (s *MetricsService) Gauge(name string) Gauge {
	gauge := metrics.NewGauge()
	s.underlyingRegistry.Register(name, gauge)
	return gauge
}

func (s *MetricsService) Counter(name string) Counter {
	counter := metrics.NewCounter()
	s.underlyingRegistry.Register(name, counter)
	return counter
}

func (s *MetricsService) Meter(name string) Meter {
	meter := metrics.NewMeter()
	s.underlyingRegistry.Register(name, meter)
	return meter
}

func (s *MetricsService) Registry() metrics.Registry {
	return s.underlyingRegistry
}
