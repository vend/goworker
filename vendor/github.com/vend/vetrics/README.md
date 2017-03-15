# vetrics
Metrics for Go, allows exporting Counters, Gauges and Timers to Datadog et al

DRI: Nick Walker

[![wercker status](https://app.wercker.com/status/c4827d0e82b2fa4315712c0f5646fe58/m/master "wercker status")](https://app.wercker.com/project/bykey/c4827d0e82b2fa4315712c0f5646fe58)

## Common Usage

```go
package main

import "github.com/vend/vetrics"

func defaultUsage() {
  // Enable Datadog
  vetrics.EnableDatadog("123-573")

  // Ready to use!
}

func timer() {
  // Using a timer
  timer := vetrics.Metrics().Timer("operation")

  // Do some work you want to time
  doWork()

  // All done!
  timer.Stop()
}

func gauge() {
  gauge := vetrics.Metrics().Gauge("some_gauge")
  gauge.Update(123)
}

func counter() {
  counter := vetrics.Metrics().Counter("number_of_donuts")

  // Increment by 1
  counter.Inc(1)

  // Decrement by 2
  counter.Dec(2)
}
```

