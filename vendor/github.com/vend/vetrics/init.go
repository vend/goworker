package vetrics

import (
	"os"
	"time"

	stdlog "log"

	"github.com/markchadwick/go-datadog"
	"github.com/rcrowley/go-metrics"
	"github.com/vend/config"
	"github.com/vend/go-common/shutdown"
)

var shared MetricsInterface

func Metrics() MetricsInterface {
	if shared == nil {
		metricsPrefix := config.String("METRICS_PREFIX", "")
		if metricsPrefix == "" {
			metricsPrefix = config.String("SOURCE_PROGRAM", "unknown")
		}

		// We don't have a registry, just create the default one!
		underlyingRegistry := metrics.NewPrefixedRegistry(metricsPrefix + ".")
		shared = &MetricsService{
			underlyingRegistry: underlyingRegistry,
		}
	}

	return shared
}

func EnableDatadog(datadogKey string) {
	host, _ := os.Hostname()
	dog := datadog.New(host, datadogKey).Reporter(Metrics().Registry())
	go dog.Start(60 * time.Second)
	shutdown.Register("datadog-metrics", func() {
		dog.Report()
	})
}

func EnableStderr() {
	go metrics.Log(Metrics().Registry(), 60*time.Second, stdlog.New(os.Stderr, "metrics: ", stdlog.Lmicroseconds))
}

func SetMetrics(metrics MetricsInterface) {
	shared = metrics
}
