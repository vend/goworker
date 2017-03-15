package vetrics

import (
	"time"

	"github.com/rcrowley/go-metrics"
)

type MetricsInterface interface {
	Timer(name string) Timer
	Gauge(name string) Gauge
	Counter(name string) Counter
	Meter(name string) Meter

	Registry() metrics.Registry
}

type Timer interface {
	Start() StartedTimer
	Update(time.Duration)
	UpdateSince(time.Time)
}

type StartedTimer interface {
	Stop()
}

type Gauge interface {
	Update(int64)
}

type Meter interface {
	Mark(int64)
}

type Counter interface {
	Dec(int64)
	Inc(int64)
}
